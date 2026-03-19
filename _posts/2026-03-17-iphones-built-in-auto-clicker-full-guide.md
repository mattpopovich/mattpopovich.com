---
title: "iPhone's Built-in Auto Clicker: FULL GUIDE"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2026-03-17 21:52:18 -0600
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
There's a bunch of iOS auto clicker videos online, but for whatever reason... they're all kinda trash. They all just repeat the same things and show you how to set it up but no one really shows it in use or explains how it works. Alas, you can [rest here weary traveler](https://knowyourmeme.com/memes/rest-here-weary-traveler), [for your search of an iOS auto clicker tutorial is complete](https://www.youtube.com/watch?v=LJY1uzNha1k).

## Switch Control vs. Voice Control
There are two main ways that iOS lets you create an auto clicker: [voice control](https://support.apple.com/guide/iphone/use-voice-control-iph2c21a3c88/ios) or [switch control](https://support.apple.com/guide/iphone/intro-to-switch-control-iphc9d32b862/ios). The main difference between the two are that voice control uses your voice to... control it. Switch control uses taps on the screen and button presses.

Additionally, voice control lets your record screen taps while the app of interest is open, switch control is just a blank screen where you have to remember where on the screen your taps need to be.

Lastly, voice control lets you interact with the screen while it is running while switch control completely disables the touchscreen while it is running.

### Comparison Table

|                                                          | Voice Control                            | Switch Control                                       |
| -------------------------------------------------------- | ---------------------------------------- | ---------------------------------------------------- |
| How to enable                                            | 🗣️ "Hey Siri, turn on voice control"      | Triple click home or <br> side button                |
| Maximum recording time                                   | Unlimited? <br> I've tested up to 5min ✅ | 60s                                                  |
| Able to run in noisy environments                        | Can be difficult                         | Yes ✅                                                |
| Can stop recipe once one is started                      | No                                       | No                                                   |
| Touch screen is responsive <br> once recipes are ran     | Yes ✅                                    | No                                                   |
| Number of times you can <br> repeat a recipe             | 2 - 99                                   | Unlimited? <br>I've tested up to 500                 |
| Recipes can be made while <br> target app is on screen   | Yes ✅                                    | No                                                   |
| Can stop repeated recipes <br> once one of them finishes | Yes ✅                                    | No. Must wait for all repeated <br>recipes to finish |

I'll let you decide which one is best for your use case. If you just need to spam click one area on the screen, either would work. If you need something a little more complex, I'd recommend voice control.

## Setting up [Voice Control](https://support.apple.com/guide/iphone/use-voice-control-iph2c21a3c88/ios)

   1. Settings > Siri / Apple Intelligence & Siri > Talk (& Type) to Siri
      1. Enable Siri
   2. Open whatever app you want to run the auto clicker in
   3. Activate Siri, then 🗣️ "turn on voice control"
   4. 🗣️ "Start recording gestures"
   5. \*Perform taps\*
   6. 🗣️ "Stop recording gestures"
   7. Add a name for the command to reply your recorded gestures, Ex. "auto click"
   8. 🗣️ "auto click"
      - Want to repeat? 🗣️ "Repeat 2 times"
   9. 🗣️ "turn off voice control"
      - This will turn off voice control at the **end** of the current recipe

## Setting up [Switch Control](https://support.apple.com/guide/iphone/intro-to-switch-control-iphc9d32b862/ios)

   1. Settings > Accessibility > Accessibility Shortcut
      1. Check switch Control **only**
   2. [Settings > Accessibility > Switch Control > Switches](https://support.apple.com/guide/iphone/set-up-and-turn-on-switch-control-iph400b2f114/ios)
      1. Add New Switch... > Screen > Full Screen > Under "System" choose Tap
   3. Settings > Accessibility > Switch Control > Recipes
      1. Create New Recipe...
      2. Give it a Name, Ex. "auto click"
      3. Assign a Switch... > Full Screen > Custom Gesture
      4. Tap the screen exactly how you want your auto clicker to perform
      5. Save (top right)
   4. Settings > Accessibility > Switch Control > Recipes
      1. Launch Recipe > select the name of the recipe you just created
         - Set this to "None" the first time you launch switch control so that you can make a selection on the popup. Afterwards, you can set this to your custom recipe.
   5. Triple click [side button](https://support.apple.com/en-us/105103) (which turns off or locks phone), or physical home button if you have it
   6. Tap the screen once to run the recipe once
      - Want to repeat? Tap the screen multiple times
         - **WARNING**: You cannot exit until all the repeated recipes finish
         - Not sure what the maximum amount is, I've confirmed it will work at least up to 500 times
   7. Triple click the side button (or physical home button) to exit switch control

## Notes

### "Trimming" Empty Space
Both voice control and switch control "trim" empty space before the first tap and after the last tap

Example: if your recipe looks as such (with `*` representing taps):
```
[    *    * *    ***   *     ]
```
Apple will "trim" that recipe into:
```
[*    * *    ***   *]
```
So if you repeat the recipe, it will look like:
```
[*    * *    ***   *][*    * *    ***   *]
```
Be aware of the "double tap" that will occur between the first recipe ending and the second recipe starting.

### Exiting Recipes While They Are Running

Voice control: You can lock the screen, tap the screen, say "reboot device"

Switch control: Impossible to stop once started. Tapping the screen will only make it worse by repeating the recipe. My advice is to triple click your home/power button, then lock the screen and wait it out.

### Recipes are "designed to be temporary"
> "[You can also assign recipes—a set of temporary, specialized actions—to your switches.](https://support.apple.com/guide/iphone/set-up-and-turn-on-switch-control-iph400b2f114/ios)"

I guess this is why Apple doesn't let you exit in the middle of recipes running?

## Outro
I'd recommend starting small. Make small recipes to get the hang of things, then learn how to repeat them, and build from there.

Voice control and switch control are very powerful. But, [with great power, comes great responsibility](https://youtu.be/guuYU74wU70?t=70). 💭




## Tags
No jailbreak, no computer needed, no additional apps, no download, free, games, tweak, osrs, tiktok, evony, whiteout survival,

Roblox, Runescape, Pokemon Go,

fortnite, among us!, Brawl stars, Clash Royale, PUBG, bloons,





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
