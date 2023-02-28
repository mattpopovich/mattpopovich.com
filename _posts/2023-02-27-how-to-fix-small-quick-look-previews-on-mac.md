---
title: "How to Fix Small Quick Look Previews on Mac"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entriesdate: 2023-02-27 01:12:28 -0700
categories: [Blog, YouTube]    # <=2 values here: top category and sub category
tags: [apple, big sur, mac, monterey, osx, preview, quick look, tech, tutorial, drone]     # TAG names should always be lowercase
layout: post                # post is the default, we will set it to be explicit
pin: false
toc: true                   # Table of contents
comments: true              # Enable/disable comments at the bottom of the post
math: false                 # Disabled by default for performance reasons
mermaid: false              # Diagram generation tool via ```mermaid [...]```
#img_cdn: https://cdn.com
#img_path: /img/path/
#image:
#  path: /path/to/image.jpg
#  width: 100   # in pixels
#  height: 40   # in pixels
#  alt: image alternative text
---

<!-- TODO
{% include embed/youtube.html id='TODO' %}
-->

# Intro
[Quick Look](https://support.apple.com/guide/mac-help/preview-a-file-mh14119/mac) is a simple feature on macOS that lets users view certain file types without opening any applications. In my opinion, it is one of Mac's best features. To use it, just [select one or more items](https://support.apple.com/guide/mac-help/aside/glos3b057c3a/13.0/mac/13.0) in Finder, then press the space bar. It is especially handy for viewing images and videos.

However, occasionally, Quick Look doesn't show a full screen preview of the selected file. Sometimes it will only show a small sized window with a small preview along with some file information. The fix for this is very simple and I will detail it below.

# [TL;DR](https://www.merriam-webster.com/dictionary/TL%3BDR)
1. Try to open Quick Look on a file/image/video: select one or more items, then press the space bar
   * If you get a large preview of your file, you're good to go! If not, continue
2. Click on the Apple logo on the top left of your menu bar, select "Force Quit"
   * Or press Option+Command+Escape
3. Select Finder in the window that pops up, then click "Relaunch"
4. Now when pressing space bar to preview files, you should see a large preview window
   * If not, comment below and I'll try to help you!

# Fixing Quick Look
All right everyone, a really quick post for you here today. I was out shooting some footy with the drone and wanted to come back and take a look at it. Upon pressing space bar to preview some of these images and videos (which brings up Quick Look), it wasn't showing a full screen image and the videos weren't loading either... I've had this problem recently on older versions of macOS and I was hoping they fixed it, but it looks like they have not. This is running OS Monterey 12.6.2:

![Quick Look giving small windows / previews](/assets/img/posts/2023-02-27-how-to-fix-small-quick-look-previews-on-mac/QuickLook_not-fully-working.png){: width="480"} *Quick Look not properly working with a small window/preview*

Fortunately, it's a really quick fix to get Quick Look fully working again. All you have to do is click on the Apple logo in the top left, and then go to "Force Quit" (or press Option+Command+Escape), select "Finder", then click "Relaunch".

![Window to Relaunch Finder](/assets/img/posts/2023-02-27-how-to-fix-small-quick-look-previews-on-mac/ForceQuit_Finder.png) *Window to Relaunch Finder*

When relaunching, it will take down all your Finder windows then bring them back up to where they were. Hopefully, if you press space bar, now you should get a full screen image!

![Quick Look giving a full preview](/assets/img/posts/2023-02-27-how-to-fix-small-quick-look-previews-on-mac/QuickLook_fully-working.png) *A properly working Quick Look!*

# Outro
Hopefully Apple can fix this in a future software release, but if not, that is the "quick fix" that we're going to have to deal with.

Thanks for watching, I hope this helped. Let me know if it did or did not in the comments and I'll catch you guys in the next post!


<!-- Could not find audio for Brandon Kai - MDNT (Instrumental)>

<div style="text-align:center">
<iframe style="border-radius:12px"
src="https://open.spotify.com/embed/track/1ngygj9MIxtLvDFJxZj0vE?utm_source=generator&theme=0"
width="100%" height="352" frameBorder="0"
allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
</div>{: .dark }

<div style="text-align:center">
<iframe style="border-radius:12px"
src="https://open.spotify.com/embed/track/1ngygj9MIxtLvDFJxZj0vE?utm_source=generator"
width="100%" height="352" frameBorder="0"
allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
</div>{: .light }

-->


<!-- Video transcript
All right everyone, a really quick video for you here today. I was out shooting some footy with the drone and wanted to come back and take a look at it but upon pressing space bar to preview some of these images and videos (which brings up Preview), it wasn't showing a full screen image and the videos weren't loading either. I've had this problem recently on older versions of macOS and I was hoping they fixed it, but it looks like they have not. This is running OS Monterey 12.6.2 and it's not just this memory card that I have plugged in that it doesn't work for, anything on my desktop as well. But it's a really quick fix to get this working. All you've gotta do is click on the Apple logo in the top left, and then go to "Force Quit", and we are going to quit "Finder"... That is not the right Finder logo... All right, there it is. Ok, well, all you have to do is relaunch Finder and it will take down all your Finder windows, and it will then bring them back up to where they were and if you press space bar, now you get a full screen image, which is what we were hoping to see! So, hopefully Apple can fix this in a future software release, but if not, until then, that is the "quick fix" that we're going to have to deal with. So, thanks for watching, hope this helped. Let me know if it did or did not in the comments and I'll catch you guys in the next video!
-->
