---
layout: module
title: |
    Review
type: lecture
draft: 0
num: 10
description:
  - More on Scope
  - Review for Q1
due_date: 2022-04-20
slides:
   - title: "Quiz 1 Review"
     url: https://docs.google.com/presentation/d/1GTg2jypc-u101Wn_BNgsBqB0NznNDOXO07uX_TD3SWM/edit?usp=sharing
videos:
  - title: "Live Lecture"
    url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e9ae198d-4473-4a6c-901d-ae670037b204
    live: 1
    duration: "50:00"
exercise_url: "lecture10.zip"
---

Today in class, we will review any questions that you have about the material covered thus far. Please review the [Quiz 1 study materials](week04-lecture03) and come with questions. We're also going to make sure we understand how to do these two problems:

## Exercise 1
```python
# Given the following two lists...
first_names = ['Kim', 'Brenda', 'Karlo']
last_names = ['Jones', 'Jauregui', 'Imper']

# Write a program that combines the two lists by creating a third list,
# where each entry is the full name of the person. You can assume that
# (1) first names and last names of the same person are located in the same slot of
# their respective lists (e.g. Kim Jones, Brenda Jauregui, Karlo Imper), and
# (2) that the lists always have three values in them.
```

## Exercise 2
Write a function that shifts a list of three coordinate pairs by some horizontal amount and some vertical amount. The function should return the new/updated list.

```python

# here is how I would call your function...
print(shift_coordinates([(20, 20), (30, 30), (40, 40)], x_units=100, y_units=200))
print(shift_coordinates([(40, 40), (100, 100), (200, 200)], x_units=50, y_units=100))
print(shift_coordinates([(40, 40), (100, 100), (200, 200)]))

# ...and here's what would print to the screen...
# [(120, 20), (130, 230), (140, 240)]
# [(90, 140), (150, 200), (250, 300)]
# [(40, 40), (100, 100), (200, 200)]
```
