---
layout: module
title: "Introduction to Dictionaries"
description:
type: lecture
draft: 0
num: 20
due_date: 2023-02-24
canvas_id: friday-lecture-20-dictionaries-feb-24
exercise_url: "lecture20.zip"
slides:
   - url: https://docs.google.com/presentation/d/13UPZ2pugkyi-dti7EiMCNmAp5P0XqyUfpWa5J0_lXiw/edit?usp=sharing
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