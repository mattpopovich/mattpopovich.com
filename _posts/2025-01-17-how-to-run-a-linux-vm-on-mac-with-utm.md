---
title: "How to Run a Linux VM on Mac with UTM"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries # change to 18:32:08
date: 2025-01-17 11:32:08 -0600
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

## Intro
I did this a few years ago because I needed docker to access a USB device, but docker for Mac somehow does not have that capability... ([GitHub issue created in 2016](https://github.com/docker/for-mac/issues/900) 🤕)...  So I installed Ubuntu in a virtual machine with the help of UTM and it worked great. I have found myself needing a Linux VM once again, so I figured it would be a good time to document the installation process!

## What is UTM?
> "UTM is a full featured system emulator and virtual machine host for iOS and macOS. [...] In short, it allows you to run Window, Linux, and more on your Mac, iPhone, and iPad."

- [UTM Documentation](https://docs.getutm.app/)

## Installing UTM
Good video tutorial [here](https://www.youtube.com/watch?v=JrNS3brSnmA).

Go to [mac.getutm.app](https://mac.getutm.app/), either download the installer (free) or get it on the Mac App Store ($10, identical but comes with automatic updates + helps support the developers). If you download the installer, follow the typical Mac app installation process (open the `.dmg`, drag the application into the `Applications` folder).

## Creating a VM
I'm going to be installing Ubuntu for my Linux VM. If you have a M1, M2, etc. Mac, I'd recommend downloading [Ubuntu for ARM](https://ubuntu.com/download/server/arm). This will give you the best performance as M1, M2, etc. Macs are an ARM platform. If you have an Intel-based Mac, you should download the typical [Ubuntu Desktop](https://ubuntu.com/download/desktop).

Once downloaded, open the UTM application.
* Click on "Create a New Virtual Machine"
* "Virtualize"
* "Linux"
* Leave the settings as default, browse for the "Boot ISO Image" and select the `*.iso` file that you just downloaded, click "Continue"
* Select the amount of Memory and CPU cores that you desire
  * I'll be allocating 2048MB of RAM and 2 CPU cores
* Select the size of hard drive
  * I'll be allocating 32GiB
* Select a shared directory (if desired)
* Review the summary and click "Save"

You should now see your VM on the sidebar of the UTM app. Click "Play" and let it boot up!

Upon boot, select "Try or Install Ubuntu Server". Then go through the prompts to finish installation.
* English
* Continue without Updating
* Done (English (US))
* Done (Ubuntu Server)
* Done (Default network configuration)
* Done (Blank proxy address)
* Done (Default mirror address)
* Done (Use an entire disk)
  * This is the 32GiB disk that I created above
* Done (Default storage configuration)
* Continue (Begin the installation process and wipe the 32GiB virtual "hard drive" that we allocated above)
* Fill out the profile configuration and click "Done"
  * Your name: user
  * Your servers name: ubuntu-server
  * Pick a username: user
* Continue (Skip Ubuntu Pro)
* Done (I did not install OpenSSH server)
  * All the files I will be accessing will be done via a shared folder, so I don't foresee any need to SSH
* Done (I did not install any featured server snaps)
* Let the installation run...
  * 30 seconds or so on my M1 Mac
* Reboot Now
  * You will likely then end up at a black screen with a blinking cursor.
  * Click on the backwards play arrow (top left) to reboot the machine.
    * You'll get a prompt "This will reset the VM and any unsaved state will be lost". That sounds scary, but just click "OK".
* You will likely then end up at the original "Try or Install Ubuntu Server" screen.
  * Power off the VM (power icon on the top left)
    * You'll get another scary prompt "This may corrupt the VM and any unsaved changes will be lost". Click "OK".
* Close the Linux UTM window, go back to the main UTM window
* Select our new Linux VM on the left sidebar, scroll down, click on CD/DVD, click "Clear".
  * This will effectively "eject" the Ubuntu installer `.iso`/CD.
* Click "Play" on our Linux VM
* You'll get a prompt asking you for the username password you created earlier, enter it

## Configuring the VM

At this point, this is just a server with a terminal environment. To get a GUI ([Graphical User Interface](https://en.wikipedia.org/wiki/Graphical_user_interface)), we'll need to install a package or two.

> Unfamiliar with the terminal? [Check out my post here for an introduction](posts/introduction-to-the-command-line-shell-terminal-etc/)
{: .prompt-info }

We will be using GNOME for our desktop environment. Start by installing `tasksel` followed by `ubuntu-desktop`:
```console
$ sudo apt install tasksel -y
[...]
$ sudo apt install ubuntu-desktop
[...]
Need to get 649MB of archives.
After this operation, 2,330 MB of additional disk space will be used.
Do you want to continue? [Y/n]: y
[...]
```

This will download and install ~650MB and will largely depend on your internet speed. Expect a few minutes at the minimum.

Once complete, let's reboot the VM to experience the new desktop environment

```console
$ sudo reboot now
```

Upon reboot, you might see a "Display output not active". Be patient for about a minute. You will then see a login GUI that resembles Ubuntu for desktop.

Log in and go through the setup prompts...

## Enabling shared folders

```console
$ sudo apt install spice-webdavd
```

Reboot the VM by clicking on the power button in Ubuntu (not UTM) in the top right. Once powered down, go back into UTM to change some settings. If the status of the VM isn't "Stopped", close UTM and reopen it. Once the status is stopped, we can right click our Linux VM on the left bar of UTM, then click "Edit". Go to "Sharing", then change our "Directory Share Mode" to "SPICE WebDAV". Click "Save" in the bottom right, then start our VM up again by clicking on the play button.

TODO: We may want to enable "Retina Mode" in the display settings here.

Upon reboot open the "Files" (left side of Ubuntu, looks like a folder), go to "Other Locations" (bottom left side of Files), then click on "Spice client folder". You will then see a new folder appear, double click that to view your shared folder.

You can also do this manually in a terminal.

```console
$ sudo apt install davfs2
```
Then allow unprivileged users I guess??




TODO: Maybe simply the mounting point? It currently gets mounted at `/run/user/1000/gvfs/dav+sd:host=Spice%2520client%2520folder._webdav._tcp.local`. Something like

We can then mount via

```console
$ cd
$ pwd
/home/user
$ mkdir SharedFolder
$ sudo mount -t davfs -o noexec http://127.0.0.1:9843/ /home/user/SharedFolder/
```

Will want to follow these instructions to fix `SharedFolder` permissions: [[https://docs.getutm.app/guest-support/linux/#fixing-permission-errors]]



## Viewing synology encrypted folders
Then, we can create our mount:

```console
$ cd ~/SharedFolder
$ ls
ECRYPTFSxxxxx
ECRYPTFSxxxxx
ECRYPTFSxxxxx
$ mv ECRYPTFSxxxxx FUT/
$ sudo mount -t ecryptfs FUT/ decryptedFUT/
```

Now, anything you put into FUT will appear in decryptedFUT + is decrypted!







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
