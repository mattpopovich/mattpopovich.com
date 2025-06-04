---
title: "Is Ethernet Over Powerline Any Good?"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2025-06-04 00:09:49 -0600
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

<!--
Subtitle: Ethernet through your walls?

https://capitalizemytitle.com/youtube-title-checker/
Is Ethernet Over Powerline Any Good? = 57 + 60 + 80 = 197
are Powerline to ethernet adapters any good? = 54 + 60 + 80 = 194
what to know about ethernet over Powerline = 57 + 69 + 50 = 176
what you need to know about Powerline to ethernet adapters = 64 + 59 + 50 = 173
let's talk about Powerline to ethernet adapters = 46 + 64 + 50 = 160
let's talk about ethernet over Powerline = 47 + 65 + 50 = 162
what to expect with ethernet over Powerline = 56 + 64 + 50 = 170
-->

## Intro
Powerline to ethernet adapters aren't great, and many people online swear against them. But, they do have a use case: you do not want to (or cannot) run ethernet or coaxial cables and WiFi does not reach or is too unreliable. If this is your scenario, powerline might be a quick and easy solution. The good thing about powerline is that it's extremely easy to test: buy two adapters and plug them into the wall! No construction necessary.

>In short: `Ethernet > Coax > WiFi >> Powerline `

If you understand powerline's weaknesses, I believe that it can be an effective tool to supplement your network. Here is how and why I added it to my network, what speeds you can realistically expect out of powerline, and tips for getting the most out of powerline adapters.

## Why I Added Powerline to my Network
I was upgrading the WiFi in my (a friend's) house, and I first tested my current WiFi speeds using [`iperf3`](https://iperf.fr) at various locations around the house to establish a baseline. Then I tested [a wireless mesh network](https://amzn.to/452BPsZ) and how different locations for access points affected performance, and lastly I tested the mesh network but with an ethernet backhaul [over coaxial](https://amzn.to/4kRYNYA), which was the best option.
<!-- TODO: Add link to iperf3 post -->
<!-- TODO: Add link to wireless mesh network post -->

However, my garage is disconnected from the house and receives pretty poor WiFi performance. I didn't really want to run a new wire the whole way to the garage... but then I remembered I already have wires running to the garage (electricity) and I can try to run ethernet over that! I didn't need a lot of speed, I just wanted consistent, reliable performance. Thus, if powerline could give me a reliable >20Mbps, I could use that as an "ethernet backhaul" to then add another wireless access point to the mesh network and cover the whole garage with reliable WiFi!

Spoiler alert: it actually worked pretty well! Let's get into some numbers:

## Real-world Powerline Speeds

### Testing Setup
The house I'm testing this on was built in the 1980s-1990s. I don't know exactly what that means in terms of electrical wiring standards, but you can probably expect a bit worse performance if your house is older, and better performance if your house is newer. 🤷‍♂️

<!-- TODO: Add image here of before and after -->

My testing setup is capable of ~1Gbps throughput. A 10 second `iperf3` test from laptop --> ethernet --> router --> ethernet --> laptop gave 918Mbps. We'll be effectively performing the same test but removing the router and adding the powerline adapters. Thus, this system is capable of testing *up to* 918Mbps.

All tests will be 10s runs of `iperf3`. I'll run it twice and report the average.

### Speeds

#### Testing from Central Point in the House
I set up shop in a central room in the house and started testing throughput to other outlets. The first thing I test was two outlets directly (~6ft) next to each other only gave ~325Mbps. So... do not expect to reach the "1000Mbps" given by the marketing material.

<!-- Image of testing throughout the house from the playroom -->

TODO: Takeaways

#### Testing from the End of the House

<!-- Image of testing throughout the house from the playroom -->

TODO: Takeaways

#### Testing from the Electrical Panel

<!-- Image of testing throughout the house from the playroom -->

TODO: Takeaways

#### Testing when Directly Connected

TODO: Takeaways

## Tips for getting the most out of powerline

TODO: Takeaways, might already explain some of this above

## Summary

TODO: Takeaways


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
