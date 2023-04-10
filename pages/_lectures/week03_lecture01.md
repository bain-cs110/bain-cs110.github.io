---
layout: module
title: Writing Flexible Functions
type: lecture
draft: 0
num: 6
due_date: 2023-04-10
exercise_url: "lecture06.zip"
description:
canvas_id: monday-lecture-6-writing-flexible-functions
slides:
  - url: https://docs.google.com/presentation/d/16ldSczIOl1A7A8PrwzXncsyaRTiWVADr17cefzbWTWw/edit?usp=sharing
    title: Writing Flexible Functions
readings:
   - title: "Ch 4: Functions"
     author: "Charles Severance"
     url: https://www.py4e.com/html3/04-functions
     video_url: https://www.py4e.com/lessons/functions
     source: "Python for Everybody"
---

Today we'll start a discussion of defining our own functions with a special emphasis on writing _flexible_ functions. One of the main advantages to building a machine to automate something is that once we figure out how to do it once...we never need to worry about those exact steps again. But...imagine you build an oven that always heats to 350 degrees.

What if you want to bake something at 400  degrees?

Would you really make **a whole new oven** that only bakes at 400 degrees? Or could you add some knob / option to allow the oven to bake at _either_  350 or 400 degrees? Which one sounds more reasonable to you?

Our goal for today is to add those "knobs" (**parameters**) to our own functions in Python!
