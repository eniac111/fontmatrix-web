#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Blagovest Petrov <blagovest@petrovs.info>
# SPDX-License-Identifier: GPL-2.0-or-later
"""Draws the social sharing card that Facebook, Mastodon and the rest show.

Open Graph wants 1200x630; the site's own screenshots are 1280x800, so they
cannot be used directly without the services cropping them badly. This builds a
card at the right size out of the site's own pieces: the colours from
assets/style.css, the Veleka World text face from static/fonts/, the application
icon, and one screenshot.

  static/images/og-default.png    1200x630, referenced by layouts/baseof.html

Run it again after changing the colours, the screenshot or the wordmark:

  python3 tools/make-og-image.py

It needs Pillow, fontTools with brotli (to read the woff2 files) and
rsvg-convert (to rasterise the icon).
"""

from __future__ import annotations

import io
import subprocess
import sys
import tempfile
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent

# The tokens from :root in assets/style.css, light scheme.
PAPER = (251, 250, 246)
INK = (29, 28, 26)
MUTED = (107, 103, 96)
RULE = (220, 216, 207)
ACCENT = (155, 44, 31)

WIDTH, HEIGHT = 1200, 630
MARGIN = 72

HEADLINE = "Fontmatrix"
TAGLINE = "A font manager for people who\nwork with thousands of fonts."
DOMAIN = "fontmatrix.l10n-bg.dev"

SCREENSHOT = ROOT / "static" / "images" / "list.png"
ICON = ROOT / "static" / "images" / "fontmatrix.svg"
OUT = ROOT / "static" / "images" / "og-default.png"


def load_face(stem: str, size: int, tmp: Path) -> ImageFont.FreeTypeFont:
    """Unpacks one of the site's woff2 files far enough for Pillow to draw it."""
    woff2 = ROOT / "static" / "fonts" / f"{stem}.woff2"
    ttf = tmp / f"{stem}.ttf"
    if not ttf.exists():
        font = TTFont(str(woff2))
        font.flavor = None
        font.save(str(ttf))
    return ImageFont.truetype(str(ttf), size)


def render_icon(px: int) -> Image.Image:
    out = subprocess.run(
        ["rsvg-convert", "-w", str(px), "-h", str(px), str(ICON)],
        check=True,
        capture_output=True,
    )
    return Image.open(io.BytesIO(out.stdout)).convert("RGBA")


def rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([(0, 0), (size[0] - 1, size[1] - 1)],
                                           radius=radius, fill=255)
    return mask


def panel(img: Image.Image, radius: int = 10) -> tuple[Image.Image, Image.Image]:
    """Rounds the screenshot's corners, hairlines it, and casts a soft shadow."""
    mask = rounded_mask(img.size, radius)
    card = img.convert("RGBA")
    card.putalpha(mask)

    edge = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(edge).rounded_rectangle(
        [(0, 0), (img.size[0] - 1, img.size[1] - 1)],
        radius=radius, outline=RULE + (255,), width=1)
    card.alpha_composite(edge)

    pad = 48
    shadow = Image.new("RGBA", (img.size[0] + pad * 2, img.size[1] + pad * 2),
                       (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle(
        [(pad, pad + 8), (pad + img.size[0], pad + img.size[1] + 8)],
        radius=radius, fill=(29, 28, 26, 46))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    return card, shadow


def main() -> int:
    for path in (SCREENSHOT, ICON):
        if not path.exists():
            sys.exit(f"missing {path.relative_to(ROOT)}")

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        bold = load_face("VelekaWorld-Bold", 92, tmp)
        regular = load_face("VelekaWorld-Regular", 37, tmp)
        small = load_face("VelekaWorld-Bold", 25, tmp)

        canvas = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
        draw = ImageDraw.Draw(canvas)

        # The screenshot sits on the right and bleeds off that edge, so the card
        # reads as a window onto the application rather than a boxed thumbnail.
        shot = Image.open(SCREENSHOT).convert("RGB")
        # Drop the empty part of the font list below the last row, so the panel
        # is all interface and the rows stay legible at feed size.
        shot = shot.crop((0, 0, shot.width, 664))
        shot_w = 700
        shot_h = round(shot.height * shot_w / shot.width)
        shot = shot.resize((shot_w, shot_h), Image.LANCZOS)
        card, shadow = panel(shot)
        x = WIDTH - shot_w + 96
        y = (HEIGHT - shot_h) // 2
        canvas.paste(shadow, (x - 48, y - 48), shadow)
        canvas.paste(card, (x, y), card)

        # Left column: icon, wordmark, tagline, then the domain.
        icon = render_icon(60)
        canvas.paste(icon, (MARGIN, 128), icon)

        draw.text((MARGIN, 206), HEADLINE, font=bold, fill=INK)
        draw.multiline_text((MARGIN, 326), TAGLINE, font=regular, fill=MUTED,
                            spacing=12)

        draw.line([(MARGIN, HEIGHT - 132), (MARGIN + 54, HEIGHT - 132)],
                  fill=ACCENT, width=3)
        draw.text((MARGIN, HEIGHT - 112), DOMAIN, font=small, fill=ACCENT)

        OUT.parent.mkdir(parents=True, exist_ok=True)
        canvas.save(OUT, "PNG", optimize=True)

    size = OUT.stat().st_size
    print(f"{OUT.relative_to(ROOT)}  {WIDTH}x{HEIGHT}  {size // 1024} KiB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
