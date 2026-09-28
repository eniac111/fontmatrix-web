---
title: Fontmatrix 1.0.0
date: 2026-09-25
description: Qt 6 and KDE Frameworks 6, variable and colour fonts, right-to-left text, font activation everywhere.
---

Fontmatrix 1.0.0 finishes the move to Qt 6 and KDE Frameworks 6 and adds
support for modern font technologies. [Download it](/download/).

## Highlights

- **Variable fonts.** A new *Variations* panel lets you pick a named instance or
  move each axis with a slider. The glyph chart, Playground, Compare and the font
  book all use the chosen coordinates, and Fontmatrix remembers them between
  sessions. The family list can show one row per named instance.
- **Colour fonts.** CBDT and sbix bitmaps (such as Noto Color Emoji), COLR v0,
  COLR v1 and OpenType-SVG glyphs render in colour. Before, they showed as grey
  shapes or red boxes.
- **Right-to-left text.** Arabic, Hebrew and other right-to-left scripts are laid
  out in their own direction, with the Unicode bidirectional algorithm and
  mirrored glyphs.
- **Font activation on every platform.** On Linux, activated fonts go to
  `~/.local/share/fonts/fontmatrix` and Fontmatrix no longer edits your
  `fonts.conf`; an optional helper activates fonts for all users. On Windows,
  activation works for the first time, without administrator rights.
- **New filters** by language coverage, licence and font technology.
- **Duplicate finder** (*Tools → Duplicates*): identical files, and fonts with
  the same family, style and version, shown in groups.

## Also new

- *Export font list as XeTeX* in the Tools menu.
- Samples are hyphenated in their own language with the system's libhyphen.
- The handbook opens in a window of its own where KDE Help Center is missing.
- Remote directories are back.
- The Bulgarian translation is complete. **Human translators for other
  languages are wanted.**

## Removed

The PythonQt scripting engine, the QtWebEngine help browser, the embedded copies
of HarfBuzz and libhyphen (the system libraries are used now), and the ICU,
m17n and Pango shapers.

The [full release notes](https://github.com/fontmatrix/fontmatrix/releases/tag/v1.0.0)
list every change, including the bug fixes and the packaging work.
