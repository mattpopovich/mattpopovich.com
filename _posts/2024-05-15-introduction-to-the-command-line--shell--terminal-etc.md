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
### <big>**ls**</big>
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
{: .prompt-warning }

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
$ ls -l -h -d Documents
drwx------@ 32 mattpopovich  staff   1.0K Jul 19  2023 Documents
```

Here, we add the `-d` flag to tell `ls` to show us information about the ***d**irectory* and not what is *inside the directory*. Also note that the flags can be together (`-lhd`) or separate (`-l -h -d`).

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

Also worth noting that the terminal supports **tab completion**!! This is a lifesaver and can save tons of time (particuarly when typing in long filenames). Basically, whenever you are typing a command or a file path, just press `tab` in the middle of the word and if the terminal finds a match for it, it will auto-complete the rest of the word. If there are multiple words that would match the completion, pressing `tab` twice will show all possible matches.

```console
$ ls D[tab]
Desktop/    Documents/  Downloads/
$ ls Do[tab]
Documents/  Downloads/
$ ls Doc[tab]
$ ls Documents
```

### Other programs
Here, I will be using the term *program* but note that there are again many terms that are sometimes used interchangeably: *program*, *executable*, *script*, *binary*, *command*, etc.

### <big>**pwd**</big>
`pwd` = ***p**resent **w**orking **d**irectory*

This command tells you where you terminal session is currently located

```console
/users/mattpopovich $ pwd
```

### <big>**cd**</big>

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

### <big>**man**</big>

`man` = *Display **man**ual documentation pages*

This command displays documentation for the argument you pass to it.

```console
$ man ls
LS(1)                          General Commands Manual                         LS(1)

NAME
     ls – list directory contents

SYNOPSIS
     ls [-@ABCFGHILOPRSTUWabcdefghiklmnopqrstuvwxy1%,] [--color=when] [-D format]
        [file ...]

DESCRIPTION
     For each operand that names a file of a type other than directory, ls displays
     its name as well as any requested, associated information.  For each operand
     that names a file of type directory, ls displays the names of files contained
     within that directory, as well as any requested, associated information.

     If no operands are given, the contents of the current directory are displayed.
     If more than one operand is given, non-directory operands are displayed first;
     directory and non-directory operands are sorted separately and in
     lexicographical order.

     The following options are available:

     -@      Display extended attribute keys and sizes in long (-l) output.

     -A      Include directory entries whose names begin with a dot (‘.’) except for
             . and ...  Automatically set for the super-user unless -I is specified.

     -B      Force printing of non-printable characters (as defined by ctype(3) and
             current locale settings) in file names as \xxx, where xxx is the
             numeric value of the character in octal.  This option is not defined in
             IEEE Std 1003.1-2008 (“POSIX.1”).
[...]
```

Note that once you run `man`, a new "window" in the terminal opens. You can navigate it with the enter key, up and down errors, or even scrolling (if enabled). Press `q` (quit) to exit. `q` to exit is common in other programs as well (`vi`) as we will find out.

### <big>**touch**</big>

`touch` = change file access and modification times

Personally, I never use this command for its intended purpose. I only use it for creating new, empty files.

```console
$ man touch
[...]
The touch utility sets the modification and access times of files.  If any file
     does not exist, it is created with default permissions.
[...]
$ ls
$ touch test_file.txt
$ ls -l
total 0
-rw-r--r--  1 mattpopovich  staff  0 Feb 31 20:42 test_file.txt
```

### <big>**mkdir**</big>

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

### <big>**mv**</big>
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

### <big>**cp**</big>
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

### <big>**rm**</big>
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

```console
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

TODO

* --help = help
* grep
  * grep -rnw
* cat
* head
* tail
* | = pipe
* find
  * find . -name
* exit
* ssh
* scp
* tmux
* history
* cmd+R
* echo
* which
* !!
* source
* chmod
* chown
* tar
  * https://xkcd.com/1168/
  * https://www.explainxkcd.com/wiki/index.php/1168:_tar
* zip
* ifconfig
* wc
* where
* curl
* rsync
* Multiple commands; on one line
* bg, fg
* ctrl+c, ctrl+\, ctrl+z

## Text Editors

There are multiple "editors" available to use in the command prompt. Engineers will have their own (sometimes strong) preference as to which one you should use. I just use `vi` and for no particular reason other than I know how to use it and I don't use it enough to warrant learning other editors.
The other major editors are `emacs` and `nano`.

### `vi` / `vim`

`vi` = ***vi**sual*
`vim` = ***vi** i**m**proved*

```console
$ ls
$ vi text_file.txt
```

From here, we are kicked into the editor. It can be a little daunting at first but here are some of its commands. These are entered in once `vi` is open. These are not command line arguments.
* `i` = go into "insert" mode
  * After pressing `i` on the keyboard, you can now type and modify text in the file
  * You can tell you are in insert mode by the `-- INSERT --` text at the bottom of your screen
* `Esc` = exit "insert" mode
  * When you are out of insert mode, you can type commands but cannot modify text
* `vi` commands
  * `/` = search for text
    * Ex. `/text` + `Enter` will bring you to the next occurrence of `text` in the file
    * Then press `n` to go to the next occurrence of `text` in the file
  * `gg` = go to the first line in the file
  * `GG` = go to the last line in the file
  * `dd` = delete the current line that the cursor is on
  * `:q` = quit the file
  * `:q!` = quit the file and discard changes
  * `:wq` = save the file (write to disk) and quit

Additional commands can be found [here](https://www.cs.colostate.edu/helpdocs/vi.html).

## Return values
Notice that with all the commands we've ran, when they are successful, they largely don't display anything (unless when that is their job, such as `ls`). This is by design. No output is typically indicative of success while output is typically signs that something went wrong.

Each command ran in the terminal returns a value. This value is set in the variable `?` and can be displayed via `echo $?`. Successful terminal commands return `0`. Failed terminal commands return a non-zero value.

```console
$ ls
test_file.txt test_folder
$ echo $?
0

$ rm test_file.txt
$ echo $?
0

$ rm test_file.txt
rm: test_file.txt: No such file or directory
$ echo $?
1

$ rm test_folder
rm: test_folder: is a directory
$ echo $?
1

$ ls
test_folder
```


## Environment variables
TODO

### Programs are in your path
TODO

## `.bashrc` file
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

## Additional Resources
* [effective-shell.com](https://effective-shell.com/)
  * Very in depth. If it were a book, it'd be 100s of pages.

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
