---
title: "How to Eject Stubborn External Hard Drives on MacOS"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2026-03-17 21:52:18 -0600
categories: [Blog, TODO]    # <=2 values here: top category and sub category
tags: [todo]                # TAG names should always be lowercase
layout: post                # post is the default, we will set it to be explicit
pin: false
toc: true                   # Table of contents
comments: true              # Enable/disable comments at the bottom of the post
math: false                 # Disabled by default for performance reasons
mermaid: false              # Diagram generation tool via ```mermaid [...]```
#img_cdn: https://cdn.com
#media_subpath: /img/path/
#image:
#   path: /path/to/image.jpg
#   width: 1200   # in pixels
#   height: 630   # in pixels, 1.90:1 desired by chirpy
#   alt: image alternative text
#   show_image_in_post: false
#description:               # A short sentence to describe the article, used when sharing links on social media and on homepage
---

## Intro
For whatever reason, sometimes external (USB) hard drives do not want to eject on macOS. You can wait as long as you would like but sometimes they will never be ready to eject. One less than ideal solution to this is to shutdown your computer, but afterwards you would need to reopen all your windows and programs which can be a real pain. Let me tell you about a much better, and easier solution.

## [TL;DR](https://www.merriam-webster.com/dictionary/TL%3BDR)
1. Close any programs that are running which might be accessing a file on your external hard drive
1. Open Teminal
1. Locate your external hard drive
   - Will likely be in `/Volumes`
1. `lsof /Volumes/ExternalHDD`
1. Note the PID of various processes that are keeping files open
1. Kill the process `kill ####`
   - Run this command with care, make sure the process isn't modifying a critical file
   - If `kill` does not end the process, you can try `kill -9 ####` which will forcefully end the process (more dangerous than `kill`)
1. Repeat `lsof /Volumes/ExternalHDD` and `kill ####` until all processes are killed
1. Eject the external hard drive

## Exit any Programs that Might be Accessing Files on your External Hard Drive
The first obvious solution is to make sure you close any applications that might be accessing files on your external hard drive.

## Identifying and Killing Processes that are using Files on the External Hard Drive

### Locate our External Hard Drive
The reason you cannot eject your external hard drive is because some process is using a file on the external hard drive. Ejecting the hard drive while that file is in use could result in the file being corrupted. We need to identify those processes and exit them.

The first step will be to open the `Terminal` application, then locate where our external hard drive is mounted. It will likely be in `/Volumes`:

```terminal
# ls /Volumes
Macintosh HD         ExternalHDD
```

This command lists (`ls`) anything we have mounted in `/Volumes`. If you are unfamiliar with the terminal, check out my [terminal tutorial post](TODO).

As an example, my external hard drive is mounted at `/Volumes/ExternalHDD`.

### Identify Processes that are Using the External Hard Drive
Next, we will run `lsof` which will **l**i**s**t **o**pen **f**iles.

```terminal
# lsof /Volumes/ExternalHDD

TODO

```

Here, we see that PID (**P**rocess **ID**entification number of the process) 28885 is using a couple `.sql` files in my `Photos Library.photoslibrary`. This is a very common occurrence whenever I open the `Photos.app` and point it to a library on my external hard drive. It consistently will access/index a sq-lite (TODO) file even once I close the app.

### Kill the Running Process
Lastly, we will kill the process(es) that are running which will ensure nothing is being accessed on the external hard drive, allowing it to be safely ejected.

> Killing processes that are running can sometimes result in whatever file they are using to be corrupted. Be mindful of the type of file that is being accessed and kill processes with care.
{: .prompt-warning }

```terminal
# kill 28885

TODO
```

We can check to make sure the file was killed by again listing the open files on the external hard drive

```terminal
# lsof /Volumes/ExternalHDD

TODO
```

Typically, the process will be killed. Occasionally, the process will remain running. You can give it a few seconds and try to kill it again. If that doesn't work, we can run `kill -9 ####` which will attempt the kill again but this time with a "non-catchable, non-ignorable kill" signal. You can find more information on the `kill` command by running `man kill`, which will bring up the manual for the `kill` command.

```terminal
# kill -9 28885

TODO

# lsof /Volumes/ExternalHDD

```

Repeat these commands until all the processes accessing the external hard drive have been closed.

## Eject the External Hard Drive
Once there are no remaining processes accessing the external hard drive, you can try to eject it again.

Hopefully, it will eject successfully this time!








&nbsp;

TODO: Add spotify link here (if applicable)
<div style="text-align:center">
<iframe
style="border-radius:12px"
src="https://open.spotify.com/embed/track/5fEThMYHHyoohPxqsCvz1l?utm_source=generator"
width="80%" height="352" frameBorder="0"
allowfullscreen=""
allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
loading="lazy">
</iframe>
</div>
