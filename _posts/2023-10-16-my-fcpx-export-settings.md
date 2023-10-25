---
title: "My FCPX Export Settings"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2023-10-15 22:12:19 -0600
categories: [Blog, TODO]    # <=2 values here: top category and sub category
tags: [apple, how to, mac, video editing, tech, tutorial, final cut pro, fcpx]  # TAG names should always be lowercase
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

## Intro
This weekend's project was to finally take some of the timelapses that I took with my [GoPro HERO 8](https://amzn.to/3ZUuXcD) and convert them from images to a video. I do this (and all of my video editing) with [Final Cut Pro (FCP/FCPX)](https://www.apple.com/final-cut-pro/). The way that I usually export my projects was giving me some very bad compression artifacts / banding... so I researched a better solution and will explain that to you in this post!

## [TL;DR](https://www.merriam-webster.com/dictionary/TL%3BDR)

## How I Used to Export My Projects

> Note that when I export FCPX projects, my goal is:
> 1. Very high quality videos (as close to the input material as possible) with
> 2. The smallest file size (while maintaining very high quality videos)
>
> This will create my ["master file"](https://www.izzyvideo.com/master-video-file/#:~:text=The%20master%20video%20file%20is,of%20your%20final%20edited%20video.)
{: .prompt-info }

I used to export my projects by clicking on the share icon in the top right (or File --> Share) --> Export file:
![FCPX share button](/assets/img/posts/2023-10-16-my-fcpx-export-settings/FCPX_share_button.png) *FCPX Share Button*

I then went to the "Settings" tab and set Format to *Mastering*: Video and Audio, Codec to H.264.
![FCPX share button](/assets/img/posts/2023-10-16-my-fcpx-export-settings/FCPX_export_file_settings.png) *FCPX Export File Window*

This seemed like a good option to me. We were exporting a "master" copy and file sizes were large (which implied good quality: 600MB for 30s?? Sheesh!).

The only thing I didn't like about this was that there was no *Video Codec* option for H.265/HEVC. If you were unaware, H.265 is a newer codec than H.264 and [is ~50% more efficient than H.264](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding#Coding_efficiency). Thus, our exported file sizes are ~twice as big as they need to be!

![FCPX share button](/assets/img/posts/2023-10-16-my-fcpx-export-settings/FCPX_export_file_video_codecs.png) *FCPX Export File Video Codec Options*

However, since [YouTube recommends uploading files in H.264](https://support.google.com/youtube/answer/1722171?hl=en), and most of my FPCX videos were being uploaded to YouTube, I was content with H.264. Note that YouTube does support [many more file versions](https://support.google.com/youtube/troubleshooter/2888402?hl=en&ref_topic=2888648#ts=2888407) than just H.264 in `.MP4`.

## Exported Compression Artifacts







[exercise for the reader](http://www.mathmatique.com/articles/left-exercise-reader) 😉

Starting with the iPhone 12, video is shot in 10-bit HDR.

