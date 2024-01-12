---
layout: module
title: "Abstraction"
type: lecture
description: "(Mini-Quiz 1)"
draft: 0
num: 4
due_date: 2024-01-12
mini_quiz_id: quizzes/225247
mini_quiz_num: 1
mini_quiz_title: Variables, Operators, and Using Functions
exercise_url: "lecture04.zip"
canvas_id: friday-lecture-4-abstraction
slides:
   - url: https://docs.google.com/presentation/d/1SyKAtH2TlrelKZKSxqO12z5GS5N1KNYhOiOvWNCXG70/edit?usp=sharing
     title: Writing our Own Functions
readings:
   - title: "Ch 4: Functions"
     author: "Charles Severance"
     url: https://www.py4e.com/html3/04-functions
     video_url: https://www.py4e.com/lessons/functions
     source: "Python for Everybody"
---

<img alt="what is a function" class="module-image" src="{{site.url}}/assets/images/lectures/lecture_05_functions.png" />
Now that we're starting to get used to functions...we need to start to understand how to design them ourselves. First we'll review some topics from Wednesday and then re-motivate why functions are useful - to encapsulate code. Then, we'll start to understand all of the details of defining our own functions, from names, to parameters, to awesome functionality.

Functions allow us to tackle the key CS concept of **abstraction**. Programming is like making an investment in your future – we do a bunch of work **now** in order to be **lazy** later. Why? Think of it this way. Programming is basically like considering all of the tasks you do each day, and making a cool machine (aka a _function_) in order to automate that task. But what happens when you have two very similar tasks. For instance, what if on Mondays you have an Ego Waffle...but on Tuesdays you have toast.

Toasting those things is a very similar process. Do you really need to build a SEPARATE machine to toast toast...vs toasting egos? Of course not! You can just make one machine that is able to do both of those actions. This is the concept of **abstraction** at play and is an incredibly powerful idea in computer science both when creating our own machines (functions) and teaching the computer new ways of representing the world around us (data types).