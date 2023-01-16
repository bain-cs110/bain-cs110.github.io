---
layout: module
title: "Writing Flexible Functions"
type: lecture
draft: 0
num: 6
due_date: 2023-01-18
exercise_url: "lecture06.zip"
description:
canvas_id: wednesday-lecture-6-pre-recorded-writing-flexible-functions-january-18
videos:
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=8e74938b-c5d7-418e-9206-af8c004ef5f6
     title: "Intro & Review"
     duration: "4:44"
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=0fec152b-3669-44a5-9a9b-af8c004ef623
     title: "Function with One Parameter (Concept)"
     duration: "5:42"
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=690a0a51-0f8b-4aaa-8244-af8c004ef64f
     title: "Function with One Parameter (IDLE)"
     duration: "4:22"     
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=95cf6477-5cb9-4146-9dfd-af8c004fbe15
     title: "Function with Multiple Parameters (Concept)"
     duration: "3:41"   
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2202f16f-5ebd-4028-843f-af8c004ef66f
     title: "Function with Multiple Parameters (IDLE)"
     duration: "4:34" 
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a4377b54-a37f-4d29-a93d-af8c004f669b
     title: "Intro to TKinter"
     duration: "5:36" 
slides:
   - url: https://docs.google.com/presentation/d/1ILh03z-qiMdTfeL9Om_XTHKuBqlj-YtcR51yLRTyvv0/edit?usp=sharing 
     title: Writing Flexible Functions
---

Today we'll continue our discussion of defining our own functions with a special emphasis on writing _flexible_ functions. One of the main advantages to building a machine to automate something is that once we figure out how to do it once...we never need to worry about those exact steps again. But...imagine you build an oven that always heats to 350 degrees.

What if you want to bake something at 400  degrees? 

Would you really make **a whole new oven** that only bakes at 400 degrees? Or could you add some knob / option to allow the oven to bake at _either_  350 or 400 degrees? Which one sounds more reasonable to you?

Our goal for today is to add those "knobs" (**parameters**) to our own functions in Python!