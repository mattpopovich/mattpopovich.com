---
title: "Moving Tautulli from a Mac to a Synology NAS"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2024-11-16 19:50:39 -0600
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
#  path: /path/to/image.jpg
#  width: 100   # in pixels
#  height: 40   # in pixels
#  alt: image alternative text
#description:               # A short sentence to describe the article, used when sharing links on social media and on homepage
---

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
