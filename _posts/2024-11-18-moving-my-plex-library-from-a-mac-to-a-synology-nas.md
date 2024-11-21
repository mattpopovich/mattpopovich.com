---
title: "Moving My Plex Library from a Mac to a Synology NAS"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2024-11-18 14:22:47 -0600
categories: [Blog, Not YouTube]    # <=2 values here: top category and sub category
tags: [apple, bash, how to, mac, not youtube, osx, tech, tutorial, plex, synology, nas, docker, docker compose, rsync]                # TAG names should always be lowercase
layout: post                # post is the default, we will set it to be explicit
pin: false
toc: true                   # Table of contents
comments: true              # Enable/disable comments at the bottom of the post
math: false                 # Disabled by default for performance reasons
mermaid: false              # Diagram generation tool via ```mermaid [...]```
#img_cdn: https://cdn.com
#media_subpath: /img/path/
image:
 path: /assets/img/posts/2024-11-18-moving-my-plex-library-from-a-mac-to-a-synology-nas/plex-macbook-to-synology-nas.jpg
#  width: 100   # in pixels
#  height: 40   # in pixels
 alt: Image is AI-assisted. The Synology NAS is an AI creation and not a real model for sale.
description: A detailed walkthrough of the steps I took to move my Plex Media Server from a Mac to a Synology NAS
---

<!-- TODO: Add YouTube video link here -->

> This tutorial assumes you have some [basic knowledge of the command line/terminal](/posts/introduction-to-the-command-line-shell-terminal-etc/) and [`ssh`](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server)ing into a machine to run commands. Docker familiarity is helpful as well, but I'll explain the `docker compose` commands we'll be running if you're unfamiliar.
{: .prompt-warning}

## Intro

### What is this post about?
This post documents my experience moving my [Plex](https://www.plex.tv/) server from my MacBook to a [Synology NAS](https://www.synology.com/dsm/solution/what-is-nas/for-home) (network attached storage). The Plex server was installed using the [Mac Plex app](https://www.plex.tv/media-server-downloads/?cat=computer&plat=macos) (`.dmg`) and I will be transitioning to docker on the Synology NAS to make future moves (if necessary) much easier due to docker being operating system independent.

I use [Tautulli](https://tautulli.com/) for Plex statistics, so I will also be moving that from the Mac (running via Python) to a docker container on the Synology NAS as well. I've documented that in a separate blog post [here](/posts/moving-tautulli-from-a-mac-python-to-a-synology-nas-docker/).

> Note that this post is not meant to be an endorsement of Synology. While I do use one of their machines and like it, I can't say I agree in the direction the company is moving... Removing features ([video station](https://www.youtube.com/watch?v=D4YLeTQXICY)), [requiring Synology-branded hardware](https://www.reddit.com/r/synology/comments/1f310mx/end_of_video_station_no_more_synology/lkb066q/) (RAM, HDDs), etc.
>
> There isn't another system that I would currently recommend over them, but I think they should be purchased with caution.
{: .prompt-info }

### What is Plex?
Plex is an server/client utility that lets you host your own music, pictures, videos, live TV, etc. and view/download them on any device with a streaming service-esque app. You can think of it as your own custom [Netflix](https://www.netflix.com/)! Here are the main steps to get it up and running:
1. Download and install the Plex server onto a computer. This computer will be the host of your content.
    * Note that you can only stream and download your content when this computer is powered on and connected to your network/the internet.
2. Copy all of the content that you want to stream/download onto your host computer
3. Tell Plex which folder your content is in
4. Download the Plex app or navigate to [plex.tv](https://www.plex.tv) onto your client (phone, TV, tablet, etc.)
5. Login on the client and stream/download your content!

### Why move to a NAS?
I previously hosted my Plex server on a MacBook that was constantly powered on and plugged in. My Mac was old (2012) so it struggled to decode the newer video codecs (H.265/HEVC) + leaving it plugged in all the time isn't great on its battery (use [AlDente](https://apphousekitchen.com/) if you leave your Mac constantly charging). I also had all of my content on an external hard drive so in the event of a disk failure (can happen randomly as drives get older), I would have lost all my content. Sure, I could have made a backup but it can be annoying to constantly keep the backup up to date.

My solution: buy a NAS (network attached storage). Why? A NAS is a:
* Computer that is designed to be a server (always on)
* Accepts hard disks (HDDs) that are designed to be always on ([NAS hard drives](https://amzn.to/40EWG3v))
* Automatically supports RAID (redundant array of independent (or inexpensive) disks)
  * RAID automatically duplicates your data on multiple disks such that, in the event of a disk failure, your data is not lost

### Additional reasons to get a NAS
* Easily expandable storage once a hard drive gets full (just plug another one in!)
* A place to host [Time Machine](https://support.apple.com/en-us/HT201250) backups of your Mac (or other machines)
* A place to host storage that can be easily accessible from multiple machines
  * Think of it as your own personal cloud (with no monthly fees)
* A computer that is always on and online to run any scripts you might need
  * You could host your own VPN through your NAS to protect your network traffic when connecting to unsecured hotspots, get around location restrictions, etc.
* [And more](https://www.synology.com/dsm/solution/what-is-nas/for-home)

## [TL;DR](https://www.merriam-webster.com/dictionary/TL%3BDR)
<details markdown="1">
  <summary>Know your stuff? Click here to see the main points with minimal explanation (<a href="https://support.plex.tv/articles/201370363-move-an-install-to-another-system/">Ref.</a>)❗️❗️</summary>

  * Disable the `Empty trash automatically after every scan` option by clicking the [settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right in Plex on web) —> Library (under Settings)
  * Shut down your Plex Media Server
  * [Back up your Plex media server data](https://support.plex.tv/articles/201539237-backing-up-plex-media-server-data/)
    * Your Plex Media Server (PMS) data location can be found [here](https://support.plex.tv/articles/202915258-where-is-the-plex-media-server-data-directory-located/)
      * `~/Library/Application Support/Plex Media Server/` for macOS.
    * Additional Plex settings can be found [here](https://support.plex.tv/articles/201539237-backing-up-plex-media-server-data/)
      * `~/Library/Preferences/com.plexapp.plexmediaserver.plist` for macOS.
      * I did not restore this file as Plex on Linux uses a `Preferences.xml` for additional Plex settings and converting between the two formats seemed like a hack. I decided to start fresh as ["the vast majority of users will never need to alter these settings"](https://support.plex.tv/articles/201105343-advanced-hidden-server-settings/).
  * Install [container manager](https://www.synology.com/en-us/dsm/feature/docker) onto Synology NAS
  * Make a `plex` folder in the `/docker` folder
    * In the `plex` folder I made 3 more folders: `config`, `data`, `transcode`.
  * Start copying over Plex data to `/docker/plex/data/*`
  * Create a docker compose file: `plex-pms-docker-compose.yaml` from [this template](https://github.com/plexinc/pms-docker/blob/master/docker-compose-host.yml.template)
    * Set the `TZ` (timezone) environment variable
      * Ex. `TZ='America/Denver'`
      * Find valid options [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
    * Set the `PLEX_CLAIM` environment variable which connects your docker instance to your Plex account
      * Ex. `PLEX_CLAIM=claim-xxxxxxxxxxxxxx-xxxxx`
      * Get your plex claim value from [plex.tv/claim](https://www.plex.tv/claim/)
    * Mount `config`, `data`, and `transcode` into the docker container
      *  `- /volume1/docker/plex/config:/config`
      *  `- /volume1/docker/plex/transcode:/transcode`
      *  `- /volume1/docker/plex/data:/data`
  * Run the docker container using docker compose:
    * `sudo docker-compose -f plex-pms-docker-compose.yaml up -d`
  * For each of our libraries (in Plex on NAS), [update the location of media files](https://support.plex.tv/articles/200289266-editing-libraries/)
    * For each library, add a new media folder
    * "Scan Library Files" for each library
    * After confirming the files in your library point to the new location, delete the library's reference to the old location
  * [Empty the library trash](https://support.plex.tv/articles/200289326-emptying-library-trash/)
    * Enable the "Empty trash automatically after every scan" [library option](https://support.plex.tv/articles/200289526-library/), if you originally disabled it.
  * [Clean Bundles](https://support.plex.tv/articles/226836308-help/)
  * [Optimize Database](https://support.plex.tv/articles/226836308-help/)
  * [Setup Plex for remote access](https://support.plex.tv/articles/200289506-remote-access/)
  * Give other (internal/external) Plex accounts access to the new server
  * [Enable hardware transcoding](https://support.plex.tv/articles/200250347-transcoder/)
  * Make some popcorn and enjoy 🍿
</details>

## Moving my Plex library from a Mac to a Synology NAS

[This](https://support.plex.tv/articles/201370363-move-an-install-to-another-system/) is the official documentation from Plex for how to move a Plex install to a new system. I will largely be following those instructions in this guide.

### Copying Plex Data from a Mac to Synology NAS

[This](https://support.plex.tv/articles/201154537-move-media-content-to-a-new-location/) is the official documentation from Plex for how to move media content to a new location.

In there, step 1 is to [back up your Plex media server data](https://support.plex.tv/articles/201539237-backing-up-plex-media-server-data/) before making major changes to your library. This holds all your viewstates, metadata, settings, etc.. It probably is a good idea to quit your Plex Media Server before backing anything up just to make sure the files aren’t changing while you’re doing it. But before you do that, disable the `Empty trash automatically after every scan` option you can find by clicking the [settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right in Plex on web) —> Under "Settings", click on Library. Once you disable the `Empty trash automatically after every scan` option, then you can shut down your Plex Media Server.

> "Backing up" can be as simple as copying a file or copying a folder and giving it a new name. I like to append a `_backup` to the filename to distinguish backups. For folders, it might be easier to right click on them and then "Compress `<folder name>`". This will make a copy of that folder but as a `.zip` file.
{: .prompt-info }

Your Plex Media Server (PMS) data location can be found [here](https://support.plex.tv/articles/202915258-where-is-the-plex-media-server-data-directory-located/). `~/Library/Application Support/Plex Media Server/` for macOS. Mine was decently large at ~60GB in size.

Additional Plex settings can be found [here](https://support.plex.tv/articles/201539237-backing-up-plex-media-server-data/), `~/Library/Preferences/com.plexapp.plexmediaserver.plist` for macOS.
* I ended up not moving this file over to my NAS. Plex on Linux uses a `Preferences.xml` for additional Plex settings and converting between `.plist` and `.xml` seemed like a messy hack. I don't remember ever manually modifying any of these values so I decided to start fresh as ["the vast majority of users will never need to alter these settings"](https://support.plex.tv/articles/201105343-advanced-hidden-server-settings/).

Additionally, I’d recommend upgrading your Synology box's operating system (the OS is named *DiskStation Manager*, also known as DSM) to 7.2+ if you haven't already as 7.2 was an update that changes the name of the package that is installed from the Package Center. DSM versions <7.2 installed a package named *Docker* whereas versions 7.2+ installed a package named *Container Manager*.

Also, in your down time, I’d start transferring over your Plex movies, tv shows, music, pictures, etc. as that could take some time.

### "Installing" Plex via Docker Compose
Next, I’m going to install *Container Manager* to my Synology NAS. [To do that](https://kb.synology.com/en-nz/DSM/tutorial/How_to_install_applications_with_Package_Center), simply go to the *Package Center* in your Synology NAS, then search for and install *Container Manager*.

Next I went into the *File Station* and made a `plex` folder in the `docker` folder. I believe the `docker` folder is created upon *Container Manager* install. In the `plex` folder I made three more folders: `config`, `data`, `transcode`.
```
|-- docker
|   |-- plex
|   |   |-- config
|   |   |-- data
|   |   `-- transcode
```
<my-caption>Plex folder structure</my-caption>

Next, I made a file in the `plex` folder: `plex-pms-docker-compose.yaml` and pasted in the [docker compose template for host networking](https://github.com/plexinc/pms-docker/blob/master/docker-compose-host.yml.template).
In that docker compose file I updated the `TZ` (time zone) environment variable to match my respective `TZ` identifier. For me it was `‘America/Denver’`. You can find a list of valid strings for the `TZ` environment variable [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
```yaml
services:
  plex:
    environment:
      - TZ='America/Denver'
```
{: file='plex-docker-compose.yaml'}

If you are a [Plex Pass](https://www.plex.tv/plex-pass/) subscriber, to enable [the additional features](https://www.plex.tv/plex-pass/#modal-plex-pass-features), you'll likely need to specifically [use the image](https://hub.docker.com/r/plexinc/pms-docker/tags) that has the `plexpass` tag:
```yaml
services:
  plex:
    image: plexinc/pms-docker:plexpass
```
{: file='plex-docker-compose.yaml'}

If you don't subscribe to Plex Pass, you can just leave it at `image: plexinc/pms-docker`.

The next variable that needs updating in our docker-compose file is the `PLEX_CLAIM`. This connects your docker plex media server to your plex account. You can get your plex claim from [plex.tv/claim](https://www.plex.tv/claim/).
```yaml
services:
  plex:
    environment:
      - PLEX_CLAIM=claim-xxxxxxxxxxxxxx-xxxxx
```
{: file='plex-docker-compose.yaml'}

Now, we need to mount `/config`, `/data`, and `/transcode` into the docker container so that Plex has access to them. In docker, the container only has access to the files/folders that you mount inside it. My mountings were as follows:
```yaml
services:
  plex:
    volumes:
      - /volume1/docker/plex/config:/config
      - /volume1/docker/plex/transcode:/transcode
      - /volume1/docker/plex/data:/data:ro
```
{: file='plex-docker-compose.yaml'}

> Here, I am mounting the `data` directory as `ro` = *read only*. This is some additional security to ensure Plex doesn't go rogue and delete anything. *However*, if you're going to record live TV or have Plex write anything to the data folder, you will want to remove the `:ro`, as Plex won't have permissions to write/save anything if the folder is *read only*.
{: .prompt-info }

To run the docker container using docker compose:
```console
matt@mac # ssh nas

user@nas $ # The path that I use for the below line is /volume1/docker/plex/
user@nas $ cd /path/to/folder/with/plex-docker-compose-file
user@nas $ sudo docker-compose -f plex-pms-docker-compose.yaml up -d
```

> Note that Synology's *Container Manager* is [supplying us an older version of docker compose](https://www.reddit.com/r/synology/comments/1ei9c1x/outdated_docker_composer/) that uses `docker-compose`. Newer versions call docker compose via `docker compose`.
>
> Note the space vs a hyphen.
{: .prompt-info }

### Copying my Plex media from an external hard drive to Synology NAS

My Plex library is terabytes in size so this was a decent chore. I’m moving all the plex content to `/volume1/docker/plex/data/`
```console
user@nas:/volume1/docker/plex/data$ ls
 Movies
 TV Shows
```

It seems as if you can [connect an external hard drive directly to the NAS](https://kb.synology.com/en-ph/DSM/help/DSM/AdminCenter/system_externaldevice_devicelist?version=7) (if your NAS has a USB port). I have not tested nor experimented with this.

Another option is to mount your external hard drive and NAS on the same computer and click and drag files from one to another. This is a nice, easy option. One issue with this is if things get interrupted for any reason, it can be difficult to resume the transfer.

Using ~~[`scp`](https://www.geeksforgeeks.org/scp-command-in-linux-with-examples/)~~ [`rsync`](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories) to transfer the data to the NAS is probably the best option but can be a bit difficult/intimidating. I would highly recommend not using `scp` as if the transfer gets interrupted for any reason, it is very difficult to resume it. `rsync` can easily resume incomplete transfers and is a much better tool for this job.

I elected to plug in the external hard drive to a computer and then open/mount both my external hard drive and my NAS on my computer. This allows me to then click and drag the files/folders from one to the other. I did this mainly because I have a few folders that have [Apple's tags feature](https://support.apple.com/guide/mac-help/tag-files-and-folders-mchlp15236/mac) on them. I could not get `rsync` to copy over the tags no matter what I did. In hindsight, the tags are kind of a dumb feature and I probably would have been better off just modifying the file/folder names.
* **However**, be aware that there are a few issues that can silently happen when copying files via Finder and `afp`. If you are going to copy the files with Finder, make sure you [connect to the NAS via `smb`](https://kb.synology.com/en-global/DSM/help/DSM/Tutorial/store_with_mac?version=6), [do not use `afp`](https://www.macworld.com/article/234926/using-afp-to-share-a-mac-drive-its-time-to-change.html). I am working on a blog post with a writeup containing my difficulties. <!-- TODO: Add link -->

No matter which route you choose (`rsync` or Finder via `smb`), I'd **highly recommend hard wiring things together during the transfer**. Try your best to avoid connecting to the NAS over WiFi. Things will go much faster. Your computers (and Father Time) will thank you.

After the transfer is complete, I'd recommend to use `rsync` to ensure all your files got transferred over to the NAS. This is optional, but it's good to double check:
```console
$ rsync -avin --no-p /path/to/external/hard/drive/Movies/  nas:/volume1/docker/plex/data/Movies/ | grep -v .DS_Store
```
This command should be run whenever you have your external hard drive mounted on your computer and your NAS is accessible on your network via `ssh nas`. This command will output all the files that are in your local directory but not on the NAS (while ignoring `.DS_Store` files). This checks file size and file modification time but ignores permissions.

If you have some weird characters in filenames, you can ignore them by adding the `--iconv=utf-8-mac,utf-8` flag:
```console
$ rsync -avin --no-p /path/to/external/hard/drive/Movies/ --iconv=utf-8-mac,utf-8 nas:/volume1/docker/plex/data/Movies/ | grep -v .DS_Store
```

If you also want to check the contents of the file to make sure they are the same, you can add the `-c` (checksum) flag. `rsync` will run a checksum on your local file + it will have `rsync` on the NAS run a checksum of its file and compare. This saves lots of data transfer time (only transmitting checksums back and forth, not the actual files) at the expense of CPU time (to calculate the checksums).

> **MAKE SURE YOU ADD A TRAILING `/` TO YOUR FILE PATHS WHEN USING `RSYNC`**. Otherwise, `rsync` does not do this comparison correctly. Basically, having a trailing `/` tells `rsync` "compare the contents of this directory". See [this StackOverflow post](https://stackoverflow.com/a/56627246/4368898) and/or [this blog post](https://cheat.readthedocs.io/en/latest/rsync.html) for additional information.
{: .prompt-warning}

>If you are seeing **A TON** of files (like all of them) showing up, you probably have a path wrong. For some reason, my tab complete for “TV Shows” was completing to `TV\\\ Shows` when it should have been `TV\ Shows`. Seems to be a disagreement over escape characters...
{: .prompt-info}

### Configuring Plex on the NAS

Now that we have our content moved over to the NAS, we need to tell Plex the new location of all its content (Plex support article [here](https://support.plex.tv/articles/200289266-editing-libraries/) with some great instructions that I will be following).
To properly do that, we need to:
1. Edit our Plex library so that we can add a source of where the new content is
  * Go to the [Plex home screen](https://app.plex.tv/desktop/#!/settings/web/index.html#!) --> Hover over a library on the left sidebar --> click the 3 dots --> Manage Library --> Edit... --> Add folders --> Browser for Media Folder
2. Plex will rescan and associate the new content location with the old content
  * If Plex does not do this automatically, you can go to the [Plex home screen](https://app.plex.tv/desktop/#!/settings/web/index.html#!) --> Hover over a library on the left sidebar --> click the 3 dots --> Scan Library Files
3. Confirm Plex can play your content with the new location
  * Because Plex can't access the old location (as it's on an external hard drive connected to another computer), if you can play your Plex media, that shows that Plex has associated your media to its new location
4. Remove the old content location
  * Go to the [Plex home screen](https://app.plex.tv/desktop/#!/settings/web/index.html#!) --> Hover over a library on the left sidebar --> click the 3 dots --> Manage Library --> Edit... --> Add folders --> click on the "X" next to the old content location

Once this is done for all of your libraries (Ex. I have a library for Movies, TV Shows, etc.), you can then [empty the library trash](https://support.plex.tv/articles/200289326-emptying-library-trash/)
- [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Libraries (under Manage) —> 3 dots on the right once you hover over a library —> Empty Trash.

You can then “[Clean Bundles](https://support.plex.tv/articles/226836308-help/)”
- [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Troubleshooting (under Manage) —> Clean Bundles

You can “[Optimize Database](https://support.plex.tv/articles/226836308-help/)"
- [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Troubleshooting (under Manage) —> Optimize Database

If you originally disabled the "Empty trash automatically after every scan" [library option](https://support.plex.tv/articles/200289526-library/), you can turn that back on.
- [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right in Plex on web) —> Settings —> Library

If you’re moving this Plex library to a new device, don’t forget to [setup Plex for remote access](https://support.plex.tv/articles/200289506-remote-access/).
- This might involve forwarding Plex’s ports (32400 by default) to the new device.
  - This may be done automatically via [UPnP](https://en.wikipedia.org/wiki/Universal_Plug_and_Play)
  - Or if you set a static port forwarding in your router, change where port 32400 gets forwarded to.
- Check Plex's remote access in [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Remote Access (under Settings) —> Show Advanced

Lastly, I needed to give my other Plex accounts access to the new server.
* For accounts external of your home account: [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Manage Library Access (top left, under your username), then modify accordingly
* For accounts internal to your home account: [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Plex Home (top left, under your username), then modify accordingly

I then logged out of my account and logged into each internal account and changed their pin sources on the left sidebar to remove the old server and add the new one.

### Enabling Hardware (HW) Transcoding
If you have [Plex pass](https://www.plex.tv/plex-pass/), you can enable hardware transcoding to speed up video conversions.

Before wasting time doing this, make sure your [NAS supports it](https://docs.google.com/spreadsheets/d/1MfYoJkiwSqCXg8cm5-Ac4oOLPRtCkgUxU0jdj3tmMPc/edit#gid=1274624273).
Or, make sure your [CPU supports it](https://ark.intel.com/content/www/us/en/ark/search/featurefilter.html?productType=873&0_QuickSyncVideo=True) (filter on Intel Quick Sync Video).

To take full advantage of this, you need to check BOTH “Use hardware acceleration when available” AND “Use hardware-accelerated video encoding”. This is in [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Transcoder (under Settings).
* “Use hardware acceleration when available” = encode and decode to hardware-accelerated video codecs
* “Use hardware accelerated video encoding” = use hardware acceleration for the encoding / decoding
  * [Source](https://support.plex.tv/articles/200250347-transcoder/)
  * Additional article [here](https://medium.com/@MrNick4B/plex-on-docker-on-synology-enabling-hardware-transcoding-fa017190cad7)
  * Plex's instructions [here](https://github.com/plexinc/pms-docker#intel-quick-sync-hardware-transcoding-support)

![Plex settings window with the two checkboxes mentioned above](/assets/img/posts/2024-11-18-moving-my-plex-library-from-a-mac-to-a-synology-nas/plex-hw-transcoding-checkboxes.png)
*Check both of these boxes to fully enable hardware transcoding*

There is one addition you need to make to the `docker-compose.yaml` file: the `devices` keyword
```yaml
services:
  plex:
    devices:
      - "/dev/dri:/dev/dri"
```
{: file='plex-docker-compose.yaml'}

I also switched the image to the plexpass tag: `plexinc/pms-docker:plexpass`. I can't confirm that is necessary as I've never tried hardware transcoding with `plexinc/pms-docker`.

As [others have noted](https://medium.com/@MrNick4B/plex-on-docker-on-synology-enabling-hardware-transcoding-fa017190cad7), using CPU transcoding, my CPU usage is around 100%, but after HW decoding gets enabled, I see it drop to ~35%. This is a good indicator if things are working or not.
* You can find these numbers by clicking the [settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right in Plex on web) —> Dashboard (under *Status* on the left).

Another indicator if things are working is to look at Plex's status when streaming. While a device is viewing a video, if hardware transcoding is setup properly and transcoding is required, you will see "Transcoding (hw)". If you see that the video is playing back via *direct play*, you can manually change the streaming quality on the device viewing the video to force transcoding to happen.
* The screen below can be accessed via [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Dashboard (under Status):
![Plex will show you "Transcode (hw)" if hardware transcoding is setup properly](/assets/img/posts/2024-11-18-moving-my-plex-library-from-a-mac-to-a-synology-nas/plex-hw-transcoding-dashboard.png)
*Plex will show you "Transcode (hw)" if transcoding is required and hardware transcoding is setup properly*

If this doesn’t work, some starting points for debugging is to search the logs for “transcoding”, “error”, or “ffmpeg”:
* You can find the logs via [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Console (under Manage at the very bottom left). From there, you can search for the keywords mentioned above in the "Filter logs" text box.
* If you're brave and the above doesn't work, you could try to "Download Logs" via [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Troubleshooting (under Manage at the very bottom left).
* Additionally, you could try to look through some other logs by running `sudo docker logs plex` in a terminal connected to the NAS. I didn't have much luck looking in these logs, but I'm just making you aware of their existence.

### Updating Plex
To update plex, there is no need to do it through the web GUI anymore. All you need to do is restart docker, and the plex image will automatically redownload the latest version of plex media server:
```console
user@nas $ sudo docker-compose pull   # Necessary if using `plexinc/pms-docker` image
user@nas $ sudo docker-compose -f plex-pms-docker-compose.yaml down
[+] Running 1/1
 ⠿ Container plex  Removed                                                      17.6s
user@nas $ sudo docker-compose -f plex-pms-docker-compose.yaml up -d
[+] Running 1/1
 ⠿ Container plex  Started
```

Note that this is only applicable if you are using a "dynamic" tag for the `pms-docker` image.
* In `plex-pms-docker-compose.yaml`, if you used `image: plexinc/pms-docker` (which points to `image: plexinc/pms-docker:latest`) or `image: plexinc/pms-docker:plexpass`, those are both dynamic tags.
  * If you instead specified a specific tag, Ex. `image: plexinc/pms-docker:1.41.2.9200-c6bbc1b53`, then you will need to manually change the tag that is being pulled in, then restart docker.
  * You can find valid `pms-docker` tags at the [`pms-docker` repo on Docker Hub](https://hub.docker.com/r/plexinc/pms-docker/tags).

## Moving Tautulli from a Mac to Synology NAS
I've moved this section into its own blog post: [Moving Tautulli from a Mac (Python) to a Synology NAS (Docker)](/posts/moving-tautulli-from-a-mac-python-to-a-synology-nas-docker/).
