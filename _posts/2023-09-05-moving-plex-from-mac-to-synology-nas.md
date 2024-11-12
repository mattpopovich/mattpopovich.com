---
title: "Moving My Plex Library from a Mac to a Synology NAS"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2023-09-05 02:22:47 -0600
categories: [Blog, TODO]    # <=2 values here: top category and sub category
tags: [todo]                # TAG names should always be lowercase
layout: post                # post is the default, we will set it to be explicit
pin: false
toc: true                   # Table of contents
comments: true              # Enable/disable comments at the bottom of the post
math: false                 # Disabled by default for performance reasons
mermaid: false              # Diagram generation tool via ```mermaid [...]```
#img_cdn: https://cdn.com
#img_path: /img/path/
#image:
#  path: /path/to/image.jpg
#  width: 100   # in pixels
#  height: 40   # in pixels
#  alt: image alternative text
---

<!-- TODO: Add YouTube video link here -->

> This tutorial assumes you have some [basic knowledge of the command line/terminal](TODO: link to command line for beginners post) and [`ssh`](TODO)ing into a machine to run commands. Docker familiarity is helpful as well, but I'll explain the docker commands we'll be running if you're unfamiliar.
{: .prompt-warning}

## Intro

### What is this post about?
This post documents my experience moving my [Plex](https://www.plex.tv/) server from my MacBook to a [Synology NAS](https://www.synology.com/dsm/solution/what-is-nas/for-home) (network attached storage). The Plex server was installed using the [Mac Plex app](https://www.plex.tv/media-server-downloads/?cat=computer&plat=macos) (`.dmg`) and I will be transitioning to docker on the Synology NAS to make future moves (if necessary) much easier due to docker being operating system independent.

I use [Tautulli](https://tautulli.com/) for Plex statistics, so I will also be moving that from the Mac (running via Python) to a docker container on the Synology NAS as well.

### What is Plex?
Plex is an server/client utility that lets you host your own music, pictures, videos, live TV, etc. and view/download them on any device with a streaming service-esque app. You can think of it as your own custom Netflix! Here are the main steps to get it up and running:
1. Dowload and install the Plex server onto a computer. This computer will be the host of your content.
    * Note that you can only stream and download your content when this computer is powered on and connected to your network/the internet.
2. Copy all of the content that you want to stream/download onto your host computer
3. Tell Plex which folder your content is in
4. Download the Plex app or navigate to [plex.tv](https://www.plex.tv) onto your client (phone, TV, tablet, etc.)
5. Login on the client and stream/download your content!

### Why move to a NAS?
I previously hosted my Plex server on a MacBook that was constantly powered on and plugged in. My Mac was old (2012) so it struggled to decode the newer video codecs (H.265/HEVC) + leaving it plugged in all the time isn't great on its battery. I also had all of my content on an external hard drive so in the event of a disk failure (can happen randomly as drives get older), I would have lost all my content. Sure, I could have made a backup but it can be annoying to constantly keep the backup up to date.

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
* [Official Plex documentation on how to move media content to a new location](https://support.plex.tv/articles/201154537-move-media-content-to-a-new-location/)
* Disable the `Empty trash automatically after every scan` option by clicking the [settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right in Plex on web) —> Settings —> Library
* Shut down your Plex Media Server
* [Back up your Plex media server data](https://support.plex.tv/articles/201539237-backing-up-plex-media-server-data/)
  * Your Plex Media Server (PMS) data location can be found [here](https://support.plex.tv/articles/202915258-where-is-the-plex-media-server-data-directory-located/)
    * `~/Library/Application Support/Plex Media Server/` for macOS.
  * Additional Plex settings can be found [here](https://support.plex.tv/articles/201539237-backing-up-plex-media-server-data/)
    * `~/Library/Preferences/com.plexapp.plexmediaserver.plist` for macOS.
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

## Moving my Plex library from a Mac to Synology NAS

### "Installing" Plex via Docker Compose

[This](https://support.plex.tv/articles/201154537-move-media-content-to-a-new-location/) is the official documentation from Plex for how to move media content to a new location.

In there, step 1 is to [back up your Plex media server data](https://support.plex.tv/articles/201539237-backing-up-plex-media-server-data/) before making major changes to your library. This holds all your TODO (plex data?). It probably is a good idea to quit your Plex Media Server before backing anything up just to make sure the files aren’t changing while you’re doing it. But before you do that, disable the `Empty trash automatically after every scan` option you can find by clicking the [settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right in Plex on web) —> Under "Settings", click on Library. Once you disable the `Empty trash automatically after every scan` option, then you can shut down your Plex Media Server.

Your Plex Media Server (PMS) data location can be found [here](https://support.plex.tv/articles/202915258-where-is-the-plex-media-server-data-directory-located/). `~/Library/Application Support/Plex Media Server/` for macOS. Mine was decently large at ~60GB in size.

Additional Plex settings can be found [here](https://support.plex.tv/articles/201539237-backing-up-plex-media-server-data/), `~/Library/Preferences/com.plexapp.plexmediaserver.plist` for macOS.

Additionally, I’d recommend upgrading your Synology box's operating system (the OS is named *DiskStation Manager*, also known as DSM) to 7.2+ if you haven't already as 7.2 was an update that changes the name of the package that is installed from the Package Center. DSM versions <7.2 installed a package named *Docker* whereas versions 7.2+ installed a package named *Container Manager*.

Also, in your down time, I’d start transferring over your Plex movies, tv shows, music, pictures, etc. as that could take some time.

Next, I’m going to install *Container Manager* to my Synology NAS. [To do that](https://kb.synology.com/en-nz/DSM/tutorial/How_to_install_applications_with_Package_Center), simply go to the *Package Center* in your Synology NAS, then search for and install *Container Manager*.

Next I went into the *File Station* and made a `plex` folder in the `docker folder`. In the `plex` folder I made 3 more folders: `config`, `data`, `transcode`.
```
|-- docker
|   |-- plex
|   |   |-- config
|   |   |-- data
|   |   `-- transcode
```

Next, I made a file in the `plex` folder: `plex-pms-docker-compose.yaml` and pasted in the [docker compose template for host networking](https://github.com/plexinc/pms-docker/blob/master/docker-compose-host.yml.template).
In that docker compose file I updated the `TZ` (time zone) environment variable to match my respective `TZ` identifier. For me it was `‘America/Denver’`. You can find a list of valid strings for the `TZ` environment variable [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
```yaml
services:
  plex:
    environment:
      - TZ='America/Denver'
```
{: file='plex-docker-compose.yaml'}

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
> Here, I am mounting the `data` directory as `ro` = *read only*. This is some additional security to ensure Plex doesn't go rogue and delete anything. *However*, if you're going to record live TV or have Plex write anything to the data folder, you will want to remove the `:ro`, as Plex won't have permissions to save anything if the folder is *read only*.
{: .prompt-info }

To run the docker container using docker compose:
```console
matt@mac # ssh nas
user@nas $ cd /path/to/folder/with/plex-docker-compose-file   # /volume1/docker/plex
user@nas $ sudo docker-compose -f plex-pms-docker-compose.yaml up -d
```

> Note that Synology's *Container Manager* is [supplying us an older version of docker compose](https://www.reddit.com/r/synology/comments/1ei9c1x/outdated_docker_composer/) that uses `docker-compose`. Newer versions call docker compose via `docker compose`.
>
> Note the space vs a hyphen.
{: .prompt-info }

### Copying my Plex data from an external hard drive to Synology NAS

My Plex library is terabytes in size so this was a decent chore. I’m moving all the plex content to `/volume1/docker/plex/data/`
```console
user@nas:/volume1/docker/plex/data$ ls
 Movies
 TV Shows
```

It seems as if you can [connect an external hard drive directly to the NAS](https://kb.synology.com/en-ph/DSM/help/DSM/AdminCenter/system_externaldevice_devicelist?version=7) (if your NAS has a USB port). I have not tested this.

Another option is to mount your external hard drive and NAS on the same computer and click and drag files from one to another. This is a nice, easy option. One issue with this is if things get interrupted for any reason, it can be difficult to resume the transfer.

Using ~~[`scp`](https://www.geeksforgeeks.org/scp-command-in-linux-with-examples/)~~ [`rsync`](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories) to transfer the data to the NAS is probably the best option but can be a bit difficult/intimidating. I would highly recommend not using `scp` as if the transfer gets interrupted for any reason, it is very difficult to resume it. `rsync` can easily resume incomplete transfers and is a much better tool for this job.

I elected to plug in the external hard drive to a computer and then open/mount both my external hard drive and my NAS on my computer. This allows me to then click and drag the files/folders from one to the other. I did this mainly because I have a few folders that have [Apple's tags feature](https://support.apple.com/guide/mac-help/tag-files-and-folders-mchlp15236/mac) on them. I could not get `rsync` to copy over the tags no matter what I did. In hindsight, the tags are kind of a dumb feature and I probably would have been better off just modifying the file/folder names. **However**, be aware that there are a few issues that can silently happen with this method. Read my blog post [here](TODO) for a writeup of my difficulties.

No matter which route you choose, I'd **highly recommend hard wiring things together during the transfer**. Try your best to avoid connecting to the NAS over WiFi. Things will go much faster. Your computers will thank you.

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

> **MAKE SURE YOU ADD A TRAILING `/` TO YOUR FILE PATHS**. Otherwise, `rsync` does not do this comparison correctly (TODO explain why)
{: .prompt-warning}

>If you are seeing **A TON** of files (like all of them) showing up, you probably have a path wrong. For some reason, my tab complete for “TV Shows” was completing to `TV\\\ Shows` when it should have been `TV\ Shows`. Seems to be a disagreement over escape characters...
{: .prompt-info}

### Configuring Plex on the NAS

TODO: Where does this link belong
https://support.plex.tv/articles/201370363-move-an-install-to-another-system/

Now that we have our content moved over to the NAS, we need to tell Plex the new location of all its content (Plex support article [here](https://support.plex.tv/articles/200289266-editing-libraries/)).
To properly do that, we need to edit our Plex library, add a source of where the new content is, Plex will rescan and associate the new content location with the old content, then you can delete the old content location.
TODO: Image of this

Once this is done for all of your libraries (Ex. I have a library for Movies, TV Shows, etc.), you can then [empty the library trash](https://support.plex.tv/articles/200289326-emptying-library-trash/)
- [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Libraries (under Manage) —> 3 dots on the right once you hover over a library —> Empty Trash.

You can then “[Clean Bundles](https://support.plex.tv/articles/226836308-help/)”
- [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Troubleshooting (under Manage) —> Clean Bundles

You can “[Optimize Database](https://support.plex.tv/articles/226836308-help/)"
- [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Troubleshooting (under Manage) —> Optimize Database

If you’re moving this Plex library to a new device, don’t forget to [setup Plex for remote access](https://support.plex.tv/articles/200289506-remote-access/).
- This might involve forwarding Plex’s ports (32400 by default) to the new device.
  - This may be done automatically via [UPnP](https://en.wikipedia.org/wiki/Universal_Plug_and_Play)
  - Or if you set a static port forwarding in your router, change where port 32400 gets forwarded to.
- Check Plex's remote access in [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Remote Access (under Settings) —> Show Advanced

Lastly, I needed to give my other Plex accounts access to the new server.
* For accounts external of your home account: [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Manage Library Access (top left, under your username), then modify accordingly
* For accounts internal to your home account: [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Plex Home (top left, under your username), then modify accordingly
I then went into each account and changed their pin sources on the left to remove the old server and add the new one.

### Enabling HW Transcoding
If you have [Plex pass](https://www.plex.tv/plex-pass/), you can enable hardware transcoding to speed up video conversions.

Before wasting time doing this, make sure your [NAS supports it](https://docs.google.com/spreadsheets/d/1MfYoJkiwSqCXg8cm5-Ac4oOLPRtCkgUxU0jdj3tmMPc/edit#gid=1274624273).
Or, make sure your [CPU supports it](https://ark.intel.com/content/www/us/en/ark/search/featurefilter.html?productType=873&0_QuickSyncVideo=True) (filter on Intel Quick Sync Video).

To take full advantage of this, you need to check BOTH “Use hardware acceleration when available” AND “Use hardware-accelerated video encoding”. This is in [Settings/wrench](https://app.plex.tv/desktop/#!/settings/web/general) (top right) —> Transcoder (under Settings).
* “Use hardware acceleration when available” = encode and decode to hardware-accelerated video codecs
* “Use hardware accelerated video encoding” = use hardware acceleration for the encoding / decoding
* [Source](https://support.plex.tv/articles/200250347-transcoder/)
* Additional article [here](https://medium.com/@MrNick4B/plex-on-docker-on-synology-enabling-hardware-transcoding-fa017190cad7)
* Plex's instructions [here](https://github.com/plexinc/pms-docker#intel-quick-sync-hardware-transcoding-support)

TODO: Show image

There is one addition you need to make to the docker-compose.yaml file: the `devices` keyword
```yaml
services:
  plex:
    devices:
      - "/dev/dri:/dev/dri"
```
{: file='plex-docker-compose.yaml'}

I did also switch to the plexpass tag: `plexinc/pms-docker:plexpass`. Not sure if that is necessary or not.

As [others have noted](https://medium.com/@MrNick4B/plex-on-docker-on-synology-enabling-hardware-transcoding-fa017190cad7), using CPU transcoding, my CPU usage is around 100%, but after HW decoding gets enabled, I see it drop to ~35%. This is a good indicator if things are working or not. TODO: Where to find these numbers?

Another indicator if things are working is to look at Plex's status when streaming or to look in Tautulli's logs. TODO: Expand on this

If this doesn’t work, some starting points for debugging is to search the logs for “transcoding”, “error”, or “ffmpeg”. You can find the logs by running `docker logs plex` in a terminal connected to the NAS, settings —> manage —> console, and settings —> manage —> Troubleshooting. TODO: Where are these last ones?

### Updating Plex
To update plex, there is no need to do it through the web GUI anymore. All you need to do is restart docker, and the plex image will automatically redownload the latest version of plex media server:
Note that this is only applicable to the plexpass tag.
```console
user@nas $ sudo docker-compose -f plex-pms-docker-compose.yaml down
[+] Running 1/1
 ⠿ Container plex  Removed                                                                                                                                           17.6s
user@nas $ sudo docker-compose -f plex-pms-docker-compose.yaml up -d
[+] Running 1/1
 ⠿ Container plex  Started
```

If you don't have the plex pass, TODO


## Moving Tautulli from a Mac to Synology NAS
Next up is moving [Tautuilli](https://github.com/Tautulli/Tautulli). They have two good FAQ questions on their wiki:
* [I moved media in Plex, how to move Tautulli? TODO verify this is what the article talks about](https://github.com/Tautulli/Tautulli/wiki/Frequently-Asked-Questions#q-i-moved-media-in-plex-now-tautulli-is-linking-to-the-wrong-itemshowing-up-twice)
* [FAQ: I need to move/reinstall Tautulli, can I keep my history and statistics?](https://github.com/Tautulli/Tautulli/wiki/Frequently-Asked-Questions#q-i-need-to-movereinstall-tautulli-can-i-keep-my-history-and-statistics)

Basically, you need to go into Tautulli --> settings, download your database and config.

I created a new user in DSM (Control Panel --> User & Group --> Create user) named `tautulli` that only had access to docker file mount share thing TODO: what? TODO: Did I also create a plex user? No, I did not also create a plex user.

Here's how to get the newly created user's *user id* and *group id*:
```console
user@nas $ id -u tautulli
1033
user@nas $ id -g tautulli
100
```

We have a few configuration changes to make in [Tautulli's docker-compose file](https://github.com/Tautulli/Tautulli/wiki/Installation#using-docker-compose). We need to mount Tautulli's config in `/config` + set the timezone to `America/Denver` just as we did for Plex's docker-compose:
```yaml
version: '3'
services:
  tautulli:
    image: ghcr.io/tautulli/tautulli
    container_name: tautulli
    restart: unless-stopped
    volumes:
      - /volume1/docker/tautulli/config:/config
    environment:
      # Matches Tautulli user created on Synology's DiskStation Manager
      - PUID=1033   # Match `id -u tautulli`
      - PGID=100    # Match `id -g tautulli`
      - TZ=America/Denver
    ports:
      - 8181:8181
```
{: file='tautulli-docker-compose.yaml'}

Note that you can specify the Tautulli version after the `image:` tag (Ex. `ghcr.io/tautulli/tautulli:v2.13.4`). This can be a smart idea in case future updates break things. However, nothing really "depends" on Tautulli and I don't forsee any issues with future Tautulli updates. Thus, I will leave the image without mentioning the version. This will pull the latest image available and will make updating very easy in the future.

Now it's time to launch Tautulli with Docker Compose:

```console
user@nas $ cd /path/to/folder/with/tautulli-docker-compose-file
user@nas $ sudo docker-compose -f tautulli-docker-compose.yaml up
```

Afterwards, you should now be able to access Tautulli in a web browser at `<NAS_IP>:8181`.

Once you’re in Tautulli, go into settings —> Plex Media Server. We will need to connect a new server. To do this, click on “Fetch New Token”, sign in. Then the rest might auto populate? If not, put in the IP of your NAS, port, and I checked “use secure connection” because why not?

Then I streamed a few videos in Plex and saw it show up in Tautulli so I think we’re good to go!

Obviously if you are importing a database and config, you’re going to want to see the history tab populated just as it was. That will tell you if you exported and imported it correctly.

### Updating Tautulli
If you specified a specific Tautulli image version in the `tatutulli-docker-compose.yaml`, you will need to manually update that version number, then bring Tautulli down then back up:
```console
user@nas $ sudo docker-compose -f tautulli-docker-compose.yaml down
user@nas $ sudo docker-compose -f tautulli-docker-compose.yaml up -d
```

If you did not specify a specific Tautulli image version, you just need to ["re-pull" the latest version, then restart Tautulli](https://github.com/Tautulli/Tautulli/wiki/Installation#using-docker-compose):
```console
user@nas $ sudo docker-compose -f tautulli-docker-compose.yaml pull
user@nas $ sudo docker-compose -f tautulli-docker-compose.yaml up -d
```


### Other
TODO:

It is recommended to enable the QuickConnect relay service at Control Panel > External Access > QuickConnect > Advanced Settings


