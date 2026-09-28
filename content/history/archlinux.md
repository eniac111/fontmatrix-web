---
title: "Note for ArchLinux"
date: 2008-02-01
kind: news
original: http://fontmatrix.be/?q=node/23
---

Foxbunny (?) reported some issues in building Fontmatrix for ArchLinux. He
finally wrote these "PKGBUILD", hope it will work for you & thanks to him.

```
# 32-bit
# Contributor: Michal Malek, michalm at jabster pl>

pkgname=fontmatrix
pkgver=0.3.1
pkgrel=1
pkgdesc="Font manager for Linux"
arch=('i686' 'x86_64')
url="http://fontmatrix.net/"
license=('GPL')
depends=('qt>=4.3.0' 'freetype2')
makedepends=('cmake>=2.4.0')
source=(http://fontmatrix.net/archives/$pkgname-$pkgver-Source.tar.gz)
md5sums=('173b3354e0e3d03a60e3c1fd1d790b37')

build()
{
        cd $startdir/src/$pkgname-$pkgver-Source
        export QTDIR=/usr
        export QMAKESPEC=/usr/share/qt/mkspecs/linux-g++-32
        mkdir build
        cd build
        cmake .. -DCMAKE_INSTALL_PREFIX:PATH=/usr
        make || return 1
        make DESTDIR=$startdir/pkg install
}
```

For 64-bit, the same, with `QMAKESPEC=/usr/share/qt/mkspecs/linux-g++-64`.
