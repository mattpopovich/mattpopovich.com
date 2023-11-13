---
title: "How to Use Adobe DNG Converter from the Command Line"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2023-10-25 05:20:06 -0600
categories: [Blog, TODO]    # <=2 values here: top category and sub category
tags: [apple, how to, mac, video editing, tech, tutorial, adobe]                # TAG names should always be lowercase
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
Expanding on [my previous project](my-fcpx-export-settings) converting image time lapses into videos, the first step of that process is to convert the `.GPR` files that come off of the [GoPro](https://amzn.to/3ZUuXcD) into `.DNG` files that can be used by [Final Cut Pro (FCP/FCPX)](https://www.apple.com/final-cut-pro/). I do this with [Adobe Digital Negative (DNG) Converter](https://helpx.adobe.com/camera-raw/using/adobe-dng-converter.html). It's a [graphical user interface (GUI)](https://www.computerhope.com/jargon/g/gui.htm) program which requires me to use the mouse and select files... it's repetive and I select the same settings every time... I just want something I can double click that will immediately kick off the conversion for me. Turns out, as I suspected, the Adobe DNG Converter is running a command line program underneath the hood. Here's how to use it

## [TL;DR](https://www.merriam-webster.com/dictionary/TL%3BDR)
* `open -a Adobe\ DNG\ Converter.app --args -fl -d /Users/mattpopovich/Desktop/2020-09-10_NightTimelapse/DNG /Users/mattpopovich/Desktop/2020-09-10_NightTimelapse/GPR/*`

## Installation
Go [here](https://helpx.adobe.com/camera-raw/using/adobe-dng-converter.html), download and install the application.

## Using the GUI
Bring up spotlight (command+space) to search for *Adobe DNG Converter.app*, press enter to open it. There are four main steps:
1. Select the images to convert
  - Here I select the folder where I have placed my `.GPR` files
2. Select the location to save converted images
  - Here I select a `DNG` folder that I created
3. Select a name for converted images
  - I normally just change the extension to `.DNG` instead of `.dng` just because the GoPro files are `.GPR` (capitalized).
4. Preferences
  - I normally just leave these at the default:
    - Compatibility: Camera Raw 15.3 and later
    - JPEG Preview: Medium Size
    - Embed fast load data
    - Don't use lossy compression
    - Preserve Pixel Count
    - Don't embed original

Click "Convert" and let the program go to work

## Command Line Interface (CLI) Documentation
The CLI for Adobe DNG Converter has about 0 documentation that I've been able to find. [This .pdf](https://helpx.adobe.com/content/dam/help/en/photoshop/pdf/dng_commandline.pdf) is about it.

# Using the Command Line Interface (CLI)
Apparently on a Mac, we can use the `open` command to execute a `.app`:

```console
$ man open | cat
OPEN(1)                     General Commands Manual                    OPEN(1)

NAME
     open – open files and directories

[...]

DESCRIPTION
     The open command opens a file (or a directory or URL), just as if you had
     double-clicked the file's icon. If no application name is specified, the
     default application as determined via LaunchServices is used to open the
     specified files.

     If the file is in the form of a URL, the file will be opened as a URL.

     You can specify one or more file names (or pathnames), which are
     interpreted relative to the shell or Terminal window's current working
     directory. For example, the following command would open all Word files
     in the current working directory:

     open *.doc

     Opened applications inherit environment variables just as if you had
     launched the application directly through its full path.  This behavior
     was also present in Tiger.

     The options are as follows:

     -a application
         Specifies the application to use for opening the file

[...]

```

