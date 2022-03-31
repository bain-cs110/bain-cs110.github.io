---
layout: assignment-two-column
title: Working With Files
description:
    - Reading & writing files
    - File analytices
type: tutorial
abbreviation: Tutorial 7
draft: 0
num: 7
points: 3
due_date: 2022-02-23
---

<style>
    .bash-small .highlighter-rouge {
        width: 520px;
        margin: auto;
        margin-top: 10px;
    }
</style>

<a class="nu-button" href="/course-files/tutorials/tutorial07_template.zip" target="_blank">
    Tutorial Starter Files <i class="fas fa-download"></i>
</a>


In today's tutorial, you're going to calculate some statistics for the Boston Marathon. To do this, you will open some of the files in the `boston_marathon` directory, loop through each line in the file, and perform some basic summary statistics.

Please write a program to calculate the following statistics. You can write each program as a separate file, or do all of the calculations in a single file. Up to you.

## Please answer the following questions

1. How many people completed the Boston Marathon in 2015?

2. What was the average **age** of someone completing the Boston Marathon in 2015?
    * Hint: you may need to use try/except for any messy / unexpected data.
    * For an example of try/catch, see the <a href="https://docs.google.com/presentation/d/1hwSaQzYe0EDRnbQgoGUW2tcHhwZXw-gidLDplvPIXwE/edit#slide=id.g11481ce3057_0_166">end of the lecture slides</a>


3. What was the average **time** of people who completed the Boston Marathon in 2015?
    * Hint: you will have to parse the total time into a number that can be summed. So, you may want to convert all of the times to seconds.

4. What was the average **time** for **Kenyan** runners who completed the Boston Marathon in 2015?

5. ***[If Time]*** What was the average time for female runners in their 30s in 2015?
