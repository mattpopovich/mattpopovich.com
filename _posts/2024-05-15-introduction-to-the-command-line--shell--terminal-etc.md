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

# Intro to the Terminal

## Disclaimer
*Command line*, *command prompt*, *shell*, *terminal*, *console*, etc. can sometimes be used interchangeably. Normally, they are all referring to a window in which you input text commands and receive text output.

There are **a lot** of intricacies in the terminal. You might call them ["quirks"](https://youtu.be/2aiopbNnyF8) or ["features"](https://youtu.be/BQ0mlXQezxE?si=ijwZunxB5kDFciGI). You will never learn them all and some of them still stump me to this day. However, most of the terminal follows the same general pattern:

## How to Use
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

## Example Use
### `ls`
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

> Note that this gives you the size of the file. This does not give you the size of the files in the folder!! (Use `du` for that)
{:.prompt-warn}

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

### `cd`

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

Notice that `/users/mattpopovich` is being displayed as `~`.

### `man`

`man` = *Display **man**ual documentation pages*

This command displays documentation for the argument you pass to it.

```console
$ man ls
LS(1)                                      General Commands Manual                                      LS(1)

NAME
     ls – list directory contents

SYNOPSIS
     ls [-@ABCFGHILOPRSTUWabcdefghiklmnopqrstuvwxy1%,] [--color=when] [-D format] [file ...]

DESCRIPTION
     For each operand that names a file of a type other than directory, ls displays its name as well as any
     requested, associated information.  For each operand that names a file of type directory, ls displays
     the names of files contained within that directory, as well as any requested, associated information.

     If no operands are given, the contents of the current directory are displayed.  If more than one operand
     is given, non-directory operands are displayed first; directory and non-directory operands are sorted
     separately and in lexicographical order.

     The following options are available:

     -@      Display extended attribute keys and sizes in long (-l) output.

     -A      Include directory entries whose names begin with a dot (‘.’) except for . and ...  Automatically
             set for the super-user unless -I is specified.

     -B      Force printing of non-printable characters (as defined by ctype(3) and current locale settings)
             in file names as \xxx, where xxx is the numeric value of the character in octal.  This option is
             not defined in IEEE Std 1003.1-2008 (“POSIX.1”).
[...]
```

Note that once you run `man`, a new "window" in the terminal opens. You can navigate it with the enter key, up and down errors, or even scrolling (if enabled). Press `q` (quit) to exit. `q` to exit is common in other programs as well (`vi`) as we will find out.

### `touch`

`touch` = change file access and modification times

Personally, I never use this command for its intended purpose. I only use it for creating new, empty files.

```console
$ man touch
[...]
The touch utility sets the modification and access times of files.  If any file does not exist, it is
     created with default permissions.
[...]
$ ls
$ touch test_file.txt
$ ls -l
total 0
-rw-r--r--  1 mattpopovich  staff  0 Feb 31 20:42 test_file.txt
```

### `mkdir`

`mkdir` = ***m**a**k**e **dir**ectories*

```console
$ ls -l
total 0
-rw-r--r--  1 mattpopovich  staff  0 Feb 31 20:42 test_file.txt
$ mkdir test_folder
$ ls -l
total 0
-rw-r--r--  1 mattpopovich  staff   0 Feb 31 20:42 test_file.txt
drwxr-xr-x  2 mattpopovich  staff  64 Feb 31 20:49 test_folder
```

### `mv`
`mv` = ***m**o**v**e files*

Now that we know how to make files and folders, let's learn how to customize things a bit.

```console
$ ls
test_file.txt test_file2.txt test_file3.txt test_folder
$ ls test_folder
$ mv test_file.txt test_folder
$ ls
test_file2.txt test_file3.txt test_folder
$ ls test_folder
test_file.txt
$ mv test_file* test_folder
$ ls
test_folder
$ ls test_folder
test_file.txt test_file2.txt test_file3.txt
```

The `mv` command can also be used to effectively rename files and folders (by moving them to a new name)

```console
$ ls
test_folder
$ ls test_folder
test_file.txt
$ mv test_folder testing_folder
$ ls
testing_folder
$ ls testing_folder
test_file.txt
```

### `cp`
`cp` = ***c**o**p**y files*

This is used the same as the `mv` command above, but it copies the files instead of moving them.

```console
$ ls
test_file.txt test_file2.txt test_file3.txt test_folder
$ ls test_folder
$ cp test_file.txt test_folder
$ ls
test_file.txt test_file2.txt test_file3.txt test_folder
$ ls test_folder
test_file.txt
$ cp test_file* test_folder
$ ls
test_file.txt test_file2.txt test_file3.txt test_folder
$ ls test_folder
test_file.txt test_file2.txt test_file3.txt
```

### `rm`
`rm` = ***r**e**m**ove*
* `-d` = remove **d**irectory
* `-R` = **r**ecursively remove things in a directory. Implies the **-d** option
* `-r` = Equivalent to `-R`

This command will remove files and folders

```console
$ ls
test_file.txt test_folder
$ ls test_folder
$ rm test_file.txt
test_folder
$ rm test_folder
rm: test_folder: is a directory
$ rm -d test_folder
```

```
$ ls
file1 test_folder
$ ls test_folder
file2
$ ls *
file1

test_folder:
file2
$ rm -d test_folder
rm: test_folder: Directory not empty
$ rm -r test_folder
$ ls
file1
```

### Other helpful commands

* --help = help
* grep
* cat
* head
* tail
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
* bg, fg
* ctrl+c, ctrl+\, ctrl+z


## Return values
Notice that with all the commands we've ran, when they are successful, they largely don't display anything (unless when that is their job, such as `ls`). This is by design. No output is typically indicative of success, output is typically signs that something went wrong.

```console
$ ls
test_file.txt test_folder
$ rm test_file.txt
$ rm test_file.txt
rm: test_file.txt: No such file or directory
$ rm test_folder
rm: test_folder: is a directory
$ ls
test_folder
```

## Interactive Commands

There are multiple "editors" available to use in the command prompt. Engineers will have their own (sometimes strong) preference as to which one you should use. I just use `vi` and for no particular reason other than I know how to use it and I don't use it enough to warrant learning other editors.

### `vi` / `vim`

`vi` = ***vi**sual*
`vim` = ***vi** i**m**proved*

```console
$ ls
$ vi text_file.txt
```

From here, we are kicked into the editor. It can be a little daunting at first but here are some of its commands. These are entered in once `vi` is open. These are not command line arguments.
* `i` = go into "insert" mode

Additional commands can be found [here](https://www.cs.colostate.edu/helpdocs/vi.html).



Environment variables

.bash_rc

Hidden files

Different shells

Programs are in your path

Tab complete

ctrl+w, ctrl+u, ctrl+left, ctrl+right

