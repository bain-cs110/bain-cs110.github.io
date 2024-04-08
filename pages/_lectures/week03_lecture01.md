---
layout: module
title: Abstraction
type: lecture
draft: 0
num: 6
due_date: 2024-04-08
canvas_id: lecture-6-writing-functions
canvas_title: Lecture 6 - Writing Functions
#videos:
#   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=b17b6042-bfd7-4866-9b78-b0f8004b2094
#     title: "Introduction"
#     duration: ""
readings:
   - title: "Ch 4: Functions"
     author: "Charles Severance"
     url: https://www.py4e.com/html3/04-functions
     video_url: https://www.py4e.com/lessons/functions
     source: "Python for Everybody"
exercise_url: "lecture06.zip"
slides:
   - url: https://docs.google.com/presentation/d/1gNg9aZJ4KNEbwslc4tOOvzAIjsox6pXiMKIuZ2nHlvg/edit?usp=sharing
     title: Writing Functions

---

Today we'll start a discussion of defining our own functions with a special emphasis on writing _flexible_ functions. One of the main advantages to building a machine to automate something is that once we figure out how to do it once...we never need to worry about those exact steps again. But...imagine you build an oven that always heats to 350 degrees.

What if you want to bake something at 400  degrees?

Would you really make **a whole new oven** that only bakes at 400 degrees? Or could you add some knob / option to allow the oven to bake at _either_  350 or 400 degrees? Which one sounds more reasonable to you?

Our goal for today is to add those "knobs" (**parameters**) to our own functions in Python!
