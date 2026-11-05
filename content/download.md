---
title: Download
description: Get Fontmatrix for Linux or Windows, or build it from source.
---

The current release is **Fontmatrix 1.0.1**. All files are on the
[release page on GitHub](https://github.com/fontmatrix/fontmatrix/releases/latest).

<aside class="warning"><p>Download Fontmatrix only from GitHub, Flathub or your
distribution. The domain fontmatrix.net belongs to scammers, not to the project;
do not run anything you get from it.</p></aside>

## Linux

**Flathub** is the recommended way to install Fontmatrix. It carries the current
release, and it updates along with the rest of your Flatpaks:

```
flatpak install flathub com.github.fontmatrix.Fontmatrix
```

Or install it from the [Flathub page](https://flathub.org/apps/com.github.fontmatrix.Fontmatrix)
in your software centre.

Fontmatrix is sandboxed there: it opens and saves files through your desktop's
file chooser, and the only two places it reaches on its own are
`~/.local/share/fonts`, to activate fonts, and `~/.config/fontconfig`, to hide
system fonts.

**AppImage.** If you would rather not use Flatpak, download
`fontmatrix-1.0.1-linux-gcc-x86_64.AppImage` from the
[release page](https://github.com/fontmatrix/fontmatrix/releases/latest), make
it executable and run it:

```
chmod +x fontmatrix-1.0.1-linux-gcc-x86_64.AppImage
./fontmatrix-1.0.1-linux-gcc-x86_64.AppImage
```

It runs on any distribution with glibc 2.34 or newer. It has no *Activate for
all users* option, because an AppImage cannot install the polkit helper that
option needs.

**Flatpak bundle.** To install the same Flatpak without Flathub, download
`fontmatrix-1.0.1.flatpak` from the
[release page](https://github.com/fontmatrix/fontmatrix/releases/latest) and
install it with:

```
flatpak install --user fontmatrix-1.0.1.flatpak
```

It needs the KDE runtime from Flathub, which `flatpak` offers to install.

**Distributions.** Debian unstable (sid) and testing (forky) carry 1.0.1 as
`fontmatrix`; see the
[Debian package page](https://packages.debian.org/search?keywords=fontmatrix&searchon=names&suite=all&section=all).
Ubuntu 26.10 still has [0.11.0](https://packages.ubuntu.com/stonking/fontmatrix),
which predates the 1.0 series and has several issues fixed since, and 26.04 LTS
has no package at all; on Ubuntu, use Flathub or the AppImage until 27.04 arrives
with 1.0.1. Other distributions package Fontmatrix too; their version may be
older.

## Windows

Download `fontmatrix-1.0.1-windows-cl-msvc2022-x86_64.exe` (installer) or the
`.7z` archive (no installation) from the
[release page](https://github.com/fontmatrix/fontmatrix/releases/latest).
Each file has a `.sha256` checksum next to it.

## macOS

Fontmatrix is not built for macOS at present. The code still has the macOS
parts, and contributors who want to bring it back are welcome.

## From source

Fontmatrix needs Qt 6.8 or newer, KDE Frameworks 6.12 or newer, FreeType,
HarfBuzz, zlib and libhyphen. PoDoFo (PDF font extraction) and Fontconfig are
optional.

```
git clone https://github.com/fontmatrix/fontmatrix.git
cd fontmatrix
cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
ninja -C build
sudo ninja -C build install
```

See [INSTALL.md](https://github.com/fontmatrix/fontmatrix/blob/master/INSTALL.md)
for the details.
