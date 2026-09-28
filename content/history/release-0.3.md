---
title: "Fontmatrix 0.3"
date: 2008-02-01
kind: news
original: http://www.fontmatrix.net/?q=node/25
undated: true
---

If your lucky, your distro has an up to date package. Otherwise, just take the
more recent source package [here](https://web.archive.org/web/2011/http://fontmatrix.net/archives/).

The main idea is "0.3.0 is far better than 0.2.0", here are some points to
support this idea.

## We've invited Harfbuzz to the party

Harfbuzz is a library to discover and use advance OpenType features and its aim
is to enable better support for non-Latin languages. At the moment, only the
basic transformations are working. Moreover, non-latin languages handling is
not yet functionnal. For now, you can see and preview features present in
OpenType GPOS and GSUB tables. If you just arrived from Mars, it means giving
access to ligatures, optical small caps, old style figures and generally what's
called "fine typography" - even if it will be you cannot enjoy it in all
applications currently.

Why Harfbuzz? It's yet part of Pango and Qt and aimed to be the standard FLOSS
text layout component. Moreover, Scribus team wants it for its non-latin
rendering engine and Fontmatrix is definitly the Scribus' user font manager :)
But supporting other layout engines such as ICU or M17 wont be forgotten, just
a matter of spare time.

## Freetype Rendering

As expected and experienced by early users of Fontmatrix, rendering glyphs at
small size without a specific engine just results in ugliness. Little by
little, we tend to use Freetype (we have to repeat here how this piece of
software is excellent, thanks for it) more and more.

## Systray

Some might think it's kind of gadget, but beyond its own and obvious utility,
systray icon stands for "Hey, I don't eat 500Mb of memory anymore, leave me
alone!"

## Multiple Text Samples

Among a lot of UI improvements, the ability to maintain a set of samples is
what I'd like to emphasize. It saved me a lot of time, I hope it will be the
same for you.

## Changelog [0.3.1]

- Fixed zoom slider in sample text preview
- Fixed order of libs to link into fontmatrix (harfbuzz _before_ Qt)
- Fixed slowdown at starting time (report it to first search, maybe good to
  put it in subprocess when full UI is available).
- Fixed bug #10830: Wrong dialog position
- Fixed bug #10829: Font list starts at letter C
