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
Expanding on [my previous project](my-fcpx-export-settings) converting image time lapses into videos, every time I shoot a timelapse with my [GoPro (affiliate link)](https://amzn.to/3ZUuXcD) in raw, I end up with a folder full of `*.JPG` and `*.GPR` files. I want to put those two into their own folders and convert the `.GPR` files into `.DNG` files that can be used by [Final Cut Pro (FCP/FCPX)](https://www.apple.com/final-cut-pro/). I do this with [Adobe Digital Negative (DNG) Converter](https://helpx.adobe.com/camera-raw/using/adobe-dng-converter.html). It's a [graphical user interface (GUI)](https://www.computerhope.com/jargon/g/gui.htm) program which requires me to use the mouse and select files... it's repetive and I select the same settings every time... I just want something I can double click that will immediately kick off the conversion for me. Turns out, as I suspected, the Adobe DNG Converter is running a command line program underneath the hood. Here's how we can use it without the GUI:

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

Additional arguments can be found in [this .pdf](https://helpx.adobe.com/content/dam/help/en/camera-raw/digital-negative/jcr_content/root/content/flex/items/position/position-par/download_section/download-1/dng_converter_commandline.pdf)

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

I'm not sure how to bring up a help menu for it... The CLI for Adobe DNG Converter has about 0 documentation that I've been able to find. [This .pdf](https://helpx.adobe.com/content/dam/help/en/camera-raw/digital-negative/jcr_content/root/content/flex/items/position/position-par/download_section/download-1/dng_converter_commandline.pdf) is about all I can find, thankfully it explains some of the acceptable arguments that the executable understands.

If you want the same default settings that the GUI provides, you can use the following command:
```console
matt@mac $ /Applications/Adobe\ DNG\ Converter.app/Contents/MacOS/Adobe\ DNG\ Converter -fl -d /path/to/output/folder /path/to/GPR/folder/*
```
Where
* `-d = output directory`
* `-fl = embed fast load data`

And that's it! If you look in your `/path/to/output/folder`, you should see the converted `.DNG` files. 🎉

But I'd recommend adding the `-mp` flag as it adds a [decent boost to processing times](TODO):
```console
matt@mac $ /Applications/Adobe\ DNG\ Converter.app/Contents/MacOS/Adobe\ DNG\ Converter -fl -mp -d /path/to/output/folder /path/to/GPR/folder/*
```

* `-mp = process multiple files in parallel`
  * `default is sequential (one image at a time)`

## Advanced information

### Reproducibility
Note that these files are not bitwise reproducible (but they are exactly the same size):
```console
matt@mac $ ./reset.sh && ./organizeGoProDNG.sh
total 58312
-rw-r--r--  1 mattpopovich  staff  15302818 Feb 23 17:55 GOPR0924.dng
-rw-r--r--  1 mattpopovich  staff  14546400 Feb 23 17:55 GOPR0925.dng
f1f7e65b828b030cf51dbe5fa7007548910a072a0c6fe525cd8b03425e26d1fa  DNG/GOPR0924.dng
fbcd20d29a58756f9078376d4387fc3e40098f1be76ed5e94e83111b69a9c209  DNG/GOPR0925.dng

matt@mac $ ./reset.sh && ./organizeGoProDNG.sh
total 58312
-rw-r--r--  1 mattpopovich  staff  15302818 Feb 23 17:55 GOPR0924.dng
-rw-r--r--  1 mattpopovich  staff  14546400 Feb 23 17:55 GOPR0925.dng
89c647242e6348a2275dfda381e674fa462476bb5f7868f250c1849f3879fa21  DNG/GOPR0924.dng
07cff6d3be3d8d9e3fdcd492c7a9f785fa6ae58e9dd10dff46a2b2538de3adc5  DNG/GOPR0925.dng
```

### Argument runtime and file size comparison

I am using 3000x4000 `.GPR` (raw) files shot with my [GoPro](https://amzn.to/3ZUuXcD) Hero 8 Black:
```console
matt@mac $ file GPR/*
GPR/GOPR0924.GPR: TIFF image data, little-endian, direntries=57, height=3000, bps=16, compression=JBIG, ITU-T T.85, PhotometricIntepretation=(unknown=0xffff8023), description=C:\DCIM\100GOPRO\GOPR0924.GPR, manufacturer=GoPro, model=HERO8 Black, orientation=[*2*], width=4000

GPR/GOPR0925.GPR: TIFF image data, little-endian, direntries=58, height=3000, bps=16, compression=JBIG, ITU-T T.85, PhotometricIntepretation=(unknown=0xffff8023), description=C:\DCIM\100GOPRO\GOPR0925.GPR, manufacturer=GoPro, model=HERO8 Black, orientation=[*2*], width=4000

matt@mac $ ls -l GPR
-rwxr-xr-x  1 mattpopovich  staff  3926850 Feb 23 18:19 GOPR0924.GPR
-rwxr-xr-x  1 mattpopovich  staff  3492368 Feb 23 18:19 GOPR0925.GPR
```

<details markdown="1">
  <summary>I wrote a script to compare the output sizes of the different arguments for the script:</summary>
  ```console
  matt@mac $ ./compareDNGsettings.sh
  Default = 28492484B, .8896226s
  Using flags -c -p1 -cr7.1 -dng1.7.1 = -.0081965s (0%), +0B (+0%) vs default
  Using flags -u -p1 -cr7.1 -dng1.7.1 = -.0341326s (-3%), +0B (+0%) vs default
  Using flags -l -p1 -cr7.1 -dng1.7.1 = +.0024795s (+0%), +0B (+0%) vs default
  Using flags -c -e -p1 -cr7.1 -dng1.7.1 = -.0055936s (0%), +0B (+0%) vs default
  Using flags -c -p0 -cr7.1 -dng1.7.1 = -.0499066s (-5%), -238840B (0%) vs default
  Using flags -c -p2 -cr7.1 -dng1.7.1 = +.7349366s (+82%), +4165366B (+14%) vs default
  Using flags -c -p1 -fl -cr7.1 -dng1.7.1 = +.0102043s (+1%), +1379742B (+4%) vs default
  Using flags -c -p1 -lossy -cr7.1 -dng1.7.1 = +.1604536s (+18%), -18143172B (-63%) vs default
  Using flags -c -mp -p1 -cr7.1 -dng1.7.1 = -.2128286s (-23%), +0B (+0%) vs default
  ```
</details>

This particular example was ran using the two `*.GPR` files I mentioned above.

| [Flags](https://helpx.adobe.com/content/dam/help/en/camera-raw/digital-negative/jcr_content/root/content/flex/items/position/position-par/download_section/download-1/dng_converter_commandline.pdf) | Speedup (s) | Speedup (%) | Size (bytes) | Size (%) |
|-------|-------------|-------------|--------------|----------|
| `-c -p1        -cr7.1 -dng1.7.1` | -.0081965s | 0% | +0B | +0% |
| `-u -p1        -cr7.1 -dng1.7.1` | -.0341326s | -3% | +0B | +0% |
| `-l -p1        -cr7.1 -dng1.7.1` | +.0024795s | +0% | +0B | +0% |
| `-c -p1 -e     -cr7.1 -dng1.7.1` | -.0055936s | 0% | +0B | +0% |
| `-c -p0        -cr7.1 -dng1.7.1` | -.0499066s | -5% | -238,840B | 0% |
| `-c -p2        -cr7.1 -dng1.7.1` | +.7349366s | +82% | +4,165,366B | +14% |
| `-c -p1 -fl    -cr7.1 -dng1.7.1` | +.0102043s | +1% | +1,379,742B | +4% |
| `-c -p1 -lossy -cr7.1 -dng1.7.1` | +.1604536s | +18% | -18,143,172B | -63% |
| `-c -p1 -mp    -cr7.1 -dng1.7.1` | -.2128286s | -23% | +0B | +0% |

Where
* Speedup = smaller (negative) is better
* Size = smaller (negative) is better

## Outro
Hope this was helpful and can save you some time!

Please let me know in the comments below if you have any suggestions or difficulties.

Thanks for reading!
