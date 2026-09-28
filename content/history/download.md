---
title: "Download"
date: 2008-02-01
kind: page
original: http://fontmatrix.be/node/22
weight: 40
description: "Source releases, Linux packages and Subversion, 2008–2011."
---

We provide source packages of Fontmatrix as public releases which you can
download [here](https://web.archive.org/web/2011/http://fontmatrix.net/archives/).

Fontmatrix is highly available on Linux, check [here](#linux) for your distro.

From time to time, someone takes time to build it on Windows or MacOSX and we
host these packages [here](https://web.archive.org/web/2011/http://fontmatrix.net/archives/win/) (Windows) and
[here](https://web.archive.org/web/2011/http://fontmatrix.net/archives/mac/) (Mac).

Finally, we are please to offer a direct access to our versionning system where
you can grab latest code:

```
svn co http://svn.gna.org/svn/undertype/trunk/tools/typotek fontmatrix
```

For ArchLinux users, here is special [note](../archlinux/). [maybe obsolete]

For Debian and Ubuntu users, there are installation
[instructions](https://web.archive.org/web/2011/http://svn.gna.org/svn/undertype/trunk/tools/typotek/debian-ubuntu-install.txt).

## Linux download {#linux}

*23 May 2009*

Some RPMs are available from
[mrdocs' repository](http://download.opensuse.org/repositories/home:/mrdocs) at
OBS (OpenSUSE Build Service). There are packages for: Suse 11.3+ 32 and 64 bit;
Fedora 13+; Mandriva 2010.0 32 and 64 bit. Even though you can install them
"as is", it might be a good idea to add the repository to your package manager
if you run one of the supported distibutions.

Fontmatrix is also available for Fedora users. For Fedora 8 users: Install
Fontmatrix using command

```
yum install --enablerepo=updates fontmatrix
```

For Rawhide/Fedora 9 users: Install Fontmatrix using the command

```
yum install fontmatrix
```

For Debian Sid (unstable), Lenny (testing) and Ubuntu Gutsy users, you can take
a tour at [scribus.net](https://web.archive.org/web/2011/http://www.scribus.net/?q=debian) to read how to take
advantage of Aleksandr Moskalenko's repository to install Fontmatrix. Note that
you can have a look at [Fontmatrix at Debian](https://packages.debian.org/fontmatrix).
