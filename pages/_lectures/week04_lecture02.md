---
layout: module
title: |
    Review: Week 3
type: lecture
draft: 0
num: 9
description:
  - Defining Functions
  - Variables & Variable Scope
  - Modules
due_date: 2022-01-26
slides:
   - title: "Quiz 1 Review"
     url: https://docs.google.com/presentation/d/13M-Y1ZJpR_XlQZRC6Lu_gmOq_3vpqWpbyl5-ghlV-Ek/edit?usp=sharing
videos:
  - title: "Live Lecture"
    url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=ace9dca1-7723-4593-a547-adf6016a94a6
    live: 1
    duration: "50:00"
exercise_url: "lecture09.zip"

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

### Answer (Another Approach)

```python
full_names = []
full_names.append(first_names[0] + ' ' + last_names[0])
full_names.append(first_names[1] + ' ' + last_names[1])
full_names.append(first_names[2] + ' ' + last_names[2])
print(full_names)
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

### Answer (One Approach)
```python
def shift_coordinates(my_list, x_units=0, y_units=0):
    return [
        (my_list[0][0] + x_units, my_list[0][1] + y_units),
        (my_list[1][0] + x_units, my_list[1][1] + y_units),
        (my_list[2][0] + x_units, my_list[2][1] + y_units)
    ]
```
