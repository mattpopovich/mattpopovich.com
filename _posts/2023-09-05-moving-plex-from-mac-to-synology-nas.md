---
title: "Moving My Plex Library from a Mac to a Synology NAS"
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2023-09-5 02:22:47 -0600
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

Moving my Plex Library from a Mac to Synology

[This](https://support.plex.tv/articles/201154537-move-media-content-to-a-new-location/) is the official documentation from Plex for how to move media content to a new location.

In there, step 1 is to [back up your Plex media server data](https://support.plex.tv/articles/201539237-backing-up-plex-media-server-data/) before making major changes to your library. It probably is a good idea to quit your Plex Media Server before backing anything up just to make sure the files aren’t changing while you’re doing it. But before you do that, disable the `Empty trash automatically after every scan` option you can find by clicking the wrench —> Settings —> Library. Then you can shut down your Plex Media Server.

Your Plex Media Server (PMS) data location can be found [here](https://support.plex.tv/articles/202915258-where-is-the-plex-media-server-data-directory-located/). `~/Library/Application Support/Plex Media Server/` for macOS. Mine was quite large at ~60GB in size.

Additional Plex settings can be found [here](https://support.plex.tv/articles/201539237-backing-up-plex-media-server-data/), `~/Library/Preferences/com.plexapp.plexmediaserver.plist` for macOS.

Additionally, I’d recommend upgrading your Synology box to 7.2+ as 7.2 was an update that changes the docker utitlity that was installed (docker vs container manager). Also, in your down time, I’d start transferring over your Plex movies, tv shows, music, pictures, etc. as that could take some time.

Next, I’m going to install container manager (formerly known as docker) to my Synology NAS

From there I will search and download the plexinc/pms-docker image

Next I went into the file station and made a `plex` folder in the `docker folder`. In the `plex` folder I made 3 more folders: `config`, `data`, `transcode`.

Next, I made a file plex-pms-docker-compose.yaml and pasted in the docker compose template for host networking
https://github.com/plexinc/pms-docker/blob/master/docker-compose-host.yml.template
In that docker compose file I updated the TZ environment variable to match my respective TZ identifier. For me it was ‘America/Denver’
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
The next variable that needs updating is the PLEX_CLAIM. This connects your docker plex media server to your plex account. You can get your plex claim from https://www.plex.tv/claim/


Now, we need to mount /config, /data, and /transcode into the docker container. My mountings were as follows:
      - /volume1/docker/plex/config:/config
      - /volume1/docker/plex/transcode:/transcode
      # - /volume1/docker/plex/data:/data:ro
      - /volume1/NAS/elements14TB/MATT/Documents/PlexMBPr12Backup:/Volumes/Plex_8TB:ro

Where
```
$ ls /volume1/docker/plex/config
com.plexapp.plexmediaserver.plist  @eaDir  Library
MattAdmin@DS1520plus:/volume1/docker/plex$ ls /volume1/docker/plex/config/Library/
'Application Support'
MattAdmin@DS1520plus:/volume1/docker/plex$ ls /volume1/docker/plex/config/Library/Application\ Support/
'Plex Media Server'
MattAdmin@DS1520plus:/volume1/docker/plex$ ls /volume1/docker/plex/config/Library/Application\ Support/Plex\ Media\ Server/
 Cache   'Crash Reports'   Drivers   Media      plexmediaserver.pid  'Plug-in Support'   Scanners  'Setup Plex.html'   update-log.txt
 Codecs   Diagnostics      Logs      Metadata   Plug-ins              Preferences.xml    Scripts    Thumbnails         Updates
```


To run the docker container using docker compose:
sudo docker-compose -f plex-pms-docker-compose.yaml up






To make sure all your files got transferred over from the Mac to the NAS:
rsync -avin --no-p Movies/  nas:/volume1/NAS/elements14TB/MATT/Documents/PlexMBPr12Backup/Movies/ | grep -v .DS_Store

rsync -avin --no-p Movies/ --iconv=utf-8-mac,utf-8 nas:/volume1/NAS/elements14TB/MATT/Documents/PlexMBPr12Backup/Movies/ | grep -v .DS_Store
To ignore weird characters in filenames

This will output all the files that are in your local directory but not on the nas. This checks file size and file modification time but ignores permissions
If you also want to check the contents of the file to make sure they are the same, you can add the -c (checksum) flag.

MAKE SURE YOU ADD TRAILING /
Otherwise it does not do this correctly (TODO explain why)

If you are seeing A TON of files (like all of them) showing up, you probably have a path wrong. For some reason, my tab complete for “TV Shows” was completing to “TV\\\ Shows”. It should have been “TV\ Shows”. Not sure why that was.




Now that all my files are moved over, I’m going to move their location in Plex to better represent where they actually are. I’m moving all the content to `/volume1/docker/plex/data/`
MattAdmin@DS1520plus:/volume1/docker/plex/data$ ls
 Movies
 TV Shows

https://support.plex.tv/articles/201370363-move-an-install-to-another-system/

Then, I need to tell Plex that I moved the location of all its content. https://support.plex.tv/articles/200289266-editing-libraries/
To do that, you move the content, edit the library, add a source of where the new content is, Plex will rescan and associate the new content location with the old content, then you can delete the old content location.

Once this is done for all of your libraries, you can then empty the library trash (settings —> Manage —> Libraries —> 3 dots next to library —> Empty Trash).
https://support.plex.tv/articles/200289326-emptying-library-trash/
You can then “Clean Bundles” (Settings —> Manage —> Troubleshooting —> Clean Bundles): https://support.plex.tv/articles/226836308-help/
You can “Optimize Database” (Settings —> Manage —> Troubleshooting —> Optimize Database): https://support.plex.tv/articles/226836308-help/

Lastly, if you’re moving this Plex library to a new device, don’t forget to forward Plex’s ports (32400 by default) to the new device. (Settings —> Settings —> Remote Access —> Show Advanced).


Lastly, I needed to give access to the new server to my other Plex accounts.
For accounts external of your home account: Settings —> UserName (MattPopovich) —> Manage Library Access, then modify accordingly
For accounts internal to your home account: Settings —> UserName (MattPopovich) —> Plex Home, then modify accordingly
I then went into each account and changed their pin sources on the left to remove the old server and add the new one

Enabling HW Transcoding
If you have Plex pass, you can enable hardware transcoding to speed up video conversions https://www.plex.tv/plex-pass/

Before wasting time doing this, make sure your NAS supports it: https://docs.google.com/spreadsheets/d/1MfYoJkiwSqCXg8cm5-Ac4oOLPRtCkgUxU0jdj3tmMPc/edit#gid=1274624273
Or, make sure your CPU supports it: https://ark.intel.com/content/www/us/en/ark/search/featurefilter.html?productType=873&0_QuickSyncVideo=True

To take full advantage of this, you need to check BOTH “Use hardware acceleration when available” AND “Use hardware-accelerated video encoding”. This is in settings —> settings —> Transcoder.
“Use hardware acceleration when available” = encode and decode to to hardware-accelerated video codecs
“Use hardware accelerated video encoding” = use hardware acceleration for the encoding / decoding
https://support.plex.tv/articles/200250347-transcoder/

Good article here: https://medium.com/@MrNick4B/plex-on-docker-on-synology-enabling-hardware-transcoding-fa017190cad7
Plex instructions here: https://github.com/plexinc/pms-docker#intel-quick-sync-hardware-transcoding-support

There is one addition you need to make to the docker-compose.yaml file
    devices:
      - "/dev/dri:/dev/dri"
I did also switch to the plexpass tag: plexinc/pms-docker:plexpass. Not sure if that is necessary or not.

As others have noted, using CPU transcoding, my CPU usage is around 100%, but after HW decoding gets enabled, I see it drop to ~35%.
https://medium.com/@MrNick4B/plex-on-docker-on-synology-enabling-hardware-transcoding-fa017190cad7

If this doesn’t work, some starting points for debugging is to search the logs for “transcoding”, “error”, or “ffmpeg”. You can find the logs at `docker logs plex`, settings —> manage —> console, and settings —> manage —> Troubleshooting.



Tautulli
Next up is moving tautuilli. They have two good FAQ questions on their wiki:
https://github.com/Tautulli/Tautulli/wiki/Frequently-Asked-Questions#q-i-moved-media-in-plex-now-tautulli-is-linking-to-the-wrong-itemshowing-up-twice
https://github.com/Tautulli/Tautulli/wiki/Frequently-Asked-Questions#q-i-need-to-movereinstall-tautulli-can-i-keep-my-history-and-statistics

Basically, you need to go into tautulli, settings, download your database and config.

I created a new tautulli user in DSM that only had access to docker file mount share thing
I got its user id and group id with id -u tautulli and id -g tautulli.
Mount the database and config in /config
Timezone is AMErica/Denver
Then you can launch tautulli with docker compose. It will appear at NAS_IP:8181
Once you’re in tautulli, go into settings —> Plex Media Server. We will need to connect a new server. To do this, click on “Fetch New Token”, sign in. Then the rest might auto populate? If not, put in the IP of your NAS, port, and I checked “use secure connection” because why not?

Then I streamed a few videos in Plex and saw it show up in tautulli so I think we’re good to go!
Obviously if you are importing a database and config, you’re going to want to see the history tab populated just as it was. That will tell you if you exported and imported it correctly.








It is recommended to enable the QuickConnect relay service at Control Panel > External Access > QuickConnect > Advanced Settings


