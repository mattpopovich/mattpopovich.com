---
title: "How to use VCDS (Ross-Tech) on a Mac"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2025-07-10 20:25:46 -0600
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

> This post is only for Macs with Apple Silicon (M1, M2, etc.) processors. If you're unsure which processor you have, follow [this](https://support.apple.com/en-us/116943) support page.
> If you'd like info for how to use VCDS with an Intel-based Mac, let me know in the comments!
{: .prompt-warning }

## Intro
I see a [few](https://forums.ross-tech.com/index.php?threads/42681/#post-349313) [people](https://www.reddit.com/r/Volkswagen/comments/1hbm5cw/vcds_working_on_m1_mac_with_hexcan_cable_apple/) online confirming that [VCDS](https://www.ross-tech.com/vag-com/VCDS.php) works on a Mac, but I don't see many tutorials of how they did it. It's relatively straightforward but I figured I'd make a tutorial to remove any possible confusion.

## TLDR
TODO

## Some VCDS Background
VCDS is a "[Windows-based diagnostic software for Volkswagen / Audi / Seat / Skoda](https://www.ross-tech.com/vag-com/VCDS.php)". VCDS is a software program which talks to a HEX-interface (hardware) which is plugged into and communicates with your vehicle. VCDS needs a [hardware interface](https://www.ross-tech.com/vcds/interfaces.php) in order to communicate with a vehicle.

TODO: Image schematic here

Currently [Ross-Tech](https://www.ross-tech.com/index.php) offers two hardware interfaces: [HEX-V2](https://www.ross-tech.com/vcds/hex-v2.php) and [HEX-NET](https://www.ross-tech.com/vcds/hex-net.php). HEX-V2 will communicate with VCDS via USB. HEX-NET will communicate with VCDS via USB or Wi-Fi.

[VCDS](https://www.ross-tech.com/vag-com/VCDS.php) is the full-fledged software program used with a hardware interface. It is written for Windows and they have [no plans of writing a version for Mac](https://forums.ross-tech.com/index.php?threads/14514/#post-130861) or Linux.

They also offer [VCDS-Mobile](https://www.ross-tech.com/vcds-mobile/vcds-mobile.php) to communicate to a hardware interface via Wi-Fi and a web browser. Because you only need a web browser and Wi-Fi, you can use VCDS-Mobile with any Android, iOS, Mac, Linux, Windows, etc. VCDS-Mobile is simply a local webpage hosted by a hardware interface and currently HEX-NET is the only hardware interface that supports this. Also worth noting is VCDS-Mobile is currently in beta and [does not have full feature parity](https://wiki.ross-tech.com/wiki/index.php/Functions) with VCDS.

### Legacy Hardware Interfaces
There are many [legacy interfaces](https://www.ross-tech.com/vag-com/old-interfaces/discontinued_interfaces.php) such as HEX+CAN, HEX+COM, etc. These interfaces require installing "legacy drivers" which are only available in x86-64 VCDS. This requires installing a x86-64 version of Windows. This is possible on an Apple Silicon Mac with UTM (I can confirm), but requires emulation of an Intel CPU. Expect much, much more CPU usage and much, much slower operation.

TODO: Ensure correct quote of legacy drivers

TODO: Image here

## Basic Hardware Check
If our hardware interface doesn't work, then there's no need to go any further as VCDS won't have anything to communicate with. I have a HEX-NET so connecting to VCDS is accomplished via a USB-B cable (sometimes referred to as a printer cable). The first thing we need to do is verify that our computer sees the HEX-NET interface. This can be confirmed by seeing both lights on the interface blinking blue. On a Mac, you can also go to the System Report (Settings --> General --> Scroll to the bottom --> System Report) --> USB and you should see a "TODO: Ross Tech" device confirming the connection.

If you only see one blinking light, that means the interface has power, but no data. In my experience, this was due to a faulty cable. Try bending either end of the cable in all directions to see if you can "bend some wires back together". For me, this was bending the USB-A side of the cable 90 degrees in the direction of TODO.

TODO: Image of USB bent + good connection next to image of USB not bent and bad connection.

I don't believe this is a rare issue. I've seen a few posts in their forums that are resolved with a [new USB-A to USB-B cable](https://store.ross-tech.com/shop/rtcusb-a2b02/).
TODO: link to posts

They also [sell a USB-C to USB-B cable](https://store.ross-tech.com/shop/usb-c/) so that newer laptops won't need to use a dongle. But, given their USB-A cable's reliability, I might recommend purchasing a [cheaper one](TODO).

Other blinking lights and their meanings are below ([source](https://forums.ross-tech.com/index.php?threads/8778/page-3#post-89230)):
* TODO

## Install VCDS

### Install UTM

### Install Windows

### Install VCDS




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
