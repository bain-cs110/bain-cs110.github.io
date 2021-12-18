---
layout: module
title: The Building Blocks
type: lecture
draft: 0
num: 3
description:
  - Variables, operators, data types, and built-in functions
due_date: 2021-09-27
quiz_url: https://canvas.northwestern.edu/courses/149580/quizzes/159822
slides:
  - url: https://docs.google.com/presentation/d/1rjHRfrfsbNbci_MMHUsJs-hodKI7_aczBGyoAKaRZrU/edit?usp=sharing
    title: The Building Blocks of Programming
  - url: https://docs.google.com/presentation/d/1XoHhmxBghe_x6JFufFkdXy7CvTFIivjOp-d9FoEMGZ8/edit?usp=sharing
    title: Live Lecture Activities
videos:
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=5e8668ba-7ecd-406c-95a3-adab0002be9f
     duration: |
        10:51
     title: Using the Lecture Files
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=51f44ad7-0088-450f-8c39-adab0002be00
     duration: |
        17:04
     title: Data Types & Variables
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=3df68939-9ec8-4adb-9c21-adab0002c2b6
     title: Operators
     duration: |
        08:36
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=ad65b34b-7ed1-4f50-a483-adab0002c20f
     title: Built-in Functions
     duration: |
        13:31
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=4a328a1a-e767-405f-9689-adb000f6a564
     live: 1
     title: Practice with variables, constants, & operators
     duration: "44:28"

readings:
  - title: "Ch2: Variables"
    author: "Severance"
    url: https://www.py4e.com/html3/02-variables
    video_url: https://www.py4e.com/lessons/memory
  - title: "Ch2: Variables"
    author: "Heinold"
    url: https://www.brianheinold.net/python/A_Practical_Introduction_to_Python_Programming_Heinold.pdf

extras:
  - title: "Tutorial Signups"
    comments: "You MUST sign up for a tutorial session. This week's tutorial is mandatory."
    url: "https://docs.google.com/spreadsheets/d/1n9io9LSvSR_IolYRnwMluJ2Eq_qFN7uhGFRBMQVzvec/edit?usp=sharing"
    external: 1

exercise_url: "lecture03.zip"
---

<img class="module-image" src="/fall2021/assets/images/lectures/lecture_02_blocks.jpg" />Python (and all programmming languages) are made up of very small "words" (like nouns and verbs) that can be composed into meaningful "sentances" (i.e. code blocks that do something useful). Today we are going to review some of the basic building blocks of code, including data types, operators, and variables.<br><br>In addition to the lectures and videos, there are also some sample python files that you will need to download and run (using IDLE). If, for any reason, you are having trouble installing IDLE (instructions can be found in the first part of [homework 1](../assignments/hw1)), reach out to your TA or sign-up for an office hours session. Please keep your files organized (as explained in hw01). I recommend a folder structure like this:

```
cs110
    |-- homework
    │   |-- hw01
    │   |-- hw02
    |   ...
    |-- lectures
    │   -- lecture01
    │   -- lecture02
    │   ...
    |-- tutorials
        |-- tutorial01
        |-- tutorial02
        ...
```