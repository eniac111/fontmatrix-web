---
title: "system fonts"
date: 2008-12-20
kind: news
original: http://fontmatrix.be/node/41
---

First of all, it worth noticing a couple of things about Fontmatrix under
Linux. Fontmatrix relies on Fontconfig for font management. If you use an
application which is not fc-aware (e.g. TeX), Fontmatrix can't do anything for
you. To be precise, Fontmatrix uses the fact that Fontconfig provides a user
level configuration. What it does exactly is to symlink fonts which you want to
activate into a directory, itself being declared in the user configuration file
(~/.fonts.conf). Deactivating fonts is thus just a matter of unlinking these
files from the specific directory.

To be honest, it's just what I used to do manually before I wrote Fontmatrix!
Here appear two important things, one unrelated to this article — there's no
way, yet, for programs to know that a font has been de/activated, hope we'll
later agree on a DBUS channel to carry this information — , the other being
that all what's configured by Fontconfig at a higher level can't be (easily)
handled by Fontmatrix. Namely "deactivation of system fonts". While I still
think it's a bad idea to play with fonts which have been installed by the
administrator because some fonts eventually come as required packages for
other programs, the features has been requested so many times… There's now
experimental code to achieve just that.

Perhaps Fontconfig gurus will feel sick reading what's follow, but as long as
I'm not exactly sure it works everywhere I'd like to explain how I did it so
you'll know where to look if it does not work for you. For each "system font"
(means a font which has been registered in Fontconfig database at a higher
level) that Fontmatrix deactivates, it write a selectfont/rejectfont rule (not
sure it's the right word though) in your ~/.fonts.conf file. example:

```xml
<selectfont>
    <rejectfont>
        <glob>/usr/lib/jvm/java-1.6.0.u7-sun-1.6.0.u7/jre/lib/fonts/LucidaBrightDemiBold.ttf</glob>
        <glob>/usr/lib/jvm/java-1.6.0.u7-sun-1.6.0.u7/jre/lib/fonts/LucidaBrightDemiItalic.ttf</glob>
        <glob>/usr/lib/jvm/java-1.6.0.u7-sun-1.6.0.u7/jre/lib/fonts/LucidaBrightItalic.ttf</glob>
        <glob>/usr/lib/jvm/java-1.6.0.u7-sun-1.6.0.u7/jre/lib/fonts/LucidaBrightRegular.ttf</glob>
    </rejectfont>
</selectfont>
```

What worries me is what follows, from Fontconfig user manual about glob
element: "Note that globs only apply to directories, not to individual fonts."
What I understand is that the rules above, since they are related to
individual fonts, should not work properly, but it does fine here. So, if I
misunderstood, you're lucky and it will work for you! If not, there's a chance
they'll fix it to make the code do what the doc says, some day. Activation 100%
works at least ;-)

*Fontmatrix 1.0 still hides system fonts with rejectfont rules, but in a file
of its own, `~/.config/fontconfig/conf.d/60-fontmatrix-rejects.conf`, instead
of your fonts.conf.*
