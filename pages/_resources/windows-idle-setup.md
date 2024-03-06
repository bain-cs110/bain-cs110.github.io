---
layout: default
title: Windows IDLE Setup
draft: 0
description: Making IDLE the default editor for .py files on Windows
ordering: 99
canvas_title: Windows IDLE Setup
canvas_id: windows-idle-setup
---

Unfortunately, this is a multi-step process.

## Step 1. Showing Hidden Files

First we need to ask Windows to show to us all hidden files and folders. First open a File Explorer window. Click on the <code>View</code> button, then click on <code>Show</code> and click on <code>Hidden item</code>. A checkbox will appear.

<img style="width:50%;" a="Screenshot of show hidden items" src="{{site.url}}/assets/images/windows/windows-1.png">

## Step 2. Modifying the Default App

Now we need to open up the <code>Settings</code> application. Once there, click on the <code>Apps</code> menu, then click on <code>Default apps</code>.

<img style="width:50%;" a="Screenshot of Settings app" src="{{site.url}}/assets/images/windows/windows-2.png">

<img style="width:50%;" a="Screenshot of Apps tab" src="{{site.url}}/assets/images/windows/windows-3.png">

<img style="width:50%;" a="Screenshot of Default Apps tab" src="{{site.url}}/assets/images/windows/windows-4.png">


In the box that says "enter a file type or link type" type <code>.py</code> and select it from the resulting dropdown. Then click on the box right below. A popup window will appear. Scroll to the bottom of the window and select <code>Chose an app on your PC</code>.

<img style="width:50%;" a="Screenshot of default app popup" src="{{site.url}}/assets/images/windows/windows-5.png">

In the resulting window, you need to navigate to your user folder. 
* Click on <code>This PC</code> in the left hand menu, then <code>Local Disk</code> (the <code>C:</code> drive).
* Double click on the <code>Users</code> folder.
* Double click on the folder that shows your user name.
* Double click on the <code>AppData</code> folder (if it doesn't show, make sure you followed Step 1).
* Double click on the <code>Local</code> folder.
* Double click on the <code>Programs</code> folder.
* Double click on the <code>Python</code> folder.
* Double click on the folder with the highest number of Python version.
* Double click on the <code>Lib</code> folder.
* Double click on the <code>idlelib</code> folder (annoyed yet?).
* Double click on the <code>idle</code> "batch" file.

**Make sure to click <code>Set Default</code> or you'll have to repeat all of those steps!** 

Ta dah! You're all done. Now when you double click on a <code>.py</code> file it'll open in IDLE.
