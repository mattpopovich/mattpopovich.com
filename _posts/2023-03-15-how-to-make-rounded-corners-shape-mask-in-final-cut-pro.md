---
title: "How to Make Rounded Corners (Shape Mask) in Final Cut Pro"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2023-03-15 23:40:42 -0600
categories: [Blog, YouTube]    # <=2 values here: top category and sub category
tags: [apple, how to, mac, video editing, tech, tutorial, final cut pro, fcpx]  # TAG names should always be lowercase
layout: post                # post is the default, we will set it to be explicit
pin: false
toc: true                   # Table of contents
comments: true              # Enable/disable comments at the bottom of the post
math: false                 # Disabled by default for performance reasons
mermaid: false              # Diagram generation tool via ```mermaid [...]```
#img_cdn: https://cdn.com
#media_subpath:
image:
  path: /assets/img/posts/2023-03-15-how-to-make-rounded-corners-shape-mask-in-final-cut-pro/rounded-corners-shape-mask-fcpx-thumbnail.jpg
#  width: 100   # in pixels
#  height: 40   # in pixels
#  alt: image alternative text
  show_image_in_post: false
description: Making rounded corners in FCPX is very simple to do but I couldn't find any simple tutorials, so I made one!
---

{% include embed/youtube.html id='5dp_S5vU_xI' %}

## Intro
Ok, super quick post here. I'm working in [Final Cut Pro (FCP/FCPX)](https://www.apple.com/final-cut-pro/) and I want to be able to put a screenshot or another clip in my video and I don't like the super sharp corners of the video that happens with the default overlay. I'd like them to be a little more soft and rounded. I did some Googling to try to figure out how to do this and the first couple of links weren't terribly obvious with their solutions... but there is an easy solution (apply a shape mask) and I'm going to show you how to do it!

| Original | Rounded Corners |
|:---------------:|:---------------:|
|![Example of video overlay](/assets/img/posts/2023-03-15-how-to-make-rounded-corners-shape-mask-in-final-cut-pro/FCPX_videoOverlayWithoutMask.jpg)  |  ![Video overlay with rounded corners (shape mask)](/assets/img/posts/2023-03-15-how-to-make-rounded-corners-shape-mask-in-final-cut-pro/FCPX_videoOverlayWithMask.jpg)|

## [TL;DR](https://www.merriam-webster.com/dictionary/TL%3BDR)
1. Click and drag a Shape Mask from the Effects Browser to your desired clip
    * ⌘5 to bring up the Effects Browser
2. Modify the Shape Mask to your liking
    * Click and drag on the Shape Mask in the viewer to move it around + adjust height and width
    * In the Inspector, modify the Shape Mask's feather value
      * ⌘4 to bring up the Inspector

## Applying a Shape Mask
In FCPX, on the bottom right, click on *Show or hide the Effects Browser* (or press ⌘5)

![How to bring up the "Effects Browser"](/assets/img/posts/2023-03-15-how-to-make-rounded-corners-shape-mask-in-final-cut-pro/FCPX_showOrHideTheEffectsBrowser.png){: .shadow }
*How to bring up the "Effects Browser"*

Then, search for a "mask" **Video** Effect. This will bring up a draw mask, graduated mask, image mask, shape mask, and vignette mask. The draw mask is more for custom shapes that you want to be able to *draw* yourself. The shape mask is specifically meant for what we're trying to do (those are the two that I'm familiar with). You'll drag the **shape mask** onto our clip and you'll see that it gets pretty close to what we were looking for.

## Configuring the Shape Mask
Now that we have the shape mask applied, there's a few tweaks that I want to point out. For starters, you can click and drag on the shape mask in the viewer to move it around. You can drag the sides for the width and height of the mask. You can do the same thing in the "Inspector" (bring up the inspector window with ⌘4)

The big thing to point out in the Inspector is the "Feather" option for the Shape Mask. The *Feather* changes how hard or soft the edges of the shape mask fall off.

## Potential Pitfalls
The only other thing I'll comment on is you can somewhat "lose" the mask... If the "Shape Mask" isn't selected in the Inspector, you won't be able to click and drag and modify the shape mask in the viewer.

And this makes sense, for example, if you had many different clips and effects running around in the viewer, it could be hard to select the one effect that you wanted. This explicitly makes it clear which effect you are selecting and modifying.

**However**, even if you select the Shape Mask in the Inspector, there is a chance that you still won't be able to click and drag the Shape Mask in the viewer to modify it. If you want to be able to modify the Shape Mask in the viewer, you need to make sure "Show Shape Mask onscreen controls" is selected in the Shape Mask section in the Inspector.

![How to "Show Shape Mask onscreen controls"](/assets/img/posts/2023-03-15-how-to-make-rounded-corners-shape-mask-in-final-cut-pro/FCPX_showShapeMaskOnscreenControls.jpg){: .shadow }
*How to "Show Shape Mask onscreen controls"*

## Outro
That's about all there is to the Shape Mask. Feel free to customize and mess around with it. I will leave the other parameters of the Shape Mask Inspector as an [exercise for the reader](http://www.mathmatique.com/articles/left-exercise-reader) 😉

Hope this helps!

<!-- TODO: Could not find "Sweet Tea" by Travis Loafman anyhere -->
