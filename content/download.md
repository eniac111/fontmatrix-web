---
title: Download
description: Get Fontmatrix for Linux or Windows, or build it from source.
---

The current release is **Fontmatrix 1.0.0**. All files are on the
[release page on GitHub](https://github.com/eniac111/fontmatrix/releases/latest).

## Linux

**Flatpak bundle.** Download `fontmatrix-1.0.0.flatpak` from the
[release page](https://github.com/eniac111/fontmatrix/releases/latest) and
install it with:

```
flatpak install --user fontmatrix-1.0.0.flatpak
```

It needs the KDE runtime from Flathub, which `flatpak` offers to install.

**Flathub.** Fontmatrix is
[on Flathub](https://flathub.org/apps/details/com.github.fontmatrix.Fontmatrix)
too, but Flathub still ships the older 0.9.100 release for now.

**Distributions.** Some distributions package Fontmatrix; their version may be older.

## Windows

Download `fontmatrix-1.0.0-windows-cl-msvc2022-x86_64.exe` (installer) or the
`.7z` archive (no installation) from the
[release page](https://github.com/eniac111/fontmatrix/releases/latest).
Each file has a `.sha256` checksum next to it.

## macOS

Fontmatrix is not built for macOS at present. The code still has the macOS
parts, and contributors who want to bring it back are welcome.

## From source

Fontmatrix needs Qt 6.8 or newer, KDE Frameworks 6.12 or newer, FreeType,
HarfBuzz, zlib and libhyphen. PoDoFo (PDF font extraction) and Fontconfig are
optional.

```
git clone https://github.com/eniac111/fontmatrix.git
cd fontmatrix
cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
ninja -C build
sudo ninja -C build install
```

See [INSTALL.md](https://github.com/eniac111/fontmatrix/blob/master/INSTALL.md)
for the details.
