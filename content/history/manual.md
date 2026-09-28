---
title: "Manual"
date: 2008-02-01
kind: page
original: http://fontmatrix.be/node/10
weight: 70
description: "The introduction and chapter plan of the first manual."
---

## Introduction

Fontmatrix is a real Linux font manager, available on any platform and as well
for KDE (which already had Kfontinstaller) as for Gnome.

It's purpose is to recursively query the fonts (ttf, ps & otf) in the
directories you give it to search, sort them quickly, (avoiding bugged or
broken ones) and show them.

Then, you can tag them, sub-tag, re-sort according various tags, preview...
Even create a pdf Font Book...

Next step, you will activate/deactivate the fonts you want at that moment using
the tags system constituting various "user profiles needs", with more sub-tags
if created, family check box grouping automatically all variations (regular,
italic, bold etc.) of one font, or even fonts selected one by one.

Each font selected can show different kind of information: name and family
related, detailed font information; one word preview (user defined); one
sentence (or set of character) preview with the ability to keep various user's
sets in the preferences; detailed glyphs view according various subsets (ie
Basic Latin, Punctuation, Mathematical Operators... and of course All Glyphs).

If you see then that the perfect font you wanted is missing one glyph or that
you want to modify one other, just call Fontforge from within Fontmatrix (if
installed of course).

And most of all, if you aren't still happy because the only function you
wanted is not available, just go to the bug tracker and ask kindly what you'd
like, then for sure if it's a good idea, it will be done! And if you want to
debate to explain in life, come to irc: #fontmatrix channel at freenode.

## The other chapters

The rest of the manual was never written; the chapters held only these notes:

- **First step** — Importing fonts. The different parts of the UI.
- **Fundamentals about management** — Here explain how Fontmatrix plays with
  fontconfig + how tags are stored.
- **Menu Bar** — Yes, Fontmatrix is an advanced software and thus provide a new
  generation widget called the menu bar, take a tour!
  - **File** — Most of the file menu items goes here.
  - **Font book** — How it works. How one can write templates.
  - **Edit** — All but tagsets.
  - **Tagsets** — It's for you Vlad. *Go on! I'll catch up... :)*
- **Rendering - the sample preview** — Here explain what's different kind of
  rendering, mainly between "absolute" and freetype.
- **Harfbuzz - advanced typo & multilinguism** — OTF features. Shaping. (With
  a video, *What's shaping looks like*, now lost.)
- **Hall of glyphs** — Some explanations about Unicode and what infos are
  displayed in glyphs tab.

*Fontmatrix 0.6.0 came with a new manual inside the application. The current
handbook ships with Fontmatrix.*
