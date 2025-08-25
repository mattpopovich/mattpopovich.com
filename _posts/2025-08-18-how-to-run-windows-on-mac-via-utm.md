---
title: "How to Run Windows on Mac (via UTM)"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2025-08-18 16:34:55 -0600
categories: [Blog, Not YouTube]    # <=2 values here: top category and sub category
tags: [apple, apple silicon, arm, mac os, not youtube, programming, tech, tutorial, windows, utm]                # TAG names should always be lowercase
layout: post                # post is the default, we will set it to be explicit
pin: false
toc: true                   # Table of contents
comments: true              # Enable/disable comments at the bottom of the post
math: false                 # Disabled by default for performance reasons
mermaid: false              # Diagram generation tool via ```mermaid [...]```
#img_cdn: https://cdn.com
#media_subpath: /img/path/
image:
  path: /assets/img/posts/2025-08-18-how-to-run-windows-on-mac-via-utm/windows-on-mac-thumbnail.jpg
#   width: 1200   # in pixels
#   height: 630   # in pixels, 1.90:1 desired by chirpy
  alt: A macOS screenshot with an UTM window open that is running Windows
#   show_image_in_post: false
description: A quick tutorial on how to run a Windows virtual machine on your Mac using UTM
---

> This post is only for Macs with Apple Silicon (M1, M2, etc.) processors. If you're unsure which processor you have, follow [this](https://support.apple.com/en-us/116943) support page.
> If you'd like info for how to create a Windows VM (virtual machine) with an Intel-based Mac, let me know in the comments!
{: .prompt-warning }

## Intro
MacOS is great but sometimes you can't get around a need for Windows.
- Legacy application
- Windows-only applications
- Developer that needs to test on multiple operating systems
- etc.

For me, [I use some vehicle diagnostic software](/posts/how-to-use-vcds-ross-tech-on-a-mac) that only runs on Windows ([VCDS](https://www.ross-tech.com/vag-com/VCDS.php)). I have also needed to access some hardware USB devices via docker, which is not supported on Mac ([GitHub issue created in 2016](https://github.com/docker/for-mac/issues/900) 🤕).

Whatever your reason, here's how:

## [TL;DR](https://www.merriam-webster.com/dictionary/TL%3BDR)
1. Download and install [UTM](https://github.com/utmapp/UTM/releases/latest/download/UTM.dmg)
1. Download an [ARM version of Windows 11](https://www.microsoft.com/en-us/software-download/windows11arm64)
1. Follow [this guide](https://docs.getutm.app/guides/windows/) to create and install a new Windows 11 VM in UTM
1. Profit

## Options for Running Windows on a Mac
Since we are using a Mac, we will need some way to install and run Windows. Common options are:
* Dual-booting (Intel Macs only: [Boot Camp](https://support.apple.com/en-us/102622))
  * Shut down macOS, install Windows onto the hard drive, and fully boot into Windows.
* [Wine](https://www.winehq.org)/[CrossOver](https://www.codeweavers.com/crossover/) (limited USB support)
  * Allows you to run Windows applications on macOS / Linux. Installs the application only. Does not emulate a whole operating system, so should have better performance.
* Virtual machine ([UTM](https://mac.getutm.app), [Parallels](https://www.parallels.com), [VMWare Fusion Pro](https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion), [VirtualBox](https://www.virtualbox.org))
  * While running macOS, run an application that runs a fully-fledged Windows operating system.

Since all recent macs are on Apple Silicon, that rules out dual-booting. If you need USB support, that will rule out Wine and CrossOver. This leaves us to using a virtual machine. I think any of them would work just fine. Parallels is paid, the others are free (VMWare is free for personal use). I'm going to document UTM in this post for no reason other than that's what I'm familiar with (a few years ago, it was the only free option available), and it works great!

The typical consensus is Parallels ($) > VMWare Fusion Pro (used to be $, now free for personal use) > UTM ([FOSS](https://en.wikipedia.org/wiki/Free_and_open-source_software)) > VirtualBox ([FOSS](https://en.wikipedia.org/wiki/Free_and_open-source_software)).

## Install UTM
> See the official UTM installation guide for macOS [here](https://docs.getutm.app/installation/macos/)
{: .prompt-info }

[UTM](https://mac.getutm.app) can virtualize Windows, Linux, and even macOS itself in macOS. It can even emulate x86-64 (Intel) processors (very slowly) to run x86 operating systems.

1. Download UTM [here](https://github.com/utmapp/UTM/releases/latest/download/UTM.dmg)
1. Open `UTM.dmg`
1. Drag `UTM.app` to the `Applications` folder

UTM has now been installed. Double click `UTM.app` in the Applications folder to open it.

## Create a Windows VM in UTM
> See the official Windows 11 UTM guide [here](https://docs.getutm.app/guides/windows/).
{: .prompt-info }

### Download Windows
Next, we will need to get an operating system to virtualize. This article is for Macs with Apple Silicon (ARM processors), so we should download an [ARM version of Windows 11](https://www.microsoft.com/en-us/software-download/windows11arm64).
1. Select the "Windows 11 (multi-edition ISO for Arm64)"
1. Click "Download Now"
1. Choose your product language
1. Click "Confirm"
1. Click "Download Now"
This will download a `Win11_*Arm64.iso` which will be ~5.5GB.

### Create Windows VM
1. Open UTM
2. Click on "Create a New Virtual Machine"
3. Virtualize (our native CPU architecture is ARM and we will be using Windows 11 for ARM)
4. Windows
5. Make sure “Install Windows 10 or higher” and “Install drivers and SPICE tools” is *checked*. Also make sure “Import VHDX Image” is *unchecked*. Press “Browse” and select the ISO you downloaded previously. Click "Continue"
6. Select the amount of RAM and CPU Cores you'd like to give the VM.
  - These will be fully reserved by the VM whenever it is running, so don't give it too much resources and thereby starving your host operating system.
  - For the initial install, it's not a bad idea to give it extra resources to speed up the install. You can always change the resource allocation later.
  - I'd recommend at least 2048MiB of RAM + 2 CPU cores. Press “Next” to continue.
    - Microsoft [says Windows 11 requires](https://support.microsoft.com/en-us/windows/windows-11-system-requirements-86c11283-ea52-4782-9efd-7674389a7ba3) at least 2 cores, 4GB RAM, and 64GB hard drive... but I haven't seen that enforced in the installer.
7. Specify the maximum amount of drive space to allocate. Press “Next” to continue.
- I'd recommend at least 32GiB. Windows 11 itself takes up ~22GiB.
  - Note that increasing this size in the future can be a little tricky. I've found it easier to store things in a shared directory (see #8) than increasing the drive space.
8. If you have a directory you'd like to mount (share with) in the VM, select it here.
  - Ex. If you select your Mac's *Downloads* folder, you will be able to add/view/modify files in your Mac's *Downloads* folder while you are in the Windows VM. It will appear as a "Network Drive" in Windows.
  - You can always change this later.
9. Press "Save" to create the VM.
  - I like to rename my VM to "Windows11arm" or similar.

### Install Windows 11
In UTM, select the VM that we just created on the left side, then press the play button to boot up the VM and begin the installation.
- Make sure you press a key when `Press any key to boot from CD or DVD...` is shown. Otherwise, you will end up at a black screen with `Shell> _`.
  - If you end up at `Shell> _`, type `exit` + press Enter. This will kick you back out to the BIOS. Use the down arrow key to go to "Continue". Press Enter.
  - You will then see `Press any key to boot from CD or DVD...`. Press a key, otherwise you will end up back at `Shell> _`.
- If you get stuck anywhere, feel free to click on the red "x" in the top left to quit the VM and start over.

<details markdown="1">
  <summary> Follow the Windows 11 installation prompts (click here to show them all ℹ️) </summary>
1. Select your language + time and currency format. Click `Next`
2. Select keyboard or input method. Click `Next`
3. Enter your product key
  - You can also click `I don't have a product key` but using Windows without a product key is against the EULA (end user license agreement). See [*Section 5*](https://www.microsoft.com/content/dam/microsoft/usetm/documents/windows/11/oem-(pre-installed)/UseTerms_OEM_Windows_11_English.pdf).
4. Select `Windows 11 Home`. Click `Next`
5. Accept license terms
6. Select `Disk 0 Unallocated Space`. Click `Next`
7. Confirm your country or region. Click `Yes`
8. Confirm your keyboard layout or input method. Click `Yes`
9.  Select if you'd like to add a second keyboard layout
10. Enter your name. Click `Next`
11. Enter a password. Click `Next`
12. Confirm your password. Click `Next`
13. Create 3 security questions, clicking `Next` each time
  - If you don't want to create security questions, use a blank password in the step above.
14. Wait for the installation to complete + reboot
15. Sign into Windows 11 + wait for more installation steps to complete
16. Once you're signed in, you should be prompted with the *UTM Guest Tools Installer*.
17. Click on `Next >`
18. Click on `I Agree`
19. Click on `Finish`
</details>

## Using the Windows VM
That's it! You now have a fully functioning Windows virtual machine running on macOS.

If you'd like to change the resources for this VM, shut down the VM. Then, at the main UTM screen, select the VM from the sidebar on the left, then click the "Edit selected VM" button on the top right. From here you can go to "System" to change the RAM, CPU cores, etc.

If you want to attach a USB device to the VM, plug it into your machine, boot up the VM, then click on the "USB devices" button in the top right. You should then see available USB devices that you can "pass-through" to the VM.

## Outro
Hope this was helpful! Please let me know of any issues or suggestions you have in the comments 😊

<!--
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
-->
