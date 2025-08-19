---
title: "How to use VCDS (Ross-Tech) on a Mac"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2025-08-19 10:41:46 -0600
categories: [Blog, Not YouTube]    # <=2 values here: top category and sub category
tags: [apple, apple silicon, arm, audi, audi a3, audi a3 8v, big sur, catalina, how to, mac, monterey, not youtube, osx, sequoia, tech, tutorial, utm, volkswagen, vw, windows, vcds]                # TAG names should always be lowercase
layout: post                # post is the default, we will set it to be explicit
pin: false
toc: true                   # Table of contents
comments: true              # Enable/disable comments at the bottom of the post
math: false                 # Disabled by default for performance reasons
mermaid: false              # Diagram generation tool via ```mermaid [...]```
#img_cdn: https://cdn.com
#media_subpath: /img/path/
image:
  path: /assets/img/posts/2025-08-19-how-to-use-vcds-ross-tech-on-a-mac/vcds-on-mac-thumbnail.jpg
#   width: 1200   # in pixels
#   height: 630   # in pixels, 1.90:1 desired by chirpy
  alt: A theoretical image of VCDS running on macOS
#   show_image_in_post: false
description: Rumor has it that you can run VCDS on a Mac... here's how
---

> This post is only for Macs with Apple Silicon (M1, M2, etc.) processors. If you're unsure which processor you have, follow [this](https://support.apple.com/en-us/116943) support page.
> If you'd like info for how to use VCDS with an Intel-based Mac, let me know in the comments!
{: .prompt-warning }

## Intro
I see a [few](https://forums.ross-tech.com/index.php?threads/42681/#post-349313) [people](https://www.reddit.com/r/Volkswagen/comments/1hbm5cw/vcds_working_on_m1_mac_with_hexcan_cable_apple/) online confirming that [VCDS](https://www.ross-tech.com/vag-com/VCDS.php) works on a Mac, but I don't see many tutorials of how they did it. It's relatively straightforward but I figured I'd make a tutorial to remove any possible confusion.

## [TL;DR](https://www.merriam-webster.com/dictionary/TL%3BDR)
1. Ensure your [HEX-interface](https://www.ross-tech.com/vcds/interfaces.php) is seeing your computer: both LEDs should be blinking blue (interface connected to computer only) or green (interface connected to computer + vehicle)
1. Create a [Windows virtual machine (VM) on your Mac](/posts/how-to-run-windows-on-mac-via-utm)
1. Install [VCDS](https://www.ross-tech.com/vcds/download/current.php) in your Windows VM
1. If you plan on using your HEX-interface via USB, connect the USB device to your VM
1. Open up VCDS, go through the program options to [create a configuration for your device](https://youtu.be/tvh_5b5Gfqg?t=120)
  - Test the connection, then get to work!

## Some VCDS Background
VCDS is a "[Windows-based diagnostic software for Volkswagen / Audi / Seat / Skoda](https://www.ross-tech.com/vag-com/VCDS.php)". VCDS is a software program which talks to a HEX-interface (hardware) which is plugged into and communicates with your vehicle. VCDS needs a [hardware interface](https://www.ross-tech.com/vcds/interfaces.php) in order to communicate with a vehicle.

![Diagram showing VCDS software --> HEX-interface (hardware) --> Vehicle](/assets/img/posts/2025-08-19-how-to-use-vcds-ross-tech-on-a-mac/VCDS-architecture.jpg)
*Architecture of VCDS*

Currently [Ross-Tech](https://www.ross-tech.com/index.php) offers two hardware interfaces: [HEX-V2](https://www.ross-tech.com/vcds/hex-v2.php) and [HEX-NET](https://www.ross-tech.com/vcds/hex-net.php). HEX-V2 will communicate with VCDS via USB. HEX-NET will communicate with VCDS via USB or Wi-Fi.

[VCDS](https://www.ross-tech.com/vag-com/VCDS.php) is the full-fledged software program used with a hardware interface. It is written for Windows and they have [no plans of writing a version for Mac](https://forums.ross-tech.com/index.php?threads/14514/#post-130861) or Linux.

They also offer [VCDS-Mobile](https://www.ross-tech.com/vcds-mobile/vcds-mobile.php) to communicate to a hardware interface via Wi-Fi and a web browser. Because you only need a web browser and Wi-Fi, you can use VCDS-Mobile with any Android, iOS, Mac, Linux, Windows, etc. VCDS-Mobile is simply a local webpage hosted by a hardware interface and currently HEX-NET is the only hardware interface that supports this. Also worth noting is VCDS-Mobile is currently in beta and [does not have full feature parity](https://wiki.ross-tech.com/wiki/index.php/Functions) with VCDS.

### Legacy HEX Hardware Interfaces
There are many [legacy HEX hardware interfaces](https://www.ross-tech.com/vag-com/old-interfaces/discontinued_interfaces.php) such as HEX+CAN, HEX+COM, etc. These interfaces requires installing "USB Drivers for Legacy Interfaces" which are only available in x86-64 VCDS. This requires installing a x86-64 version of Windows. This is possible on an Apple Silicon Mac with UTM (I can confirm), but requires emulation of an Intel CPU. Expect much, much more CPU usage and much, much slower operation.

!["USB Drivers for Legacy Interfaces" checkbox during VCDS installation](/assets/img/posts/2025-08-19-how-to-use-vcds-ross-tech-on-a-mac/VCDS-LegacyDrivers.png){: .shadow .w-50}
*Checkbox needed during installation to support legacy HEX hardware interfaces*

## Basic Hardware Check
### Confirming USB Connection
If our hardware interface doesn't work, then there's no need to go any further as VCDS won't have anything to communicate with. I have a HEX-V2 so connecting to VCDS is accomplished only via a [USB-B cable](https://cdn.sparkfun.com/assets/f/7/4/a/7/51154e0ece395fee3f000002.jpg) (sometimes referred to as a printer cable). The first thing we need to do is verify that our computer sees the HEX-V2 interface. This can be confirmed by seeing **both** lights on the hardware interface blinking blue. On a Mac, you can also go to the System Report (Settings --> General --> Scroll to the bottom --> System Report) --> USB and you should see a "Ross-Tech HEX-V2" device confirming the connection.

![Image with both VCDS lights blinking blue + Ross-Tech HEX-V2 connected via USB in the Mac's System Report](/assets/img/posts/2025-08-19-how-to-use-vcds-ross-tech-on-a-mac/successful_HEX-V2_connection_annotated.jpeg){: .shadow .w-75}
*Successful HEX-V2 connection to a 2014 MacBook Pro*

### Troubleshooting Bad USB Connection
If you only see one blue blinking LED (or both LEDs blinking red), that means the interface has power, but no data. In my experience, this was due to a faulty cable. Try bending either end of the cable in all directions or pushing the cable together to "shorten the cable" next to the ends. The goal here is to try to touch some internally frayed wires back together. For me, this was bending the USB-A side of the cable greater than 45° + pushing the cable together a bit.

![Video demonstration that bending the cable at 90 degrees allows the HEX interface to be connected and restoring the cable to be straight loses USB connection](/assets/img/posts/2025-08-19-how-to-use-vcds-ross-tech-on-a-mac/HEX-V2_hardware-bad_cable.gif){: .shadow}
*A bad VCDS cable. Notice the lights on the HEX hardware interface going from blue to red.* <!-- TODO: Higher quality [here](TODO)* -->

I don't believe this is a rare issue. I've [seen](https://forums.ross-tech.com/index.php?threads/9704/) a [few](https://forums.ross-tech.com/index.php?threads/46210/post-378200) [posts](https://forums.ross-tech.com/index.php?threads/12161/post-110517) in their forums that are resolved with a [new USB-A to USB-B cable](https://store.ross-tech.com/shop/rtcusb-a2b02/).

They also [sell a USB-C to USB-B cable](https://store.ross-tech.com/shop/usb-c/) so that newer laptops won't need to use a dongle. I purchased a slightly [cheaper one](https://amzn.to/40Pggt4) (which I can confirm works).

Other blinking lights and their meanings are below ([source](https://forums.ross-tech.com/index.php?threads/8778/page-3#post-89230)):
Initially when plugging the HEX hardware interface in, you should see one LED blink green for about 2 seconds. Then, you will see the following:

<div align="center" markdown="1">

| LED blinking color           | Power | Computer Connection | Vehicle Connection |
| ---------------------------- | ----- | ------------------- | ------------------ |
| Both off                     |       |                     |                    |
| Single Blue (older firmware) | ✅     |                     |                    |
| Both red (newer firmware)    | ✅     |                     |                    |
| Both blue                    | ✅     | ✅                   |                    |
| Both yellow                  | ✅     |                     | ✅                  |
| Both green                   | ✅     | ✅                   | ✅                  |

</div>
<my-caption>The meaning of the HEX hardware interface's blinking lights</my-caption>


## Install VCDS
As I mentioned [above](#some-vcds-background), VCDS is "[**Windows-based** diagnostic software](https://www.ross-tech.com/vag-com/VCDS.php)". Since we are using a Mac, we will need some way to install and run Windows. Because my hardware interface is a HEX-V2, I will need USB support, which is best accomplished with a [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) (VM). You may be able to use [Wine](https://www.winehq.org) or [CrossOver](https://www.codeweavers.com/crossover/) with a HEX-NET, but I won't be covering that in this post.

### Create a Windows VM
There are a few different options for creating a virtual machine. This post will be using [UTM](https://mac.getutm.app) as it is free and I have confirmed it works. For other VM options, see my post [here](/posts/how-run-windows-on-mac-via-utm/#options-for-running-windows-on-a-mac).

To keep this post short, I've separated the Windows virtual machine section into its own post: [*How to Run Windows on Mac via UTM*](/posts/how-run-windows-on-mac-via-utm). Follow that guide, then come back here to install VCDS in your new Windows VM!

### Install VCDS in Windows VM
1. In our Windows VM, open Microsoft Edge
1. Navigate to [https://www.ross-tech.com/vcds/download/current.php](https://www.ross-tech.com/vcds/download/current.php)
1. Scroll down and click on the blue "DOWNLOAD" button
  - Note that the scrolling preferences (natural vs reverse scrolling) maybe be different that what is set on your Mac. You may have to scroll up to go down, or vice versa.
1. Open the `VCDS-Release-*-Installer.exe` file once it is finished downloading
1. Click on `No` when prompted if you'd like to see the installation instructions
1. Click on `Next >`
1. Accept the terms of the license agreement + click `Next >`
1. Leave the default selected components. Click `Next >`
  - `Open Windows Firewall for HEX-NET & VCIConfig` + `Create Start Menu Shortcuts` + `Create a Desktop Shortcut` should all be checked.
  - If you need `USB Drivers for Legacy Interfaces`, you wil need to download and install [Windows 11 x86-64](https://www.microsoft.com/en-us/software-download/windows11). Apple Silicon Macs will need to "emulate" this VM (not "virtualize"). UTM can do this, but expect much, much less performance.
1. Click `Install`
1. Click `Finish` to open VCDS

## Use VCDS
1. Plug in your VCDS hardware interface (HEX-V2, HEX-NET, etc.)
- [Confirm the hardware device has a valid USB connection](#confirming-usb-connection)
  - You should see both LEDs blinking blue or green on the hardware interface
- I've also found that my Mac has difficulties seeing the hardware interface if it is already plugged into a vehicle. If having difficulties, unplug it from a vehicle, then plug it into your Mac.
1. Open your Windows VM + open VCDS
1. In your Windows UTM window, click on the "USB devices" (top right), then select your VCDS hardware interface to connect it to your Windows VM
  - You may then get a popup saying "UTM wants to access `Ross-Tech HEX-*`", click to allow access.
  - You should hear a Windows chime alerting you that a device was connected
1. In VCDS, you will see an information prompt stating "First use/No config file found". Notice that all the VCDS buttons are greyed out. Click on `Options` to tell VCDS how to connect to our hardware interface.
1. Select your correct "Port and Protocol Options"
  - Since I am using a HEX-V2 via USB, I will select the "USB" port
1. Click `Test` to verify the connection
1. You will get a popup with some information about the connection. Click `OK`
  - Hopefully it says `Interface: Found!"
1. Click `Save`

You can now use VCDS! Plug the hardware interface into your vehicle, then get to work.

[A common first step](https://youtu.be/AK1lK5DRNcg?t=3) would be to perform an "[Auto-Scan](https://www.ross-tech.com/vcds/tour/autoscan.php)": Click on `Auto-Scan`, then click on `Start` to scan all the controllers in the vehicle for fault codes. This takes about 3 minutes for my 2015 Audi A3 (8V).

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
