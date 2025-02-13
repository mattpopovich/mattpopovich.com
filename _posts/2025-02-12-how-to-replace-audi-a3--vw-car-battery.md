---
title: "How to Replace Audi A3 / VW Car Battery"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2025-02-12 17:41:20 -0600
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
#   width: 100   # in pixels
#   height: 40   # in pixels
#   alt: image alternative text
#   show_image_in_post: false
#description:               # A short sentence to describe the article, used when sharing links on social media and on homepage
---

## TODO: Add Heading Here
TODO: Add text here


## Identifying the Problem
My car battery was so dead that I had no electronics in the car, could not adjust the seat, the car would not attempt to start, and I couldn't even lock it. I knew it wasn't an issue with my remote because the light on the remote lit up whenever I tried to lock the vehicle.

All the above points to a dead car battery, but if you really want to be sure, you can grab a multimeter and test the voltage of the battery. Mine was reading about 2.8V which is **woefully low**. "[Car batteries have 6 cells and each cell is at 2.1V fully charged](https://youtu.be/h7rTcBanpMk?t=350)". They're connected in series and thus, **a fully charged car battery should read at or above 12.6V**. As an example, my new car battery reads 12.67V from the shop.

### Testing a Car Battery's Health
If you're testing your car battery's voltage to see how healthy it is, let it sit overnight then test it. This way it isn't freshly charged from the alternator during a drive. Additionally, cold weather is tougher on batteries and will cause a lower voltage reading.

| Voltage (V) | Remaining life (approx.) |
|-------------|--------------------------------|
| 12.6+ | 100% |
| 12.5 | 90% |
| 12.42 | 80% |
| 12.32 | 70% |
| 12.2 | 60% |
| 12.06 | 50% |
| 11.9 | 40% |
| 11.75 | 30% |
| 11.58 | 20% |
| 11.31 | 10% |
| 10.5 | 0% |

<my-caption><a href="https://www.autozone.com/diy/battery/what-you-need-to-know-about-car-battery-voltage">Source</a></my-caption>

> Testing the voltage of a battery is a good *approximation* to its remaining life. A [load test](https://www.youtube.com/watch?v=tsJUuLu1cw0) would be the proper test for your battery's health.
{: .prompt-warning }


## Purchasing a New Battery
For an Audi A3, you'll need a battery with a group size of H6.

[This video tested](https://youtu.be/h7rTcBanpMk?t=568) multiple different battery brands and their performance. TLDW: The [Everstart from Walmart](https://www.walmart.com/ip/EverStart-Maxx-Lead-Acid-Automotive-Battery-Group-Size-H6-LN3-48-12-Volt-750-CCA-115-RC/144301475) was the cheapest battery the video tested and it actually performed the best as well. Sold! A complete chart of their testing is below:

![Colored chart image of the table from above](/assets/img/posts/2025-02-12-how-to-replace-audi-a3--vw-car-battery/battery_comparison_chart.png)
*[Source](https://youtu.be/h7rTcBanpMk?t=568), sorted by CCA at 0°F (higher is better)*

<details markdown="1">
  <summary> Click to show a text table of the chart from above</summary>

  | Brand                 | Retailer     | Price   | Manufacturer     | Type               | Advertised CCA | 0°F CCA | \-20°F CCA |      | 0°F CCA/$ | \-20°F CCA/$ |
  | --------------------- | ------------ | ------- | ---------------- | ------------------ | -------------- | ------- | ---------- | ---- | --------- | ------------ |
  | Interstate            | Costco       | $92.99  | Johnson Controls | Flooded Lead Acid  | 810            |         |            |      |           |              |
  | Everstart             | Walmart      | $119.76 | Johnson Controls | Flooded Lead Acid  | 810            | 766     | 708        |      | 6.40      | 5.91         |
  | Duralast Gold         | Autozone     | $159.99 | Johnson Controls | Flooded Lead Acid  | 810            | 753     | 708        |      | 4.71      | 4.43         |
  | Super Start Premium   | O’Reilly     | $139.99 | East Penn Mfg.   | Flooded Lead Acid  | 840            | 745     | 683        |      | 5.32      | 4.88         |
  | Autocraft Silver      | Advance Auto | $139.99 | Johnson Controls | Flooded Lead Acid  | 800            | 725     | 651        |      | 5.18      | 4.65         |
  | Optima RedTop         | Amazon       | $224.99 | Johnson Controls | Absorbed Glass Mat | 800            | 751     | 629        |      | 3.34      | 2.80         |
  | Diehard Advanced Gold | Amazon       | $189.99 | Enersys          | Absorbed Glass Mat | 775            | 697     | 580        |      | 3.67      | 3.05         |

</details>

&nbsp;

I [purchased the Everstart](https://www.walmart.com/ip/EverStart-Maxx-Lead-Acid-Automotive-Battery-Group-Size-H6-LN3-48-12-Volt-750-CCA-115-RC/144301475) as it was the best performing (and cheapest) that was tested. They did not test an [Interstate battery from Costco](https://costco.interstatebatteries.com/results?key=auto&Program=100500&ZipCode=75254&l=75254&Country=United%20States&year=2469235&make=2469279&model=2469293&engine=2469294&option=2469296), but as it is made from the same manufacturer and has the same CCA (cold cranking amps) rating as the Everstart that was tested, I'd wager it would perform very similarly to the Everstart. And given that it was 22.5% cheaper, if I had a Costco membership, I would have bought that one.

> Note that prices are as of 2020 and the CCA listed won't match our Audi's battery. The batteries they tested had a group size of 27 vs. Audi A3's group size of H6.
{: .prompt-info }


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
