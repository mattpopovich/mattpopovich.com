---
title: "How to Outsmart Your Phone's Tethering Restrictions"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2025-10-25 22:03:06 -0600
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
ISPs (internet service providers) will commonly disable / throttle / or limit tethering from one device to another. Ex. You want to use your phone's hotspot on your laptop while traveling. Most of this comes down to limiting the amount of bandwidth and congestion on their networks. But also if you could just share a cellular plan from your phone, why would you pay an extra fee to connect an LTE iPad to their network? (You normally wouldn't)

ISPs do (at least) two things to determine if traffic is coming from a phone or a hotspot device. This article will tell you what those two things are and how we can go into "incognito mode" to make it more difficult for them to identify 🕵

## [TL;DR](https://www.merriam-webster.com/dictionary/TL%3BDR)
1. Change TTL (time to live) on tethered device to cell phone's TTL+1
2. Use a VPN / something to encrypt your traffic to prevent the provider from inspecting your packets

## Step One: TTL
The first thing that ISPs will look at whenever you are trying to send data is a packet's [TTL](https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/) (time to live). Basically, each packet you send has a TTL value which represents "how many network devices can this packet go through to get to its destination before you give up". This is to ensure packets can't get stuck in a "network loop" forever. A common TTL value is 64 which means this packet can pass through 64 "hops" to get to its destination. If it takes longer than that, stop forwarding it. Every time a network device receives and fowards a packet, it will decrease the packet's TTL by one.

ISPs know the default TTL values for different devices: iOS=64, Android=64, Windows=128, Linux=64, macOS=64, etc. Imagine a Mac is tethered to an iPhone. The Mac sends a packet with a TTL of 64 to the iPhone, which decreases the packet's TTL by one to 63, which it then forwards to the ISP. The ISP receives the packet, sees an odd and non-standard TTL value, and immediately assumes the packet is coming from a tethered device which it can then reject, slow down, etc.

Defeating this is simple enough. The TTL value is configurable. We need to find out what the TTL value is on the hotspot device, then we will set our tethered device's TTL to one above that. This way, all the packets sent by the hotspot device will have its default TTL value!

As an example, imagine you are using an iPhone or Android hotspot with a TTL value of 64. On the tethered device, you will set its TTL to 65. This way, the packet's TTL will get decremented to 64 by the hotspot, and all packets received by the ISP will have a TTL of 64, making traffic from the hotspot and tethered device indistinguishable.

### Setting TTL on macOS

> The next part of this post utilizes the terminal. If you are unfamiliar with the terminal or would like to learn more, check out my post [here](/posts/introduction-to-the-command-line-shell-terminal-etc/) for an "Introduction to the Terminal / Shell / Command Line, etc.".
{: .prompt-info }

Open `Terminal.app`. You can run the following to see what the TTL value is currently set to:
```console
$ ping localhost
PING localhost (127.0.0.1): 56 data bytes
64 bytes from 127.0.0.1: icmp_seq=0 ttl=64 time=0.086 ms
```

Press `control (^)` + `C` to stop the `ping`.

Here we see `ttl=64`, which is the default value. You can then run the following command to change the value to 65:

```console
$ sudo sysctl -w net.inet.ip.ttl=65
```

This value will only be set until restart. Once you shut down your computer, it will go back to the default value. Let's verify it was set correctly:

```console
% ping localhost
PING localhost (127.0.0.1): 56 data bytes
64 bytes from 127.0.0.1: icmp_seq=0 ttl=65 time=0.054 ms
```

`ttl=65`. Great!

To have these TTL settings persist after a reboot, see [this StackExchange answer](https://superuser.com/a/1516451/552207).

### Setting TTL on Windows (untested)

Windows is a little more tricky as we have to modify the registry. [Source](https://learn.microsoft.com/en-us/troubleshoot/windows-client/networking/tcpip-and-nbt-configuration-parameters?utm_source=chatgpt.com)
1. Press Win + R, type regedit, and press Enter.
2. `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters`
3. Right-click in the right pane → New → DWORD (32-bit) Value
4. Name it `DefaultTTL`
5. Double-click it and set the Value data (in Decimal) to your desired TTL, e.g. 65.
6. Click OK and close the Registry Editor.
7. Reboot your computer for the changes to take effect.

Or, in `Powershell`:
```console
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" -Name "DefaultTTL" -Value 65 -Type DWord
```

Then reboot. Both of these settings will persist after a reboot.

### Setting TTL in Ubuntu (untested)

```console
$ sudo sysctl -w net.ipv4.ip_default_ttl=65
```

Again, this is only for the current boot. Restarting will reset this value.

To persist this value, add the following line to `/etc/sysctl.conf`:

```console
net.ipv4.ip_default_ttl=65
```
{: file='/etc/sysctl.conf'}

Note that this is only for IPv4. To change things for IPv6, see [this StackExchange post](https://askubuntu.com/a/1388114/565704).

## Step Two: Encrypt Packets
If the TTL solution above doesn't get things working or speed things up, your ISP is probably doing some sort of [DPI](https://en.wikipedia.org/wiki/Deep_packet_inspection) (deep packet inspection). What exactly they are doing is beyond the scope of this post (but researching [TLS fingerprints](https://fingerprint.com/blog/what-is-tls-fingerprinting-transport-layer-security/) can point you in the right direction). We should be able to defeat it by using an encrypted tunnel such as a VPN. HTTPS will encrypt the application payload, but not much of the metadata. ISPs can infer a good bit from the metadata, such as “You are connected to this website with this operating system and browser to download a webpage / stream music / stream video". An encrypted tunnel obscures more data than HTTPS: it will hide pretty much everything except the IP address that you are communicating with from your ISP. Thus, your ISP will know which VPN you are communicating with, but that's about it.

> Note that while your ISP now can't see much, your VPN now has that data.
> {: .prompt-warning }

There are plenty of VPNs out there. Mullvad is a common recommendation for being the best in privacy. But if you're just trying to get around ISP limitations, any VPN will work.

[1.1.1.1](https://one.one.one.one) might work for this (TODO).

Additionally, you can make your own VPN (for free) very easily by using [Tailscale](https://tailscale.com)! All you need is your own device that is powered on and connected to the internet (such as an Apple TV or a desktop) which will be used to route traffic to. They have a great ["getting started" video](https://www.youtube.com/watch?v=sPdvyR7bLqI).

## Outro
You may have to use step one, step two, or a combination of both to get around ISP limitations.

There's just something very satisfying about using technology to enable technology 😎

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
