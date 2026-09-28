---
title: "Fontmatrix 0.6.0"
date: 2009-07-03
kind: news
original: http://fontmatrix.be/node/51
---

We're proud and scared altogether to announce a new public release of
Fontmatrix.

This release is numbered 0.6.0. It replaces the Jurassic old 0.4.2. The 0.5.0
branch has been obsoleted as soon as it was branched almost a year ago. Trunk
is now numbered 0.6.99.

Compared to 0.4.2, almost everything is new. From the storage backend to the
preview engine, all has been reworked to offer a better user experience and
prepare exciting future developments. Here's a non-exhaustive list of changes:

- SQLite database and a Python script to move data from old XML based DB
- Python scripting
- Independent samples directory (allowing easy sharing of this resource)
- Configurable shortcuts
- A text layout engine to display samples (including hyphenation)
- ICU, Harfbuzz and Fontmatrix's own shaper engines
- A playful playground
- PANOSE browser (experimental)
- New help system and user manual written from scratch
- Glyphs comparison panel
- Boolean operators in search filters
- File system browser for fonts
- Themable informations panel (CSS and JavaScript)
- Extract embedded fonts from PDF documents (experimental)
- Find font from an bitmap image (experimental)
- Expose, and possibly export, TrueType tables
- Edit tags
- billions bugs fixed and UI improvements…

You can also read a detailed
[review of the new version](https://web.archive.org/web/2011/http://libregraphicsworld.org/articles.php?article_id=6)
at [Libre Graphics World](https://librearts.org/).

## Download

Main source for this package is the fontmatrix006 branch on Subversion server:

```
svn co http://svn.gna.org/svn/undertype/branches/fontmatrix006
```

You can find source packages in archives on the web server:

[Tarball](https://web.archive.org/web/2011/http://fontmatrix.net/archives/fontmatrix-0.6.0-Source.tar.gz) |
[Md5](https://web.archive.org/web/2011/http://fontmatrix.net/archives/fontmatrix-0.6.0-Source.tar.gz.md5) |
[Signature](https://web.archive.org/web/2011/http://fontmatrix.net/archives/fontmatrix-0.6.0-Source.tar.gz.asc) |
[Key](https://web.archive.org/web/2011/http://fontmatrix.net/archives/pierre_marchand-sc.pubkey) |
[Win32 build](https://web.archive.org/web/2011/http://www.fontmatrix.net/archives/win/fontmatrix-0.6.0-win32.exe)

We don't provide binary packages for Mac OS X yet and we suggest to Linux users
to rely on package repositories for your distributions.

Have fun!
