---
title: "Moving Tautulli from a Mac (Python) to a Synology NAS (Docker)"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2024-11-20 23:00:09 -0700
categories: [Blog, Not YouTube]    # <=2 values here: top category and sub category
tags: [bash, docker, docker compose, how to, linux, mac os, nas, not youtube, synology, tautulli, tech, tutorial]  # TAG names should always be lowercase
layout: post                # post is the default, we will set it to be explicit
pin: false
toc: true                   # Table of contents
comments: true              # Enable/disable comments at the bottom of the post
math: false                 # Disabled by default for performance reasons
mermaid: false              # Diagram generation tool via ```mermaid [...]```
#img_cdn: https://cdn.com
#media_subpath: /img/path/
image:
 path: /assets/img/posts/2024-11-20-moving-tautulli-from-a-mac-python-to-a-synology-nas-docker/macbook-tautulli-to-synology-nas.jpg
#  width: 100   # in pixels
#  height: 40   # in pixels
 alt: Image is AI-assisted. The Synology NAS is an AI creation and not a real model for sale.
description: Detailed steps for moving a Tautulli installation from Python on a Mac to docker in a Synology NAS
---

> This tutorial assumes you have some [basic knowledge of the command line/terminal](/posts/introduction-to-the-command-line-shell-terminal-etc/) and [`ssh`](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server)ing into a machine to run commands. Docker familiarity is helpful as well, but I'll explain the `docker compose` commands we'll be running if you're unfamiliar.
{: .prompt-warning}

## Intro

### What is this post about?
In my previous post, I explained [how I moved my Plex Library from a Mac to a Synology NAS](/posts/moving-my-plex-library-from-a-mac-to-a-synology-nas/). This post will build off of that and guide you through how I moved [Tautulli](https://tautulli.com) from my Mac (running in Python) to a Synology NAS (running in docker).

### What is Tautulli?
> Tautulli is a 3rd party application that you can run alongside your Plex Media Server to monitor activity and track various statistics. Most importantly, these statistics include what has been watched, who watched it, when and where they watched it, and how it was watched. The only thing missing is "why they watched it", but who am I to question your 42 plays of *Frozen*. All statistics are presented in a nice and clean interface with many tables and graphs, which makes it easy to brag about your server to everyone else.
> [Source](https://tautulli.com)

I use Tautulli to historically see who is playing content and how that content was watched (direct play vs transcoding). This way, if there are any comments or questions on quality, I can look back and easily see what happened and debug.

I also love statistics and Tautulli gives some great quantitative visuals on your server's usage.

![Example graphs on Tautulli showing daily play duration, play duration by day of week, and play duration by hour of day](https://tautulli.com/images/screenshots/graphs.png)
*Example Graphs in Tautulli*

## Moving Tautulli from a Mac to Synology NAS

### Backing up old Tautulli Data
Let's get into it and start moving Tautulli. We'll start by following this question in their FAQ:
* [I need to move/reinstall Tautulli, can I keep my history and statistics?](https://github.com/Tautulli/Tautulli/wiki/Frequently-Asked-Questions#q-i-need-to-movereinstall-tautulli-can-i-keep-my-history-and-statistics)

To back up your Tautulli data, you need to go into Tautulli on web --> gear (top right) --> Settings --> Help & Info
  * Under "Tautulli Configuration", click on `/config/config.ini` to download your Tautulli configuration
  * Under "Tautulli Configuration", click on `/config/tautulli.db` to download your Tautulli database

We have now backed up everything we need from Tautulli.

### Installing Tautulli via Docker in Synology NAS
If you haven't already, install *Container Manager* to your Synology NAS. This will install docker in your Synology NAS. [You can do this by](https://kb.synology.com/en-nz/DSM/tutorial/How_to_install_applications_with_Package_Center) going to the *Package Center* in your Synology NAS, then search for and install *Container Manager*.

Personally, I want to create a new user account for Tautulli. This is recommended and will make access control easier (restricting access to certain files, permissions, etc.). Here's how to create a new user in Synology's OS: DiskStation Manager (DSM):
  * In DSM go to Control Panel --> User & Group --> Under "User", click Create
    * I gave the name of `tautulli`
    * Description: `Tautulli user account` (optional)
    * Uncheck "Send a notification mail to the newly created user" (optional)
    * Click "Next"
    * Click "Next"
    * For permissions, I gave Read/Write access to the `docker` folder, left it at "Default" for `homes`, and "No Access" for everything else
      * This way, the `tautulli` user will only be able to access the `docker` folder (and its home directory).
    * Click "Next" through the rest of the prompts

Then we will need to create a folder for Tautulli. I'll be making mine as `/volume1/docker/tautulli`, similar to [what I did for Plex](/posts/moving-my-plex-library-from-a-mac-to-a-synology-nas/#installing-plex-via-docker-compose), but you are welcome to place it wherever you'd like. The `tautulli` folder will also need a `config` folder inside of it:

```console
|-- docker
|   |-- tautulli
|   |   `-- config
```
<my-caption>Tautulli folder structure</my-caption>

In the `tautulli` folder, we'll create the `docker-compose` file. I named mine `tautulli-docker-compose.yaml`. You can find Tautulli's template for their `docker-compose` [here](https://github.com/Tautulli/Tautulli/wiki/Installation#using-docker-compose).

We have a few configuration changes to make in Tautulli's `docker-compose` file:
* We need to mount Tautulli's config in `/config`
* Set the timezone to `America/Denver` [just as we did for Plex's `docker-compose`](/posts/moving-my-plex-library-from-a-mac-to-a-synology-nas/#installing-plex-via-docker-compose).
  * Other time zones can be found [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
* If you created a `tautulli` user above, give the container its user ID (UID) and group ID (GID):
  * Here's how to get the `tautulli` user's *user id* and *group id*:
  * ```console
    user@nas $ id -u tautulli
    1033
    user@nas $ id -g tautulli
    100
    ```

After all that, my `tautulli-docker-compose.yaml` looked like this:
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

> Note that you can specify the Tautulli version after the `image:` tag (Ex. `image: ghcr.io/tautulli/tautulli:v2.13.4`). This can be a smart idea in case future updates break things. However, nothing really "depends" on Tautulli and I don't foresee any issues with future Tautulli updates. Thus, I will leave the image without mentioning the version (which is effectively the same as `image: ghcr.io/tautulli/tautulli:latest`). This will pull the latest image available and will make updating very easy in the future.
{: .prompt-info }

Now it's time to launch Tautulli with Docker Compose:

```console
user@nas $ # The path that I use for the below line is /volume1/docker/tautulli/
user@nas $ cd /path/to/folder/with/tautulli-docker-compose-file
user@nas $ sudo docker-compose -f tautulli-docker-compose.yaml up
```

> Note that Synology's *Container Manager* is [supplying us an older version of docker compose](https://www.reddit.com/r/synology/comments/1ei9c1x/outdated_docker_composer/) that uses `docker-compose`. Newer versions call docker compose via `docker compose`.
>
> Note the space vs a hyphen.
{: .prompt-info }

Afterwards, you should now be able to access Tautulli in a web browser at `<NAS_IP>:8181`.

> Note that this must be `http://NAS_IP:8181`. `https` does not work as Tautulli does not have a certificate with its default settings.
>
> Ex. if your NAS's IP is `192.168.0.10`, you would navigate to `http://192.168.0.10:8181` in your browser.
{: .prompt-warning }

### Connecting Tautulli to our Plex server
Once you’re in Tautulli, go into Tautulli on web --> gear (top right) --> Settings --> Plex Media Server. We will need to connect a new server. To do this, click on “Fetch New Token”, and sign in. I can't remember exactly but the rest might auto populate? If not, put in the IP of your NAS, port (`32400` by default), and I checked “use secure connection” because why not?

Then I streamed a few videos in Plex and saw it show up in Tautulli so I think the connection between Plex and Tautulli is good to go!

To import your old database and config go into Tautulli on web --> gear (top right) --> Settings --> Import & Backups. From here, click on the respective buttons for importing a Tautulli database and a Tautulli configuration. Once you do that, verify that the history tab is populated just as it was. That will confirm a successful database import.

If Tautulli is not "linking" old content with new content, look into the FAQ below for a solution. Luckily, I didn't have any issues.
* [FAQ: I moved media in Plex, now Tautulli is linking to the wrong item/showing up twice!](https://github.com/Tautulli/Tautulli/wiki/Frequently-Asked-Questions#q-i-moved-media-in-plex-now-tautulli-is-linking-to-the-wrong-itemshowing-up-twice)

### Updating Tautulli
If you gave a specific Tautulli image version in the `tautulli-docker-compose.yaml` (Ex. `image: ghcr.io/tautulli/tautulli:v2.14.6`), you will need to manually update that version number, then bring Tautulli down then back up:
```console
user@nas $ sudo docker-compose -f tautulli-docker-compose.yaml down
user@nas $ sudo docker-compose -f tautulli-docker-compose.yaml up -d
```

If you did not specify a specific Tautulli image version (Ex. `image: ghcr.io/tautulli/tautulli`), you just need to ["re-pull" the latest version, then restart Tautulli](https://github.com/Tautulli/Tautulli/wiki/Installation#using-docker-compose):
```console
user@nas $ sudo docker-compose -f tautulli-docker-compose.yaml pull
user@nas $ sudo docker-compose -f tautulli-docker-compose.yaml up -d
```
