---
layout: module
title: "Introduction to Dictionaries"
type: lecture
draft: 1
num: 21
due_date: 2024-05-17
canvas_title: "Friday - Lecture 212 - Dictionaries"
canvas_id: friday-lecture-21-dictionaries
exercise_url: "lecture21.zip"
#videos:
#   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=28e38a28-7ccd-4308-b1db-b0cf014c7374
#     title: "Live Lecture Recording"
#     duration: "50:00"
#     live: 1
slides:
   - url: https://docs.google.com/presentation/d/18PXQUL1pc0a6ba4hbiA6EWiV19KbkBctN-3l449Vyl4/edit?usp=sharing
     title: Intro to Dictionaries
---

Today we'll introduce a new **compound** data type called the dictionary.

Don't get me wrong; lists are great. They allow us to take lots of simple data types and squish them all into the same variable. But what's with this whole accessing data by a number thing? Do you as a human lookup stuff in your brain via number?

_Internal Monologue_

What's my favorite color?

Oh I store that at index 137875.

It's `"green"`

_End Internal Monologue_

Probably not. More likely you store it with a phrase, like "favorite_color" (in CS we call this a **key**) and get back your favorite color `"green"` (which we call a **value**). Dictionaries are Python's way of emulating this sort of storage and that's what we'll be talking about today!



