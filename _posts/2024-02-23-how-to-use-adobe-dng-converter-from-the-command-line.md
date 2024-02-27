---
title: "How to Use Adobe DNG Converter from the Command Line"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2024-02-24 03:17:06 -500
categories: [Blog]    # <=2 values here: top category and sub category
tags: [apple, how to, mac, video editing, tech, tutorial, adobe, dng, gpr, cli, gui, adobe dng converter, programming, bash]                # TAG names should always be lowercase
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

<!-- TODO: Link to "my FCPX export settings blog post. Start this blog with "expanding on my previous project" -->

## Intro
Whenever I shoot a time lapse in raw on my [GoPro (affiliate link)](https://amzn.to/3ZUuXcD), it creates one folder that is full of `*.JPG` and `*.GPR` files. I then find myself moving all the `*.JPG` files into a `JPG` folder, and all the `*.GPR` files into a `GPR` folder. I then use [Adobe Digital Negative (DNG) Converter](https://helpx.adobe.com/camera-raw/using/adobe-dng-converter.html) to convert the `.GPR` files into `.DNG` so that I can import them to [Final Cut Pro (FCP/FCPX)](https://www.apple.com/final-cut-pro/). Adobe DNG Converter is a [graphical user interface (GUI)](https://www.computerhope.com/jargon/g/gui.htm) program which means I need to open the program, select input and ouput destinations, select my seetings, all while using the mouse to make my selections. It's slow and repetive (not to mention I make the same selections every time). I just want something that I can double click that will move the pictures to their respective folders and start the `GPR` to `DNG` conversion process. Turns out, as I suspected, the Adobe DNG Converter is running a command line program underneath the hood. Here's how we can use it without the GUI to "automate" away this repetitive task:

> Note that this article assumes you have basic familiarity with the terminal and shell commands
{: .prompt-warning }

## [TL;DR](https://www.merriam-webster.com/dictionary/TL%3BDR)
``` console
matt@mac $ /Applications/Adobe\ DNG\ Converter.app/Contents/MacOS/Adobe\ DNG\ Converter -fl -mp -d /path/to/output/folder /path/to/GPR/folder/*
```
Where
* `-fl = embed fast load data`
* `-mp = process multiple files in parallel`
  * `default is sequential (one image at a time)`
* `-d = output directory`

Additional arguments can be found in [this .pdf](https://helpx.adobe.com/content/dam/help/en/camera-raw/digital-negative/jcr_content/root/content/flex/items/position/position-par/download_section/download-1/dng_converter_commandline.pdf).

View the scripts I made for this post at my GitHub repo [*AdobeDNGConverterScripts*](https://github.com/mattpopovich/AdobeDNGConverterScripts).

## Installation
Go [here](https://helpx.adobe.com/camera-raw/using/adobe-dng-converter.html), download and install the application.

> This article was created using Adobe DNG Converter version 16.2.0
{: .prompt-info }

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
    - Don't embed original

Click "Convert" and let the program go to work

## Using the Command Line Interface (CLI)
Inside the `Adobe DNG Converter.app` is an executable file: `Adobe DNG Converter.app/Contents/MacOS/Adobe DNG Converter`

```console
matt@mac $ pwd
/Applications/Adobe DNG Converter.app/Contents/MacOS
matt@mac $ ls -l
total 551496
-rwxr-xr-x  1 root  wheel  282361984 Jun  1  2023 Adobe DNG Converter
```

I'm not sure how to bring up a help menu for it... The CLI for Adobe DNG Converter has limited documentation available. [This .pdf](https://helpx.adobe.com/content/dam/help/en/camera-raw/digital-negative/jcr_content/root/content/flex/items/position/position-par/download_section/download-1/dng_converter_commandline.pdf) is about all I can find. Thankfully, that `.pdf` explains some of the acceptable arguments that the executable understands.

If you want the same default settings that the GUI provides, you can use the following command:
```console
matt@mac $ /Applications/Adobe\ DNG\ Converter.app/Contents/MacOS/Adobe\ DNG\ Converter -fl -d /path/to/output/folder /path/to/GPR/folder/*
```
Where
* `-d = output directory`
* `-fl = embed fast load data`

And that's it! If you look in your `/path/to/output/folder`, you should see the converted `.DNG` files 🎉

But I'd recommend adding the `-mp` flag as it adds a [decent boost to processing times](#argument-runtime-and-file-size-comparison):
```console
matt@mac $ /Applications/Adobe\ DNG\ Converter.app/Contents/MacOS/Adobe\ DNG\ Converter -fl -mp -d /path/to/output/folder /path/to/GPR/folder/*
```

* `-mp = process multiple files in parallel`
  * `default is sequential (one image at a time)`

## Advanced information

### Reproducibility
Note that these files are not bitwise reproducible (but they are exactly the same size):
```console
matt@mac $ /Applications/Adobe\ DNG\ Converter.app/Contents/MacOS/Adobe\ DNG\ Converter -fl *.GPR
matt@mac $ /Applications/Adobe\ DNG\ Converter.app/Contents/MacOS/Adobe\ DNG\ Converter -fl *.GPR
matt@mac $ shasum -a 256 *.dng
486395fba712ddaf3265d503f53a21a0977401e95e935857863239017692d49f  GOPR0000.dng
66a4c517d62a396977cf101e49026e0dc2d4f9ab0775a6dd96b81e5dcd41daaa  GOPR0000_1.dng
5c647d26c98bbcb34f66c7c8530cc006fab6a716d13f42dc98fa63ddb1b0b3e7  GOPR0001.dng
2864621bea9c221750bcea31b52009a063a36ebfd025bc892267e20a22c3986f  GOPR0001_1.dng
matt@mac $ ls -l *.dng
-rw-r--r--  1 matt  staff  11876742 Feb 26 22:55 GOPR0000.dng
-rw-r--r--  1 matt  staff  11876742 Feb 26 22:55 GOPR0000_1.dng
-rw-r--r--  1 matt  staff  13340838 Feb 26 22:55 GOPR0001.dng
-rw-r--r--  1 matt  staff  13340838 Feb 26 22:55 GOPR0001_1.dng
```

### Argument runtime and file size comparison

I am using 3000x4000 `.GPR` (raw) files shot with my [GoPro](https://amzn.to/3ZUuXcD) Hero 8 Black:
```console
matt@mac $ file *.GPR
GOPR0000.GPR: TIFF image data, little-endian, direntries=58, height=3000, bps=16, compression=JBIG, ITU-T T.85, PhotometricIntepretation=(unknown=0xffff8023), description=C:\DCIM\100GOPRO\GOPR3115.GPR, manufacturer=GoPro, model=HERO8 Black, orientation=[*2*], width=4000

GOPR0001.GPR: TIFF image data, little-endian, direntries=58, height=3000, bps=16, compression=JBIG, ITU-T T.85, PhotometricIntepretation=(unknown=0xffff8023), description=C:\DCIM\100GOPRO\G0029214.GPR, manufacturer=GoPro, model=HERO8 Black, orientation=[*2*], width=4000

matt@mac $ ls -l *.GPR
-rwx------  1 matt  staff  6186776 Feb 26 22:54 GOPR0000.GPR
-rwx------  1 matt  staff  3677656 Feb 26 22:54 GOPR0001.GPR
```

<details markdown="1">
  <summary><a href="https://github.com/mattpopovich/AdobeDNGConverterScripts/blob/main/compare_AdobeDNGConverter_arguments.sh">I wrote a script</a> to compare the runtime and output file sizes of the different arguments for the executable</summary>
  ```console
  matt@mac $ ./compare_AdobeDNGConverter_arguments.sh
  Default = 25217580B, .992175s
  Using flags -c -p1        -cr7.1 -dng1.7.1 = -.0003828s (0%), +0B (+0%) vs default
  Using flags -u -p1        -cr7.1 -dng1.7.1 = -.0146741s (-1%), +0B (+0%) vs default
  Using flags -l -p1        -cr7.1 -dng1.7.1 = -.0108651s (-1%), +0B (+0%) vs default
  Using flags -c -p1 -e     -cr7.1 -dng1.7.1 = -.002032s (0%), +0B (+0%) vs default
  Using flags -c -p0        -cr7.1 -dng1.7.1 = -.066626s (-6%), -140136B (0%) vs default
  Using flags -c -p2        -cr7.1 -dng1.7.1 = +.7514072s (+75%), +3101062B (+12%) vs default
  Using flags -c -p1 -fl    -cr7.1 -dng1.7.1 = +.043321s (+4%), +2295970B (+9%) vs default
  Using flags -c -p1 -lossy -cr7.1 -dng1.7.1 = +.2135278s (+21%), -8252052B (-32%) vs default
  Using flags -c -p1 -mp    -cr7.1 -dng1.7.1 = -.3165521s (-31%), +0B (+0%) vs default
  ```
</details>

This particular example was ran using the two `*.GPR` files I mentioned above (available from [my GitHub repo](https://github.com/mattpopovich/AdobeDNGConverterScripts/tree/main/examples)).

<!-- Had to add <code> &nbsp; </code> here because spaces are not kept between `` unfortunately -->

| [Flags](https://helpx.adobe.com/content/dam/help/en/camera-raw/digital-negative/jcr_content/root/content/flex/items/position/position-par/download_section/download-1/dng_converter_commandline.pdf) | Speedup (s) | Speedup (%) | Size (bytes) | Size (%) |
|-------|-------------|-------------|--------------|----------|
| <code>-c -p1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -cr7.1 -dng1.7.1</code> | -.0003828s | 0%   | +0B         | +0% |
| <code>-u -p1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -cr7.1 -dng1.7.1</code> | -.0146741s | -1%  | +0B         | +0% |
| <code>-l -p1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -cr7.1 -dng1.7.1</code> | -.0108651s | -1%  | +0B         | +0% |
| <code>-c -p1 -e &nbsp;&nbsp;&nbsp; -cr7.1 -dng1.7.1</code>                | -.002032s  | 0%   | +0B         | +0% |
| <code>-c -p0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -cr7.1 -dng1.7.1</code> | -.066626s  | -6%  | -140,136B   | 0% |
| <code>-c -p2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -cr7.1 -dng1.7.1</code> | +.7514072s | +75% | +3,101,062B | +14% |
| <code>-c -p1 -fl &nbsp;&nbsp; -cr7.1 -dng1.7.1</code>                     | +.043321s  | +4%  | +2,295,970B | +4% |
| <code>-c -p1 -lossy -cr7.1 -dng1.7.1</code>                               | +.2135278s | +21% | -8,252,052B | -63% |
| <code>-c -p1 -mp &nbsp;&nbsp; -cr7.1 -dng1.7.1</code>                     | -.3165521s | -31% | +0B         | +0% |

Where
* Speedup = smaller (negative) is better
* Size = smaller (negative) is better

## Outro
Hope this was helpful and can save you some time!

Please let me know in the comments below if you have any suggestions or difficulties.

Thanks for reading!
