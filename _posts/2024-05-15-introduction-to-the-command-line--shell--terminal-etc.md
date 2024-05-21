---
title: "Introduction to the Terminal / Shell / Command Line, etc."
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2024-05-15 03:31:28 -0600
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
#description:               # A short sentence to describe the article, used when sharing links on social media
---

## Intro to the Terminal

### Disclaimer
*Command line*, *command prompt*, *shell*, *terminal*, *console*, etc. can sometimes be used interchangeably. Normally, they are all referring to a window in which you input text commands and receive text output.

There are **a lot** of intricacies in the terminal. You might call them ["quirks"](https://youtu.be/2aiopbNnyF8) or ["features"](https://youtu.be/BQ0mlXQezxE?si=ijwZunxB5kDFciGI). You will never learn them all and some of them still stump me to this day. However, most of the terminal follows the same general pattern:

### How to Use
The terminal is made up of three possible things:
```console
$ program -flags arguments
```

A `$` or `#` are common hints that this line is meant to be ran in a terminal

* `program` is a small executable that resides on your system
  * *Required*
  * Most common ones are in `/bin`
* `flags` are normally either one letter or a full word that activate certain capabilities in a program
  * *Optional*
* `arguments` are information given to a program for it to act upon (just like function arguments)
  * *Optional*

### Example
`ls` = *a program used to list files*
```console
$ ls
Applications   Movies
Desktop        Music
Documents      Pictures
Downloads
```

We can add the flag `-l` = *list files in the **l**ong format*

```console
$ ls -l
total 8
drwx------@   5 mattpopovich  staff          160 Nov  5  2021 Applications
drwxr-xr-x+  44 mattpopovich  staff         1408 Apr 15 20:37 Desktop
drwx------@  32 mattpopovich  staff         1024 Jul 19  2023 Documents
drwx------@ 430 mattpopovich  staff        13760 May 14 10:08 Downloads
drwx------   22 mattpopovich  staff          704 Apr  9 01:32 Movies
drwx------+   5 mattpopovich  staff          160 Oct 10  2022 Music
drwx------+   7 mattpopovich  staff          224 Apr 13 10:14 Pictures
```

`ls` supports multiple flags. We can also include `-h` = *list files in a more **h**uman readable format*

```console
$ ls -lh
total 8
drwx------@   5 mattpopovich  staff         160B Nov  5  2021 Applications
drwxr-xr-x+  44 mattpopovich  staff         1.4K Apr 15 20:37 Desktop
drwx------@  32 mattpopovich  staff         1.0K Jul 19  2023 Documents
drwx------@ 430 mattpopovich  staff          13K May 14 10:08 Downloads
drwx------   22 mattpopovich  staff         704B Apr  9 01:32 Movies
drwx------+   5 mattpopovich  staff         160B Oct 10  2022 Music
drwx------+   7 mattpopovich  staff         224B Apr 13 10:14 Pictures
```

Lastly, we can give `ls` an argument for which file or folder to list:

```console
$ ls -lhd Documents
drwx------@ 32 mattpopovich  staff   1.0K Jul 19  2023 Documents
```

Here, we add the `-d` flag to tell `ls` to show us information about the ***d**irectory* and not what is *inside the directory*.

Additionally, we tell `ls` to only show us information about the directory named *Documents*.

---

Something else that's neat about the terminal is that it's created *by programmers, for programmers*. It has a lot of very powerful "shortcuts" that can be used. For example:

```console
$ ls -ld D*
drwxr-xr-x+  44 mattpopovich  staff   1408 Apr 15 20:37 Desktop
drwx------@  32 mattpopovich  staff   1024 Jul 19  2023 Documents
drwx------@ 430 mattpopovich  staff  13760 May 14 10:08 Downloads
```

Here, we use a [glob](https://en.wikipedia.org/wiki/Glob_(programming)) wildcard `*` to list all directories that start with `D`.
Very handy whenever you are in a folder with lots of files!

### Other programs
Here, I will be using the term *program* but note that there are again many terms that are sometimes used interchangeably: *program*, *executable*, *script*, *binary*, *command*, etc.

`cd` = ***c**hange **d**irectory*

Your terminal will normally show what directory you are currently in before each command. This helps keep you oriented to what folder you are currently operating in!

```console
/users/mattpopovich $ ls
Applications   Movies
Desktop        Music
Documents      Pictures
Downloads
/users/mattpopovich $ cd Music
/users/mattpopovich/Music $ ls
01_Not_Like_Us-Kendrick_Lamar.mp3
/users/mattpopovich/Music $ cd /users/mattpopovich
/users/mattpopovich $ ls
Applications   Movies
Desktop        Music
Documents      Pictures
Downloads
/users/mattpopovich $ ls Music
01_Not_Like_Us-Kendrick_Lamar.mp3
```

Two important symbols in the shell are the tilde `~` and dot-dot `..`.
* `~` represents your home directory (`/users/mattpopovich`)
* `..` represents the parent directory

The above console session could also be (and most often is) represented by:
```console
~ $ ls
Applications   Movies
Desktop        Music
Documents      Pictures
Downloads
~ $ cd Music
~/Music $ ls
01_Not_Like_Us-Kendrick_Lamar.mp3
~/Music $ cd ..
~ $ ls
Applications   Movies
Desktop        Music
Documents      Pictures
Downloads
~ $ ls Music
01_Not_Like_Us-Kendrick_Lamar.mp3
```








* cd = change directory
* ls = list files
  * ll
  * Glob patterns
  * ..
* mv = move files
* cp = copy
* rm = remove
* man = manual
* help = help
* vi / vim
* grep
* cat
* head
* tail
* touch
* | = pipe
* find
* exit
* ssh
* scp
* tmux
* history
* cmd+R
* echo
* pwd = present working directory
* which
* !!
* mkdir
* source
* chmod
* chown
* tar
* zip
* ifconfig
* wc
* where
* curl
* rsync
* Multiple commands; on one line



Arguments

Environment variables

.bash_rcHidden filesDifferent shells

Programs are in your path

Tab complete

