---
title: "Some things deserve documentation"
date: 2009-05-19
kind: news
original: http://fontmatrix.be/node/47
---

Sadly, I haven't no time nor skill to write so much useful thing as
documentation.

On the other hand, if most of the features are not obvious, at least they're
exposed in the user interface, thus "accessible" for the curious.
Unfortunately, there is an area which is not at all exposed in the UI, the
scripter. I won't start document it right now! I just wanted to let you know
the very first key (hm, 2 firsts!) of the Fontmatrix Python scripter.

```
print dir(Fontmatrix)
=>['DB', 'Debug', 'children', 'className', 'connect', 'currentFontFamily', 'currentFontNames', 'currentFontPath', 'currentFontStyle', 'currentFonts', 'deleteLater', 'disconnect', 'help', 'nextFace', 'nextFamily', 'objectName', 'parent', 'previousFace', 'previousFamily', 'quit', 'setParent', 'start', 'terminate', 'updateTree']

print dir(Fontmatrix.DB())
=>['AllFontNames', 'AllFonts', 'Font', 'FontCount', 'Fonts', 'Remove', 'addTag', 'addTagToDB', 'children', 'className', 'connect', 'deleteLater', 'disconnect', 'editTag', 'getTags', 'help', 'insertTemporaryFont', 'objectName', 'parent', 'removeTag', 'removeTagFromDB', 'setParent', 'setTags']
```

On the contrary, what is documented (in INSTALL file) is the way of enabling
scripter at compile time.

HTH

We included 3 scripts in the repository, which are installed as part as the
default target, so you can try them right in Fontmatrix (Scripts > Script
Console… > Load).

…or not! Someone actually did read the code and came with a short, but still
super-useful, Python script to import his old database. It's
[here](https://web.archive.org/web/2011/http://thomas-sibley.com/etc/tag-from-xml) and soon in our
repository, let me say it rocks!

*The Python scripter was removed in Fontmatrix 1.0.*
