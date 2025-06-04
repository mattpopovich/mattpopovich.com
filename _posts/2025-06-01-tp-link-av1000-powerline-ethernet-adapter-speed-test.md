---
title: "TP-Link AV1000 Powerline Ethernet Adapter Speed Test"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2025-06-01 07:28:31 -0600
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




Testing the [TP-Link AV1000 Powerline Ethernet Adapter (TL-PA7017P)](https://amzn.to/3T0oMAT).

All TP-Link powerline adapters: [Amazon.com](https://amzn.to/4kpYynC), [TP-Link.com](https://www.tp-link.com/us/home-networking/powerline/).

## Testing Performance

All were 10s tests. Unless specified, data transfer speed is given as seen at the receiver. House was built in the 1980s-1990s.

### Control

2012 MBPr -> Gigabit Thunderbolt to Ethernet --> 6ft Cat5e Ethernet Cable ([1Gbps](https://www.fs.com/blog/cat5e-cat6a-cat7-and-cat8-cable-buying-guide-2647.html)) --> TP Link X55 (1Gbps) --> 50ft Cat6 Ethernet Cable ([1-10Gbps](https://www.fs.com/blog/cat5e-cat6a-cat7-and-cat8-cable-buying-guide-2647.html)) --> TP Link Gigabit Switch --> 6ft Cat6 Ethernet Cable ([10Gbps](https://www.fs.com/blog/cat5e-cat6a-cat7-and-cat8-cable-buying-guide-2647.html)) --> [Mokin USB C Gigabit Ethernet Adapter](https://amzn.to/43Kevhq) --> M1 MacBook Air
```
[  5]   0.00-10.01  sec  1.07 GBytes   921 Mbits/sec                  sender
[  5]   0.00-10.01  sec  1.07 GBytes   918 Mbits/sec                  receiver
```

This control test shows that I have ~gigabit communication capabilities between my 2012 MBPr and M1 MacBook Air. Thus, I have the capability to confirm that the powerline adapters are capable **up to** 918Mbps. I can confirm below that, but not above it.

### Testing from the middle of the house

Two outlets that are 6ft away from each other and very likely on the same circuit:
306Mbps, 339Mbps, 329Mbps = 325Mbps on average

I then tried another adjacent outlet in the same room. Also about 6ft away and very likely on the same circuit:
340Mbps, 343Mbps = 341.5Mbps on average

I then moved to the next outlet in the same room. About 8ft away and very likely on the same circuit:
338Mbps, 342Mbps

I then plugged a lamp into the same outlet and turned it on to see if this additional power draw or interference had any affect (it did not):
344Mbps, 339Mbps

I then moved to the next outlet. We are now 3 outlets away from each other. 12ft or so:
311Mbps, 308Mbps

I now moved away from that room and into a hallway. Still about 12ft. This is likely a different circuit as the speeds show:
87.2Mbps, 84.9Mbps

I now move to the back of that hallway. 30ft total distance between the two computers as the fly flies:
35.1Mbps, 33.6Mbps

In the middle of that hallway is a bathroom. Maybe 25 feet:
35.0Mbps, 35.1Mbps

At the end of the hallway is a bedroom. ~40ft:
97.7Mbps, 92.3Mbps

On the other side of the front of the hallway is a kitchen. ~40ft:
99.1Mbps, 118Mbps

On the other side of the room is another room. ~40ft:
91.8Mbps, 82.6Mbps

Now testing 3 rooms away, ~60ft:
68.5Mbps, 73.2Mbps

### Testing from the end of the house

This is a room at the very end of the ranch style house.

Testing to over halfway point in the house ~100ft:
51.0Mbps, 63.9Mbps

Testing to other side of the house ~130ft:
34.2Mbps, 38.9Mbps, 41.3Mbps

Testing to the electrical panel in the basement ~60ft:
137Mbps, 140Mbps

Testing to an outlet in the basement 20ft from the electrical panel (~80ft in total):
118Mbps, 119Mbps

Testing to an outlet in the basement 40ft from electrical panel (~100ft in total):
161Mbps, 162Mbps

Testing to that same outlet except we are going **through a surge protector**:
45.7Mbps, 44.6Mbps

Now testing to the garage electrical panel ~150ft:
57.1Mbps, 57.6Mbps, 58.5Mbps

Testing to the furthest outlet in the garage ~180ft:
19.2Mbps, 20.3Mbps

Same outlet but **with a surge protector**:
Dropped connection, 0.145Mbps, could not connect

### Basement Electrical Panel

Testing to the nearest outlet in the garage ~200ft:
72.8Mbps, 74.5Mbps

The end goal is to improve network performance in the garage, and I think this is as good as we are going to get. Test complete.

### Directly connecting the two
Ok I had one last idea... Let's directly connect the two of them to see if that can help us reach the advertised 100Mbps speeds:
323Mbps, 329Mbps

I don't know why these are advertised as "gigabit"...

Reading back through the material, on Amazon, it says the device has a "gigabit ethernet port", "gigabit powerline speeds", "AV1000 powerline speeds" (whatever that means).

On [TP-Link's website](https://www.tp-link.com/us/home-networking/powerline/tl-pa7017-kit/), they are much more specific. "[...] providing data transmissions of up to 1000Mbps over the electrical wiring for ranges up to 300m". However, there are multiple asterisks at the bottom of the page, with this one I believe being notable:

> ***Maximum Powerline signal rates are the physical rates derived from HomeplugAV/AV2 specifications. Actual Powerline data throughput and Powerline range are not guaranteed and will vary as a result of network conditions and environmental factors, including electrical interference, volume of traffic and network overhead, AFCI circuit breaker, and Powerline being located in a separate circuit.

But, the [specifications section](https://www.tp-link.com/us/home-networking/powerline/tl-pa7017-kit/#specifications) of their website has no mention of data transfer rate...

Ok, so our AV1000 is advertised as gigabit and they are not capabable of providing that speed. They have a **gigabit** ethernet port. But it is not capable of gigabit data transmission. However, TP-Link also makes an AV2000...

--------

On second thought, there may be filtering on the output of the powerline adapter, thus reducing the connectivity between the two whenever they were directly connected. I should have connected them both to the same outlet, but used an extension cord as they physically block each other from both being connected... Something [like this](https://amzn.to/4dEk7y8) would be perfect for this test.

### AV2000

The [AV2000 specification page](https://www.tp-link.com/us/home-networking/powerline/tl-pa9020p-kit/#specifications) states "Transmission speeds: powerline (physical layer data rate): up to 2000Mbps Ethernet: 10/100/1000 Mbps". Again, they aren't being terribly clear. It seems like it has 2x gigabit ethernet ports. Maybe it has the switching capacity to input 1000Mbps on one port and output 1000Mbps on the other port = "2000Mbps". However, I doubt that it is capable of 2000Mbps from one AV2000 to another AV2000 given my tests of the AV1000.

They also say it has beamforming??? This is a wired device. I do not know how it can perform any beamforming.

[This guy](https://old.reddit.com/r/HomeNetworking/comments/h8m6nz/real_world_speeds_with_powerline_networking/furyf9j/) says he's getting 500Mbps out of his AV2000s.

### TP-Link Support Article
[TP-Link says](https://www.tp-link.com/us/support/faq/2928/) that the powerline speed is 1000Mbps in an ideal environment. However, they caution that the "conversion rate" (the ratio of transmission rate and powerline rate) is about 30-35%, which depends on the electric wiring system. So, with the AV1000, we should expect to see 300-350Mbps at best. Which matches my tests.

Ethernet PHYs are advertised as theoretical maximum of 1000Mbps, which they do achieve. But that is total bits being sent over the wire. Not all bits are *data* bits. Some are overhead. A rule of thumb for ethernet is 920Mbps of throughput over a theoretical 1000Mbps link, or 92%.

### Powerline "false advertising"
From what I can understand, powerline devices advertise their "[maximum half-duplex PHY rate](https://www.reddit.com/r/HomeNetworking/comments/11okbba/what_is_the_speed_being_reported_via_powerline/jbszkz0/)". This is the maximum rate of raw bits being transferred between the two devices in ideal conditions. However, not every raw bit is user data.

headers, error correction, timing pauses, handshakes, sync frames, etc.

Brief tangent: As data is sent from one computer to another, it first makes its way through different layers of networking. Each layer might add some encapsulating information which results in additional data bits needing to be transferred. See the [TCP/IP Model](https://www.geeksforgeeks.org/tcp-ip-model/) or [OSI Model](https://www.geeksforgeeks.org/open-systems-interconnection-model-osi/) for additional information.

As an example, HTTPS at layer (4 TCP/IP) [adds ~800bytes of header information](https://stackoverflow.com/a/5358276).

As a simplified example TCP at layer (4 OSI, 3 TCP/IP) adds between 20-60 bytes of header information to make sure each packet gets received and if not, resent. IP at layer (2 TCP/IP) adds 20-60bytes to make sure the packet is able to be routed across the world. Ethernet frames at layer (2 OSI, 1 TCP/IP) typically have a maximum data size of 1500 bytes (jumbo frames change this) but they also add 18-bytes of header information and they make sure the packet arrives at the correct computer and network interface (WiFi/ethernet).

So, in total we have 40 bytes + 40 bytes + 18 bytes of headers = 98bytes of headers. Given we are sending 1500bytes of data, that gives us an efficiency of ~94%. So, if we are operating over a 100Mbps link, we should expect to see data throughput of ~94Mbps.


WiFi typically gets throughput of 80% of link speeds: https://community.tp-link.com/en/home/forum/topic/581704

Wikipedia says standard frame size efficiency of TCP/IP is 95%: https://en.wikipedia.org/wiki/Jumbo_frame#Bandwidth_efficiency


In a [typical TCP packet](https://www.geeksforgeeks.org/tcp-ip-packet-format/), you have bits that specify where this packet goes and who it is from, a checksum to help notice if any of the data bits are incorrect, etc. TCP/IP headers are between 20-60bytes.

### Additional Reading
A good, longish, and somewhat technical article [here](https://micoolpaul.com/2023/07/10/how-to-actually-increase-powerline-adapter-throughput/) for how to improve powerline thoughput.



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
