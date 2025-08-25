---
title: "How to Install the Resynthesizer Plugin for GIMP on Macs with Apple Silicon (2024)"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2025-03-11 21:36:06 -0600
categories: [Blog, YouTube]    # <=2 values here: top category and sub category
tags: [youtube, linux, ubuntu, GIMP, resynthesizer, tech, tutorial, how to, apple, mac os, update, arm, apple silicon]                # TAG names should always be lowercase
layout: post                # post is the default, we will set it to be explicit
pin: false
toc: true                   # Table of contents
comments: true              # Enable/disable comments at the bottom of the post
math: false                 # Disabled by default for performance reasons
mermaid: false              # Diagram generation tool via ```mermaid [...]```
#img_cdn: https://cdn.com
#media_subpath: /img/path/
image:
  path: /assets/img/posts/2025-03-11-how-to-install-the-resynthesizer-plugin-for-gimp-on-macs-with-apple-silicon-2024/thumbnail_fix_resynthesizer_2024.jpg
#   width: 100   # in pixels
#   height: 40   # in pixels
  alt: GIMP error whenever the resynthesizer plugin is not installed/configured correctly
  show_image_in_post: false
description: Make the resynthesizer plugin work with the latest GIMP 2.x!  # A short sentence to describe the article, used when sharing links on social media and on homepage
---

{% include embed/youtube.html id='tO5EQdpugw4' %}

> This post is only for Macs with Apple Silicon (M1, M2, etc.) processors. If you're unsure which processor you have, follow [this](https://support.apple.com/en-us/116943) support page.
{: .prompt-warning }

> This post is currently only valid for GIMP 2.x. The instructions on this page **will not work with GIMP 3.x**. I will make a new post once I find a solution for GIMP 3.x.
{: .prompt-danger }

## Intro
Welp, back at it again with *another* GIMP and resynthesizer update. Per usual, this update is long overdue. But, I think this is the easiest installation yet and I did a good bit of tweaking to make this install as easy as possible. All you need to do is copy a few files over, and you should be good to go.

Additionally, I have this post titled 2024 (even though I'm publishing it in 2025) because the most recent version of GIMP for Mac (2.10.38 revision 1) [was published on May 22, 2024](https://download.gimp.org/gimp/v2.10/osx/?C=M&O=D). GIMP is currently working on releasing GIMP 3.0, and it [seems like they're very close to releasing it](https://www.gimp.org/news/2025/02/10/gimp-3-0-RC3-released/). The resynthesizer files that I created only work with GIMP 2.x so I will definitely need to modify the resynthesizer files for GIMP 3.x. I'm saving the 2025 post for GIMP 3.x.

### Backstory
A little bit of backstory, I originally had trouble installing the resynthesizer plugin back in 2021. Once I managed to install it, I made a post and video about how I did it. There was a good bit of interest from the community! I then had someone reach out to me and point out an easier way to complete the installation, so I made an update video in 2022. Again, with a decent amount of interest. However, a few months later, GIMP [released an updated build for Apple Silicon (ARM) processors](https://www.gimp.org/news/2022/12/02/gimp-2.10.32-apple-silicon/), which broke my installation steps. My installation still worked as long as you used an older version of GIMP, but now I've found a way to make things work with the newest version of GIMP. Let's jump into it.

## [TL;DR](https://www.merriam-webster.com/dictionary/TL%3BDR)
1. Download and install GIMP 2.10.x from [here](https://download.gimp.org/gimp/v2.10/macos/?C=M&O=D).
  * Recommended to use the latest 2.10.38 version: [gimp-2.10.38-arm64-1.dmg](https://download.gimp.org/gimp/v2.10/osx/gimp-2.10.38-arm64-1.dmg)
1. Download and unzip [`resynthesizer-mac-arm-v2.10.38-revision1.zip`](https://github.com/mattpopovich/GIMP-Resynthesizer-for-Mac-on-ARM/releases/download/v2.10.38-revision1/resynthesizer-mac-arm-v2.10.38-revision1.zip)
1. Copy all the files to `/Applications/GIMP.app/Contents/Resources/lib/gimp/2.0/plug-ins`.
1. Restart GIMP and use the plugin (*Filters* --> *Enhance* --> *Heal selection...*)!

## Removing Old Versions of GIMP
Uninstalling GIMP is as easy as dragging the GIMP application from the `/Applications` folder to the trash.

If you'd like to remove all GIMP user settings and other preferences (not necessary), look into [AppCleaner](https://freemacsoft.net/appcleaner/) to help you find these files.

## Installing Newest Version of GIMP
Download the latest version of GIMP 2.x: [gimp-2.10.38-arm64-1.dmg](https://download.gimp.org/gimp/v2.10/osx/gimp-2.10.38-arm64-1.dmg). Other GIMP 2.x versions can be found [here](https://www.gimp.org/downloads/). Double click the `.dmg` installer, then click and drag GIMP to the `/Applications` folder to complete the installation.

I have tested the below resynthesizer installation with GIMP 2.10.38 (revision 1), so if you are having issues on a different GIMP version, try  2.10.38 (revision 1), linked in the paragraph above.

## Installing the Resynthesizer Plugin
### Installing Resynthesizer with Pre-Built Libraries (easiest)
I've made a repository on GitHub to hold the resynthesizer files that I modified: [GIMP-Resynthesizer-for-Mac-on-ARM](https://github.com/mattpopovich/GIMP-Resynthesizer-for-Mac-on-ARM). You can go to the [releases page](https://github.com/mattpopovich/GIMP-Resynthesizer-for-Mac-on-ARM/releases) to see which versions of GIMP I've made releases for.

For GIMP 2.10.38 (revision 1), download and unzip [`resynthesizer-mac-arm-v2.10.38-revision1.zip`](https://github.com/mattpopovich/GIMP-Resynthesizer-for-Mac-on-ARM/releases/download/v2.10.38-revision1/resynthesizer-mac-arm-v2.10.38-revision1.zip)

Copy all the files from the unzipped folder:
- `resynthesizerLibraries` folder
- All the python files (`*.py`)
- `resynthesizer`
- `resynthesizer_gui`

To `/Applications/GIMP.app/Contents/Resources/lib/gimp/2.0/plug-ins`.

Relaunch GIMP and you should see the plugin under *Filters* --> *Enhance* --> *Heal selection...* 🥳

### Installing Resynthesizer via MacPorts (more difficult)
You can also install the resynthesizer plugin via MacPorts (`sudo port install gimp-resynthesizer`) if you would like to build from source. It will take a little bit longer + could be more difficult (to build) and require some more hard drive space (libraries) but this is a perfectly valid solution as well. See the markdown page on my GitHub repo: [BuildingResynthesizerViaMacPorts.md](https://github.com/mattpopovich/GIMP-Resynthesizer-for-Mac-on-ARM/blob/main/BuildingResynthesizerViaMacPorts.md) for more information on the difficulties I had and their solutions.

### How I Modified The Resynthesizer Files
See the markdown page on my GitHub repo: [RepoCreation.md](https://github.com/mattpopovich/GIMP-Resynthesizer-for-Mac-on-ARM/blob/main/RepoCreation.md) for more detail on how the resynthesizer files were built and how they needed to be modified for an easier installation.

## Alternative to the Resynthesizer Plugin
As I mentioned in my previous resynthesizer posts, you can manually recreate what the resynthesizer plugin does with the "heal" and "clone" tools. I'm not going to do a full writeup about it here, but I did go into a quick example in my past [YouTube video](https://youtu.be/MHwtKg0tws8?t=802). I'm sure you could find some similar or even better tutorials on those tools online.

Additionally, I think it's safe to say that you have a Mac (as this tutorial is only applicable to Macs). [All Apple Silicon Macs](https://support.apple.com/guide/photos/remove-distractions-and-imperfections-pht5c38b77c5/mac) have a "clean up" functionality in the Photos app which will basically do the same thing as the resynthesizer plugin, and sometimes it will even do a better job. [This functionality](https://support.apple.com/guide/iphone/use-apple-intelligence-in-photos-iphf7de217f0/18.0/ios/18.0#iph4e1fc17b5) is also available to newer iPhones in certain regions ([requirements here](https://support.apple.com/en-us/121429)). Utilizing the Photo app to perform "resynthesizer" (clean up) functionality would allow you to install GIMP 3.0 while still having resynthesizer capability (albeit in a different app).

Google has a "[Magic Eraser](https://www.google.com/intl/en_us/photos/editing/)" feature for anyone that subscribes to Google One or has a Google Pixel. Samsung has an "[Object eraser](https://www.samsung.com/uk/support/mobile-devices/how-to-remove-unwanted-objects-from-photos-on-your-galaxy-phone/)".

If you can't get the resynthesizer plugin working, these are some great backup options.

## Outro
Thanks for reading! I hope this is able to help get your resynthesizer plugin up and running again. If so, the best way to say thanks is by [liking the YouTube video](https://youtu.be/tO5EQdpugw4), [subscribing to my YouTube channel](https://www.youtube.com/@MattPopovich?sub_confirmation=1), and/or [following my socials](/about). If I have updates or fixes to future GIMP / resynthesizer things, that is where I will post updates.

If your plugin still isn't working after this, leave a comment below or send a message in [my Discord server](https://discord.gg/HsDW3X2Xba) and I'll do my best to help you out!


&nbsp;

<div style="text-align:center">
<iframe
style="border-radius:12px"
src="https://open.spotify.com/embed/track/6tAnz61l4q03zP7Qi50eiJ?si=faa1810ccc574ed2?utm_source=generator"
width="80%" height="352" frameBorder="0"
allowfullscreen=""
allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
loading="lazy">
</iframe>
</div>
