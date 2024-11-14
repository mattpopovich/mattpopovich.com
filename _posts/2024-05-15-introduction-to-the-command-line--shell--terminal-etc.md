---
title: "Introduction to the Terminal / Shell / Command Line, etc."
author: matt_popovich           # Reference author_id in _data/authors.yml
# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries
date: 2024-05-15 03:31:28 -0600
categories: [Blog, Not YouTube]    # <=2 values here: top category and sub category
tags: [bash, big sur, catalina, cli, how to, linux, mac, monterey, osx, programming, tech]  # TAG names should always be lowercase
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
description: This post will take you from couch to the command line in 15mins!
---

## Disclaimer
*Command line*, *command prompt*, *shell*, *terminal*, *console*, etc. can sometimes be used interchangeably. I will be using them interchangeably in this article. Normally, they are all referring to a window in which you input text commands and receive text output.

There are **a lot** of intricacies in the terminal. You might call them ["quirks"](https://youtu.be/2aiopbNnyF8) or ["features"](https://youtu.be/BQ0mlXQezxE?si=ijwZunxB5kDFciGI). You will never learn them all and some of them still stump me to this day. Half of the battle is just knowing which features exist. If you know it exists (even though you might not remember exactly how to use a feature), any search engine will get you there ("*How do I copy a file in the terminal*"). If you can think it, someone has probably done it in the terminal.

Also, the terminal does not add a newline between commands. I have added that in hopes of making things easier to read.

## Opening the Terminal
The terminal is opened differently depending on your operating system:
* Windows
  * Search for the program "*Command Prompt*"
* Mac
  * Search for the program "*Terminal.app*"
* Linux
  * Search for the program "*Terminal*"
  * Or via the keyboard shortcut `ctrl` + `alt` + `t`

> Note that **most** of this post will not work in Windows' Command Prompt. The Command Prompt uses a different language compared to Mac and Linux's terminals. See [this answer](https://superuser.com/a/349514/552207) for additional information.
{: .prompt-danger }

More detailed information via [effective-shell.com](https://effective-shell.com/part-1-transitioning-to-the-shell/getting-started/#opening-the-shell) (with pictures!).

## How to Use
The terminal is made up of three possible things:
```console
$ program -flags arguments
```

A `$` or `#` are common hints that this line is meant to be ran in a terminal

* `program` is a small executable that resides on your system
  * *Required*
  * Most common ones can be found in `/bin`
  * Also referred to as: *executable*, *script*, *binary*, *command*, etc.
* `flags` are normally either one letter or a full word that activate certain capabilities in a program
  * *Optional*
* `arguments` are information given to a program for it to act upon (just like function arguments)
  * *Optional*
  * Sometimes shortened to just *args*

The terminal **is** case-sensitive.

## Example Use
### <big>**ls**</big>
`ls` = *a program used to **l**i**s**t files*
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

<!-- TODO: Link to intermediate guide for `du` usage -->
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
Note how the size of the files changed from being displayed in bytes to being converted to **B**, **K**B, **G**B, etc.

If we were only interested in one specific file or folder, we can give `ls` an argument for which file or folder to list:

```console
$ ls -lh Documents
-rw-r--r--@  1 mattpopovich  staff   774K Oct  1  2022 img1.png
-rw-r--r--@  1 mattpopovich  staff   399K Oct  1  2022 img2.png
-rw-r--r--@  1 mattpopovich  staff   404K Oct  1  2022 img3.png

$ ls -lh Documents/img1.png
-rw-r--r--@  1 mattpopovich  staff   774K Oct  1  2022 img1.png
```

Note that this showed us the *contents* of what was inside that folder, or if it was a file, it showed us information about **only** that file.

If we wanted to see more detailed information about a folder (without listing its contents), we can use the `-d` flag:

```console
$ ls -lhd Documents
drwx------@ 32 mattpopovich  staff   1.0K Jul 19  2023 Documents

$ ls -l -h -d Documents
drwx------@ 32 mattpopovich  staff   1.0K Jul 19  2023 Documents
```

Here, we add the `-d` flag to tell `ls` to show us information about the ***d**irectory* (and not what is *inside the directory*) named `Documents`. Also note that single character flags can be together (`-lhd`) or separate (`-l -h -d`).


### <big>**man**</big>

`man` = *Display **man**ual documentation pages*

Before we go too much further, I should mention the `man` command.
> [Give a man a fish, and you feed him for a day. Teach a man to fish, and you feed him for a lifetime.](https://quoteinvestigator.com/2015/08/28/fish/)

This command displays documentation for the argument you pass to it. This is what it looks like if you run it with an argument of `ls` (the command I explained above):

```console
$ man ls
LS(1)                     General Commands Manual                    LS(1)

NAME
     ls – list directory contents

SYNOPSIS
     ls [-@ABCFGHILOPRSTUWabcdefghiklmnopqrstuvwxy1%,] [--color=when]
        [-D format] [file ...]

DESCRIPTION
     For each operand that names a file of a type other than directory, ls
     displays its name as well as any requested, associated information.
     For each operand that names a file of type directory, ls displays the
     names of files contained within that directory, as well as any
     requested, associated information.

     If no operands are given, the contents of the current directory are
     displayed.  If more than one operand is given, non-directory operands
     are displayed first; directory and non-directory operands are sorted
     separately and in lexicographical order.

     The following options are available:


     -@      Display extended attribute keys and sizes in long (-l)
             output.

     -A      Include directory entries whose names begin with a dot (‘.’)
             except for . and ...  Automatically set for the super-user
             unless -I is specified.

     -B      Force printing of non-printable characters (as defined by
             ctype(3) and current locale settings) in file names as \xxx,
             where xxx is the numeric value of the character in octal.
             This option is not defined in IEEE Std 1003.1-2008
             (“POSIX.1”).
[...]
```

Note that once you run `man`, a new "window" in the terminal opens. You can advance to the next line with the enter key, up and down errors, or even scrolling (if enabled). Press `q` (quit) to exit. `q` to exit is [common in other programs (`vi`)](#vi--vim) as as we will find out.

If you scroll down in that `man` page, you will find information about the flags that I explained above:
```console
     -d      Directories are listed as plain files (not searched recursively).
    [...]
     -h      When used with the -l option, use unit suffixes: Byte, Kilobyte,
             Megabyte, Gigabyte, Terabyte and Petabyte in order to reduce the
             number of digits to four or fewer using base 2 for sizes.  This
             option is not defined in IEEE Std 1003.1-2008 (“POSIX.1”).
    [...]
     -l      (The lowercase letter “ell”.) List files in the long format,
             as described in the The Long Format subsection below.
```

I will leave the other flags as an [exercise for the reader](http://www.mathmatique.com/articles/left-exercise-reader) 😉

### <big>**glob**</big>

Something else that's neat about the terminal is that it's created *by programmers, for programmers*. It has a lot of very powerful "shortcuts" that can be used. For example:

```console
$ ls -ld D*
drwxr-xr-x+  44 mattpopovich  staff   1408 Apr 15 20:37 Desktop
drwx------@  32 mattpopovich  staff   1024 Jul 19  2023 Documents
drwx------@ 430 mattpopovich  staff  13760 May 14 10:08 Downloads
```

Here, we use the [glob](https://en.wikipedia.org/wiki/Glob_(programming)) wildcard `*` to list all directories that start with `D`.
Very handy whenever you are in a folder with lots of files!

Also worth noting that the terminal supports **tab completion**!! This is a lifesaver and can save tons of time (particularly when typing in long filenames). Basically, whenever you are typing a command or a file path, just press `tab` in the middle of the word and if the terminal finds a match for it, it will auto-complete the rest of the word. If there are multiple words that would match the completion, pressing `tab` twice will show all possible matches.

```console
$ ls D<tab><tab>
Desktop/    Documents/  Downloads/

$ ls Do<tab><tab>
Documents/  Downloads/

$ ls Doc<tab>
$ ls Documents
```

### <big>**pwd**</big>
`pwd` = ***p**resent **w**orking **d**irectory*

This command tells you where your terminal session is currently located:

```console
$ pwd
/users/mattpopovich
```

### <big>**cd**</big>

`cd` = ***c**hange **d**irectory*

Your terminal will normally show what directory you are currently in before each command. (I won't always show it in this post unless I think it is needed). This helps keep you oriented to what folder you are currently operating in!

The `cd` command lets you **c**hange which **d**irectory you are currently located in:

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

Notice that `/users/mattpopovich` is being displayed as `~`. Also note that we went "up" to the parent folder via `cd ..` instead of `cd /users/mattpopovich`.

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

This command will make an empty directory/folder with a name of the argument that you specify:

> Note that `#` denotes the beginning of a "comment". Anything after `#` is [ignored by the terminal](https://phoenixnap.com/kb/bash-comment). I'm using it below to help give additional context.
{: .prompt-info }

```console
$ ls -l
total 0
-rw-r--r--  1 mattpopovich  staff  0 Feb 31 20:42 test_file.txt

$ mkdir test_folder

$ ls -l               # Confirming that a new folder was created!
total 0
-rw-r--r--  1 mattpopovich  staff   0 Feb 31 20:42 test_file.txt
drwxr-xr-x  2 mattpopovich  staff  64 Feb 31 20:49 test_folder
```

### <big>**mv**</big>
`mv` = ***m**o**v**e files*

Now that we know how to make files and folders, let's learn how to customize things a bit.

This command will move the first argument to the second argument. `mv source destination`. It can be used to move files into a folder or even "rename" files by *moving* them to a new name.

Let's move some files around:

```console
$ ls
test_file.txt test_file2.txt test_file3.txt test_folder

$ ls test_folder              # Nothing printed below means the folder is empty

$ mv test_file.txt test_folder

$ ls test_folder              # test_file.txt was successfully moved into test_folder
test_file.txt

$ ls
test_file2.txt test_file3.txt test_folder

$ mv test_file* test_folder   # Move any file that starts with "test_file" into test_folder

$ ls
test_folder

$ ls test_folder              # We have moved all of our files into test_folder
test_file.txt test_file2.txt test_file3.txt
```

You can also specify more than one source and they will all be moved to the destination `mv source1 source2 destination`:

```console
$ ls
test_file.txt test_file2.txt test_file3.txt test_folder

$ mv test_file.txt test_file2.txt test_file3.txt test_folder

$ ls test_folder
test_file.txt test_file2.txt test_file3.txt
```
Here, we accomplished the same effective thing but without the glob from above (`mv test_file* test_folder`). Although I would argue that the glob was probably easier.

Now, let's rename some files (by moving them to a new name):

```console
$ ls
test_folder

$ ls test_folder
test_file.txt

$ mv test_folder testing_folder

$ ls                    # Confirming successful "rename"
testing_folder

$ ls testing_folder     # Folder contents hasn't changed
test_file.txt
```

### <big>**cp**</big>
`cp` = ***c**o**p**y files*

This is used the same as the `mv` command above, but it copies the files instead of moving them.

This command will copy the first argument to the second argument. `cp source destination`:

```console
$ ls
test_file.txt test_file2.txt test_file3.txt test_folder

$ ls test_folder

$ cp test_file.txt test_folder    # Copy test_file.txt into test_folder

$ ls
test_file.txt test_file2.txt test_file3.txt test_folder

$ ls test_folder                  # Copy was successful, test_file.txt is in both locations
test_file.txt

$ cp test_file* test_folder       # Copy all files that begin with test_file to test_folder

$ ls
test_file.txt test_file2.txt test_file3.txt test_folder

$ ls test_folder                  # Copy was successful
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

$ ls
test_folder

$ rm test_folder
rm: test_folder: is a directory

$ rm -d test_folder   # -d flag will remove an empty directory

$ ls

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

$ rm -r test_folder   # -r flag will remove a non-empty directory

$ ls
file1
```

### <big>**cat**</big>

`cat` = *con**cat**enate and print files*

This command will print the contents of a file

```console
$ ls -lh
-rw-r--r--  1 mattpopovich  staff    38B Nov 13 18:50 test_file.txt

$ cat test_file.txt
This is the contents of test_file.txt
```

## Text Editors

There are multiple "editors" available to use in the command prompt. Engineers will have their own (sometimes strong) preference as to which one you should use. I just use `vi` and for no particular reason other than I know how to use it and I don't use it enough to warrant learning other editors.
The other major editors are [`emacs`](https://www.digitalocean.com/community/tutorials/how-to-use-the-emacs-editor-in-linux) and [`nano`](https://www.geeksforgeeks.org/nano-text-editor-in-linux/).

### <big>**vi / vim**</big>

`vi` = ***vi**sual*

`vim` = ***vi** i**m**proved*

```console
$ ls

$ vi text_file.txt
```

After typing `vi text_file.txt` and hitting `enter`, we are kicked into the editor. It can be a little daunting at first but here are some of `vi`s commands. These are entered in once `vi` is open. These are not command line arguments.
* `i` = go into "insert" mode
  * After pressing `i` on the keyboard, you can now type and modify text in the file
  * You can tell you are in insert mode by the `-- INSERT --` text at the bottom of your screen
* `Esc` = exit "insert" mode
  * When you are out of insert mode, you can type commands but cannot modify text
* `vi` commands
  * `/` = search for text
    * Ex. `/text` + `Enter` will bring you to the next occurrence of `text` in the file
    * Then press `n` to go to the next occurrence of `text` in the file
    * Or press `N` to go to the previous occurrence of `text` in the file
  * `gg` = go to the first line in the file
  * `GG` = go to the last line in the file
  * `dd` = delete the current line that the cursor is on
  * `:q` = quit the file
  * `:q!` = quit the file and discard changes
  * `:wq` = save the file (write to disk) and then quit

Additional commands can be found [here](https://www.cs.colostate.edu/helpdocs/vi.html).

If it is installed on your system, you should try to run the `vimtutor` command from your terminal, which will start a tutorial of the basic Vim commands. [Thanks, Stack Overflow](https://stackoverflow.com/a/6607635/4368898)!

## Additional Resources
* [effective-shell.com](https://effective-shell.com/)
  * Very in depth + includes pictures!

## Outro
These are the *very basics* of the terminal. My next post will touch on more *intermediate* features for the terminal.
Be sure to check back for that!
