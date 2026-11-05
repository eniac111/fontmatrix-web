---
title: Fontmatrix 1.0.1
date: 2026-11-05
description: An AppImage, a Flatpak that no longer wants your home folder, icons that can be seen on dark themes, and the current release on Flathub and in Debian.
---

Fontmatrix 1.0.1 is a packaging release. It adds an AppImage, tightens the
Flatpak sandbox, and fixes icons that could not be seen on dark themes.
[Download it](/download/).

## Where to get it

**Flathub carries the current release again.** Flathub had been stuck for six
years on 0.9.100, the release from September 2020. It is now updated to 1.0.1,
so `flatpak install flathub com.github.fontmatrix.Fontmatrix` gives you the same
version as the release page.

**Debian has it as well.** Fontmatrix 1.0.1 is packaged in Debian unstable (sid)
and testing (forky) as `1.0.1+ds-2`, for amd64, arm64, armhf and i386. The
[Debian package page](https://packages.debian.org/search?keywords=fontmatrix&searchon=names&suite=all&section=all)
lists every suite.

**Ubuntu lags behind.** Ubuntu 26.10 (stonking) ships
[0.11.0](https://packages.ubuntu.com/stonking/fontmatrix), from before the 1.0
series. It has several issues that later releases fixed, and none of the 1.0
work: no variable fonts, no colour fonts, no right-to-left text and none of the
reworked font activation. Ubuntu 26.04 LTS (resolute) has no Fontmatrix package
at all, and the two LTS releases before it, 24.04 and 22.04, are still on
0.9.100. The upcoming Ubuntu 27.04 (tenacious) has 1.0.1. Until it arrives, take
the Flatpak from Flathub or the AppImage from the
[release page](https://github.com/fontmatrix/fontmatrix/releases/latest) instead
of the version in the archive.

## New

- **An AppImage for Linux.** One file that runs on any distribution with glibc
  2.34 or newer, built with KDE Craft the same way KDE builds its own AppImages.
  Every tagged release includes one from now on. It uses your system's
  fontconfig, so a current `/etc/fonts` no longer produces a warning for every
  file. It has no *Activate for all users* option, because an AppImage cannot
  install the polkit helper that option needs.

## Flatpak

- **No access to your home folder.** Files are opened and saved through the
  desktop's file chooser. The only two places Fontmatrix can reach on its own
  are `~/.local/share/fonts`, to activate fonts, and `~/.config/fontconfig`, to
  hide system fonts.
- The runtime is **KDE 6.11**.
- The `--own-name` permission is gone. The single-instance D-Bus service now
  registers under the application ID, `com.github.fontmatrix.Fontmatrix`.
- CI checks the manifest and the built repository with `flatpak-builder-lint`.

## Fixes

- **Icons on dark themes.** Outside Plasma (in the AppImage, on other desktops,
  on Windows and on macOS), icon themes such as Breeze or Gruvbox drew their
  icons dark on a dark background. Fontmatrix now recolours them to match your
  colour scheme, and uses your chosen widget style, as Plasma does.
- **Colour schemes on KDE desktops without Plasma's Qt integration.** Your
  colours from `kdeglobals` are kept instead of being switched to Breeze Dark.

## For packagers

There is one new required dependency: KF6 IconThemes (`KF6::IconThemes`).

The [full release notes](https://github.com/fontmatrix/fontmatrix/releases/tag/v1.0.1)
list every change.
