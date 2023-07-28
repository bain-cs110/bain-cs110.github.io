---
layout: default
title: Using PIP
permalink: /resources/pip/
---

## If you have a Windows machine
If you have a Windows Machine, there are (at least) two ways to ensure that python3 and PIP work when you run them from the command prompt. Note: this is an either -or- thing (e.g. you shouldn’t have to do Option 2 unless Option 1 doesn’t work).

### Option 1: Run the Installer Again

In our opinion, the easiest way to get python to work on your command prompt is to run the Python3 installer again and make sure that the checkbox at the very bottom that says Add Python 3.x (the screenshots show Python 3.7 but this applies to all Python installations) to PATH is checked:

<img class="small frame" src="{{site.url}}/assets/images/lectures/01-command-prompt-windows-installer.png" />

### Option 2: Go to System Preferences and Manually Add the PATH

To go this route, you will complete three steps:

### Step 1

Search for Edit the System Environment Variables (see below):

<img class="medium frame" src="{{site.url}}/assets/images/lectures/02-environment-variables.png" />

### Step 2

You will then click the Environment Variables button in the Control Panel:

<img class="small frame" src="{{site.url}}/assets/images/lectures/03-environment-variables.png" />

### Step 3

Finally, you will add the \Scripts folder in their Python installation to their path (see 3rd screenshot). This looks different on everyone’s machine, so you will have to make sure that this PATH corresponds to your Python3 installation. This screenshot below is from one of the course TAs, but yours will look different.

<img class="medium frame" src="{{site.url}}/assets/images/lectures/04-environment-variables.png" />

* * *

## Command Line Cheatsheet

For your convenience, we have made you a little cheatsheet to help you get familiar with the command line. <a href="https://tutorial.djangogirls.org/en/intro_to_command_line/" target="_blank">Django Girls</a> is a good resource. Note: you will not be tested on this or anything, but navigating the command line can be useful.  DO NOT ENTER THE `>` or `$` symbols! Those are there automatically in Command Prompt and Terminal respectively.

{:.instructions}
| | DOS (Windows) | Shell (Mac / Linux) |
|--|--|--|
| **What directory am I in?** | `> cd` | `$ pwd` |
| **Change directories** | `> cd {{your_file_path}}` | `$ cd {{your_file_path}}` |
| **List files & directories** | `> dir`<br> `> tree  # lists subdirectories` | `$ ls`<br>`$ ls -l` |
| **Navigate to parent directory** | `> cd ..` | `$ cd  ..` |
| **Navigate into child directory** | `> cd cs110` | `$ cd cs110` |
| **Navigate into descendant directory** | `> cd lectures\lecture_03` | `$ cd lectures/lecture_03` |
| **Navigate to sibling directory** | `> cd ..\lecture_02` | `$ cd  ../lecture_02` |
| **Navigate to ancestor directory** | `> cd ..\..\` | `$ cd  ../../` |
| **Navigate to home directory** |  | `$ cd` |
| **Command history** | `> doskey /HISTORY` | `$ history` |

Other optional commands you may find useful...

{:.instructions}
| | DOS (Windows) | Shell (Mac / Linux) |
|--|--|--|
| **Create a new file** | `> echo . > my_file.txt` | `$ echo . > my_file.txt`<br> `$ touch my_file.txt` |
| **Append to a file** | `> echo "some text" >> my_file.txt` | `$ echo "some text" > my_file.txt` |
| **Save history to a file** | `> doskey /HISTORY > my_history.txt` | `$ history > my_history.txt` |
| **Move a file** | `> move my_history.txt Documents/.` | `$ mv my_history.txt Documents/.` |
| **Make a folder** | `> mkdir my_folder` | `$ mkdir my_folder` |
| **Delete a file** | `> del my_history.txt` | `$ rm my_history.txt` |
| **Delete a folder** | `> rmdir my_folder` | `$ rm -r my_folder` |

* * *

## Using PIP

You can use `pip` to install three packages for P2: `sendgrid`, `requests`, and then to upgrade `certifi`. If `pip3` doesn't work on your computer, then try replacing `pip3` with `pip`. (If you're on Windows, you might also try `py -m pip install requests` and the same syntax to install the other libraries).

Open your Terminal (MacOS) or Command Prompt (Windows) and execute the following commands (from any directory)

```bash
pip3 install sendgrid                        # a module to interact with Twilio
pip3 install requests                        # a module for querying internet resources
pip3 install --upgrade certifi               # for SSL certificates
```