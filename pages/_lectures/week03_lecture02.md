---
layout: module
title: "Functions and Tkinter"
type: lecture
description: "(Pre-Recorded Mini-Quiz 2)"
draft: 0
num: 5
lec_assignment: 1
canvas_assignment_group: "Mini-Quizzes"
canvas_points_possible: 10
canvas_allowed_extensions: "rkt"
canvas_submission_types: "external_tool"
canvas_id: 
canvas_title: Lecture 5 (Pre-Recorded) - Writing Functions - Mini-Quiz 2
exercise_url: "lecture05.zip"
due_date: 2024-01-17
videos:
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=b17b6042-bfd7-4866-9b78-b0f8004b2094
     title: "Introduction"
     duration: "7:05"
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d517a73c-5557-48fe-a199-b0f8004b20b9
     title: "Writing a Function"
     duration: "6:17"
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=97a738e4-ed27-45d9-b7ed-b0f8004b20ec
     title: "Functions with One Parameter"
     duration: "5:32"
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=b4c86986-1f66-497b-855f-b0f8004b212b
     title: "Functions with Many Parameters (<b>MINI-QUIZ 2</b> - USE LOAD BUTTON AT BOTTOM OF SCREEN)"
     duration: "6:31"
     quiz: 1
readings:
   - title: "Ch 4: Functions"
     author: "Charles Severance"
     url: https://www.py4e.com/html3/04-functions
     video_url: https://www.py4e.com/lessons/functions
     source: "Python for Everybody"
slides:
   - url: https://docs.google.com/presentation/d/1zdKgLQ6wBLEECW524thiUU0gmaB5Nh5svpA4oSFc5Zw/edit?usp=sharing
     title: Writing Functions
--- 

Today we'll start a discussion of defining our own functions with a special emphasis on writing _flexible_ functions. One of the main advantages to building a machine to automate something is that once we figure out how to do it once...we never need to worry about those exact steps again. But...imagine you build an oven that always heats to 350 degrees.

What if you want to bake something at 400  degrees?

Would you really make **a whole new oven** that only bakes at 400 degrees? Or could you add some knob / option to allow the oven to bake at _either_  350 or 400 degrees? Which one sounds more reasonable to you?

Our goal for today is to add those "knobs" (**parameters**) to our own functions in Python!
