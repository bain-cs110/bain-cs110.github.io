---
layout: default
title: Using PIP
canvas_id: using-pip
ordering: 99
---

## If you have a Windows machine
If you have a Windows Machine, there are (at least) two ways to ensure that python3 and PIP work when you run them from the command prompt. Note: this is an either -or- thing (e.g. you shouldn’t have to do Option 2 unless Option 1 doesn’t work).

### Option 1: Run the Installer Again

In our opinion, the easiest way to get python to work on your command prompt is to run the Python3 installer again and make sure that the checkbox at the very bottom that says Add Python 3.x (the screenshots show Python 3.7 but this applies to all Python installations) to PATH is checked:

<img alt="Command Prompt Windows Installer" class="small frame" src="{{site.url}}/assets/images/lectures/01-command-prompt-windows-installer.png" />

### Option 2: Go to System Preferences and Manually Add the PATH

To go this route, you will complete three steps:

### Step 1

Search for Edit the System Environment Variables (see below):

<img alt="Environment variables editor" class="medium frame" src="{{site.url}}/assets/images/lectures/02-environment-variables.png" />

### Step 2

You will then click the Environment Variables button in the Control Panel:

<img alt="Control Panel in Windows" class="small frame" src="{{site.url}}/assets/images/lectures/03-environment-variables.png" />

### Step 3

Finally, you will add the Scripts folder in their Python installation to their path (see 3rd screenshot). This looks different on everyone’s machine, so you will have to make sure that this PATH corresponds to your Python3 installation. This screenshot below is from one of the course TAs, but yours will look different.

<img alt="Scripts folder" class="medium frame" src="{{site.url}}/assets/images/lectures/04-environment-variables.png" />

* * *

## Command Line Cheatsheet

For your convenience, we have made you a little cheatsheet to help you get familiar with the command line. <a href="https://tutorial.djangogirls.org/en/intro_to_command_line/" target="_blank">Django Girls</a> is a good resource. Note: you will not be tested on this or anything, but navigating the command line can be useful.  DO NOT ENTER THE `>` or `$` symbols! Those are there automatically in Command Prompt and Terminal respectively.

<table class="instructions" style="border-top: solid 1px #444; border-bottom: solid 1px #444; border-collapse: collapse; width: 100%; margin-bottom: 30px;">
        <thead>
            <tr style="border-bottom: solid 1px #444;">
                <th scope="col" style="line-height: 1.5em; margin-top: 5px; vertical-align: top; border-bottom: dotted 1px #999; padding: 8px; text-align: left; font-size: 1em; min-width: 80px;">Idea</th>
                <th scope="col" style="line-height: 1.5em; margin-top: 5px; vertical-align: top; border-bottom: dotted 1px #999; padding: 8px; text-align: left; font-size: 1em; min-width: 80px;">DOS (Windows)</th>
                <th scope="col" style="line-height: 1.5em; margin-top: 5px; vertical-align: top; border-bottom: dotted 1px #999; padding: 8px; text-align: left; font-size: 1em; min-width: 80px;">Shell (Mac / Linux)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">What directory am I in?</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; cd</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ pwd</code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Change directories</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; cd </code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ cd </code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">List files &amp; directories</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; dir</code><br /><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; tree # lists subdirectories</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ ls</code><br /><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ ls -l</code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Navigate to parent directory</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; cd ..</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ cd ..</code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Navigate into child directory</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; cd cs110</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ cd cs110</code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Navigate into descendant directory</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; cd lectures\lecture_03</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ cd lectures/lecture_03</code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Navigate to sibling directory</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; cd ..\lecture_02</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ cd ../lecture_02</code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Navigate to ancestor directory</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; cd ..\..\</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ cd ../../</code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Navigate to home directory</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;">&nbsp;</td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ cd</code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Command history</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; doskey /HISTORY</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ history</code></td>
            </tr>
        </tbody>
    </table>
    <p>Other optional commands you may find useful&hellip;</p>
    <table class="instructions" style="border-top: solid 1px #444; border-bottom: solid 1px #444; border-collapse: collapse; width: 100%; margin-bottom: 30px;">
        <thead>
            <tr style="border-bottom: solid 1px #444;">
                <th scope="col" style="line-height: 1.5em; margin-top: 5px; vertical-align: top; border-bottom: dotted 1px #999; padding: 8px; text-align: left; font-size: 1em; min-width: 80px;">Idea</th>
                <th scope="col" style="line-height: 1.5em; margin-top: 5px; vertical-align: top; border-bottom: dotted 1px #999; padding: 8px; text-align: left; font-size: 1em; min-width: 80px;">DOS (Windows)</th>
                <th scope="col" style="line-height: 1.5em; margin-top: 5px; vertical-align: top; border-bottom: dotted 1px #999; padding: 8px; text-align: left; font-size: 1em; min-width: 80px;">Shell (Mac / Linux)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Create a new file</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; echo . &gt; my_file.txt</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ echo . &gt; my_file.txt</code><br /><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ touch my_file.txt</code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Append to a file</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; echo "some text" &gt;&gt; my_file.txt</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ echo "some text" &gt; my_file.txt</code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Save history to a file</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; doskey /HISTORY &gt; my_history.txt</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ history &gt; my_history.txt</code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Move a file</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; move my_history.txt Documents/.</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ mv my_history.txt Documents/.</code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Make a folder</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; mkdir my_folder</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ mkdir my_folder</code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Delete a file</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; del my_history.txt</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ rm my_history.txt</code></td>
            </tr>
            <tr>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><strong style="font-family: 'Akkurat Pro Regular';">Delete a folder</strong></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">&gt; rmdir my_folder</code></td>
                <td style="line-height: 1.5em; margin-top: 5px; vertical-align: top; font-family: 'Akkurat Pro Light'; border-bottom: dotted 1px #999; padding: 8px; font-size: 1em; min-width: 80px;"><code class="language-plaintext highlighter-rouge" style="margin-bottom: 20px; background: #F3F3F3; padding: 3px; border-radius: 6px;">$ rm -r my_folder</code></td>
            </tr>
        </tbody>
    </table>

* * *

## Using PIP

You can use `pip` to install three packages for P2: `sendgrid`, `requests`, and then to upgrade `certifi`. If `pip3` doesn't work on your computer, then try replacing `pip3` with `pip`. (If you're on Windows, you might also try `py -m pip install requests` and the same syntax to install the other libraries).

Open your Terminal (MacOS) or Command Prompt (Windows) and execute the following commands (from any directory)

```bash
pip3 install sendgrid                        # a module to interact with Twilio
pip3 install requests                        # a module for querying internet resources
pip3 install --upgrade certifi               # for SSL certificates
```