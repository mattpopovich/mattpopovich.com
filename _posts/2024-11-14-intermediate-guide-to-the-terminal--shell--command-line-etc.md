---
title: "Intermediate guide to the Terminal / Shell / Command Line, etc."
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2024-11-14 00:48:07 -0600
categories: [Blog, Not YouTube]    # <=2 values here: top category and sub category
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
#description:               # A short sentence to describe the article, used when sharing links on social media
---

## Intro
This guide is a continuation on my previous blog post, ["Introduction to the Terminal / Shell / Command Line, etc."](https://mattpopovich.com/posts/introduction-to-the-command-line-shell-terminal-etc/).

## Environment variables

An environment variable is a variable that is used to hold some value specific to the operating system. Programs can refer to these environment variables and no matter who is logged in to the system or what operating system they are running, the program can be assured that the variable will reference the correct location.

Some of the more common environment variables are `PATH`, `HOME`, `USER`, and `SHELL`. There are many more than this, but these are a few of the more popular environment variables.

While I didn't touch on it above, the `echo` command is used to print out whatever argument you give it. One of its more common uses is to print out the value of an environment variable. To tell your terminal that you are referencing a variable (and not just some string of text), use the dollar sign, `$`.

```console
$ echo HOME     # Prints out just a string of text
HOME
$               # Your shell will replace `$HOME` with the environment variable
$ echo $HOME    # for `HOME`, then echo will print it out
/users/mattpopovich
```

As an example of how these values might be specific to the user or operating system, imagine a different user, [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds), is logged in. Their `HOME` might change as such:

```console
$ echo $HOME
/users/linustorvalds
```

Now, for example, a program that might want to store a file in a user's Downloads folder could reference it as `$HOME/Downloads`, which would be valid no matter which user was logged in!

To see all of the environment variables that are currently defined, you can run the `env` command:
```console
$ env
USER=mattpopovich
PATH=/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:[...]
HOME=/Users/mattpopovich
SHELL=/bin/zsh
TMPDIR=/var/folders/3g/5d7zlfqs26j779y3tf0l4llr0000gn/T/
[...]
```

## Return values
Notice that with all the commands we've ran, when they are successful, they largely don't display anything (unless when that is their job, such as `ls`). This is by design. No output is typically indicative of success while output is typically signs that something went wrong.

Each command ran in the terminal returns a value. This value is set in the variable `?` and can be displayed via `echo $?`. Successful terminal commands return `0`. Failed terminal commands return a non-zero value.

```console
$ ls
test_file.txt test_folder
$ echo $?             # Successful ls command
0
$ rm test_file.txt
$ echo $?             # Successful rm command
0
$ rm test_file.txt
rm: test_file.txt: No such file or directory
$ echo $?             # Attempting to remove a file that does not exist will be a "failed command"
1
$ rm test_folder
rm: test_folder: is a directory
$ echo $?             # Attempting to remove a directory without the -d flag will be a "failed command"
1
$ ls
test_folder
```

## Programs are in your path
TODO

## Hidden files
Hidden files in Linux are any files that begin with a period.

```console
~ $ ls
Applications   Movies
Desktop        Music
Documents      Pictures
Downloads
~ $ ls -a
.aliases       .bash_history
.bashrc        .bashrc_popovichm
Applications   Movies
Desktop        Music
Documents      Pictures
Downloads
```

## `.bashrc` file
TODO


## Different shells
Your terminal loads a default shell upon opening. On Ubuntu/linux, it is normally `bash`. OSX has recently left `bash` and went to `zsh` as its default. `sh` is an extremely bare bones shell that is almost always available on any system. Some more fancy shells are `oh my zsh` and `fish`.

### Shells are also programming languages


```console
$ cat hello_world.sh
#!/bin/bash
echo "Hello World"

$ ./hello_world.sh
Hello World
```


## Linux Directory Structure

![Cheatsheet](https://linuxhandbook.com/content/images/size/w1000/2020/06/linux-system-directoies-poster.png)

More detailed information on what is in these folders can be found on [linuxhandbook.com](https://linuxhandbook.com/linux-directory-structure/).

## Navigating the command line
Pressing and holding the arrow keys to move around the command line is slow and inefficient. Remember, we're programmers. If there is something that is slow and inefficient, chances are that someone has a fix.

The main ones that I use are:
* Ctrl + u = Delete everything before your cursor
* Ctrl + left = Move cursor one word to the left
* Ctrl + right = Move cursor one word to the right

![A visual explanation of shortcuts to navigate the command line](https://effective-shell.com/assets/images/command-line-a47c08acd86b732173b3f6dfc1955bb1.png)


## Other helpful commands

For now, I think the above is a good set for beginners to get started in the terminal.
As I have time, I will explain more of these commands, maybe in another post as to not make this post longer than it needs to be.

This is the next set that I plan on explaining:

* `cd -`
* `--help` = help
* `grep`
  * `grep -rnw`
* `cat`
* `head`
* `tail`
* `| = pipe`
* `find`
  * `find . -name`
* `exit`
* `ssh`
* `scp`
* `tmux`
* `history`
* `cmd+R`
* `echo`
* `which`
* `!!`
* `source`
* `chmod`
* `chown`
* `tar`
  * <https://xkcd.com/1168/>
  * <https://www.explainxkcd.com/wiki/index.php/1168:_tar>
* `zip`
* `ifconfig`
* `wc`
* `where`
* `curl`
* `su` = switch user
* `rsync`
* Multiple commands; on one line
* `whoami`
* `bg`, `fg`
* `ctrl+c`, `ctrl+\`, `ctrl+z`

## Bonus: The command line is sexy
Just an example of some of the commands available:
* date
* unzip
* touch
* strip
* mount
* yes
* uptime
* umount
* sleep

![Image of the commands from above](https://pics.livejournal.com/jbauernberger/pic/00022sxk/s320x240)


















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
