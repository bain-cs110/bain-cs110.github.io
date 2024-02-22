---
layout: module
title: "Introduction to Dictionaries"
type: lecture
draft: 0
num: 19
due_date: 2024-02-23
canvas_id: friday-lecture-21-dictionaries-may-19
exercise_url: "lecture19.zip"
slides:
   - url: https://docs.google.com/presentation/d/1tedUedb6soquvByENjp0X1x7C5HSBNDYhUUicxwx-9E/edit?usp=sharing
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
