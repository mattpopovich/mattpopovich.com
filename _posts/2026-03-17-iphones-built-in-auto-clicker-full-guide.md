---
title: "iPhone's Built-in Auto Clicker: FULL GUIDE"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2026-03-17 21:52:18 -0600
categories: [Blog, TODO]    # <=2 values here: top category and sub category
tags: [apple, how to, tech, tutorial, youtube, ios, iphone, ipad]                # TAG names should always be lowercase
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

|                                                           | Switch Control                                       | Voice Control                          |
| --------------------------------------------------------- | ---------------------------------------------------- | -------------------------------------- |
| How to enable                                             | Triple click home or side button                     | 🗣️ "Hey Siri, turn on voice control"    |
| Recipes can be made while <br> target app is on screen    | No                                                   | Yes ✅                                  |
| Maximum recording time                                    | 60s                                                  | Unlimited? <br> I've tested up to 5min |
| Able to run in noisy environments                         | If a non-voice switch is used ✅                      | Can be difficult                       |
| Can stop recipe once one is started                       | No                                                   | No                                     |
| Touch screen is responsive <br> while recipes are running | If a non-screen switch<br>is used                    | Yes ✅                                  |
| Number of times you can <br> repeat a recipe              | Unlimited? <br>I've tested up to 500                 | 2 - 99                                 |
| Can stop repeated recipes <br> once one of them finishes  | No. Must wait for all repeated <br>recipes to finish | Yes ✅                                  |

I'll let you decide which one is best for your use case. If you just need to spam click one area on the screen, either would work. If you need something a little more complex, I'd recommend voice control because you can make the recording while any app is open.

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
         - See [Other Switches for Switch Control](#other-switches-for-switch-control) to activate this switch with something other than a screen tap, which will allow you to use the screen while the "action" is running
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

### Switch Control Further Explanation

A switch (tap screen, back tap, make a sound, etc.) will perform an action (scroll, home button, change volume, launch shortcut, etc.). Makes sense.

Now, a recipe, whenever it is active, will overwrite the action for any switches that you define. Recipes also have a different action set for switches. Specifically of use for auto clickers is the action "custom gesture", which is only available in recipes.

---

The "tap" action that we select for our switch action (step 2 in [Setting up Switch Control](#setting-up-switch-control)) is effectively performing a "select item" whenever Switch Control performs scanning. It's not actually "tapping" on the screen. This is also mostly irrelevant to us, because we overwrite this action once we set a "custom gesture" for this switch in our recipe.

So if our recipe is active, the switch will perform our "custom gesture". If the recipe is not active, the switch will perform a "tap".

We make the recipe active whenever we set it to launch by default in Settings > Accessibility > Switch Control > Recipes > Launch Recipe.

### Other Switches for Switch Control

Whenever we had the switch's source be "screen", that made the switch easy to activate but at the expense of any tap of the screen activates the switch + we cannot use the screen while the action is happening.

If we instead have the switch source be something else (my favorites are Back Tap > Double Tap and Sound > Sh), this will allow us to use the screen while the action is running.

![My app, SketchFade, in action](/assets/img/posts/2026-03-17-iphones-built-in-auto-clicker-full-guide/SketchFadePreview_LQ.m4v){: width="200" .shadow .right}
<!-- TODO: Would be nice to be able to pause this -->

### Debugging

While playing around with these, I found things a little tricky to debug... so I fixed that by making an app! It's called [SketchFade](https://apps.apple.com/app/sketch-fade/id6760681226) (visual on the right) and it's basically a sketch application where after a configurable amount of time, the sketch will fade away. There's also a resettable counter that will count how many times the screen has been touched. It's currently 99¢ in the App Store, but if you guys can [get me to 1,000 subscribers](https://www.youtube.com/@mattpopovich?sub_confirmation=1), **I will make the app free**.

If you're interested in this, leave a comment below letting me know and I'll comment back once I hit 1,000 subscribers and make the app free. Also, if you can think of a better name for the app, also let me know of that in the comments!

### "Trimming" Empty Space
Both voice control and switch control "trim" empty space before the first tap and after the last tap

Example: if your recipe looks as such (with `*` representing taps):
```
[*    * *    ***   *               ]
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

<u>Voice control</u>: Saying "turn off voice control" will exit **after** the current recipe finishes. Until then, you can lock the screen, tap the screen to interact with it, or even say "reboot device" if you are in a major pickle.

<u>Switch control</u>: Impossible to stop recipes once they are started or they are queued to repeat. Tapping the screen will only make it worse by repeating the recipe (if you are using a [screen switch](#other-switches-for-switch-control)). My advice is to triple click your home/power button to disable switch control, then lock the screen and wait it out.

### Recipes are "designed to be temporary"
> "[You can also assign recipes—a set of temporary, specialized actions—to your switches.](https://support.apple.com/guide/iphone/set-up-and-turn-on-switch-control-iph400b2f114/ios)"

I guess this is why Apple doesn't let you exit in the middle of recipes running?+

### Hiding the "Invalid Configuration" Pop Up

If you get tired of seeing

> Invalid Configuration<br>
> Triple-click the side button<br>
> to stop Switch Control

You can hide this by going to Settings > Accessibility > Switch Control > Alerts > Ignore Invalid Switch Setup

> It is difficult/impossible to tell when Switch Control is enabled/disabled if you do disable this alert
{: .prompt-warning }



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
