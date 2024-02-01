---
layout: assignment-two-column
title: Reading Someone Else's Program
canvas_title: Homework 4
abbreviation: HW4
type: homework
due_date: 2024-02-02
points: 100
draft: 0
canvas_id: 1360954
canvas_assignment_group: "Homework"
canvas_points_possible: 100
canvas_submission_types: "online_upload"
canvas_allowed_extensions: "py"
---

On the first day of class, I mentioned that computer science was a _social_ discipline. Programs are simply too complex these days to be only written by one person. Which means, programs need to be able to be _read_ by other programmers. In this class, we find that students often "stop" refining their programs as soon as they meet the minimum requirements of the assignment. While in a class, that might an okay approach, in the real world, this doesn't work in any environment where someone else needs to be able to use/read/evaluate your programs.

To that effect, this assignment will ask you to serve as a Peer Reviewer for another student's HW 3 submission.

* * *

## Ground Rules

1. Be kind.
2. Explain your reasoning.
3. Balance giving explicit directions with just pointing out problems and letting the programmer decide.
4. Encourage the author to simplify code or add code comments to explain their approach instead of just saying "you should do this instead...".

* * *

## How To Access

The peer review will be completed via Canvas. Here are the instructions on [how to access your assigned peer review](https://community.canvaslms.com/t5/Student-Guide/How-do-I-submit-a-peer-review-to-an-assignment/ta-p/293).

<details>
  <summary>What should the rubric look like?</summary>
  Like this!
  <img alt="screenshot of rubric" src= {{site.url}}/assets/images/hw04/hw4_rubric.png>
  <b>Note that the categories are "out of order" so make sure to select the one you mean!</b>
</details>
<br>

You should download the other person's program and copy it into your Homework 3 folder (so that you can use the `hw3_shapes` module) in order to complete your review.

<details>
  <summary>Having trouble downloading your peer's submission?</summary>
  A number of people reported not seeing a download button in the peer review (especially on Macs). To download your Peer's Submission, visit <b>your HW 4</b> assignment and view the feedback. Everyone should have a comment from Prof. Bain with an attached file that is the submission of your peer. If that's not the case, email Prof. Bain.
</details>
<br>

<mark>Once you click submit you will not be able to edit your Peer Review so make sure to read all the instructions below FIRST and double check you've completed the review before hitting submit!</mark>

Once your peer has reviewed your assignment, you can view their comments by [following the instructions here](https://community.canvaslms.com/t5/Student-Guide/Where-can-I-find-my-peers-feedback-for-peer-reviewed-assignments/ta-p/320).

<mark>Do not share your comments or your peer's submission with ANYONE other than with the original submitter via Canvas</mark>. Violating this policy is a serious NU Student Code of Conduct violation and will be reported to your Dean of Students. 

* * *

## What To Look For

Canvas has a _rubric_ built-in for the assignment for you to use to evaluate the person's program. While you should certainly look at the other student's flower function, _please focus most of your attention on the other submitter's `creature` function_. For each rubric item you should assign a **category** <mark>and</mark> add a **2+ sentence comment** justifying your rubric selection.

* Design
  * Does this program fit the idea of the assignment?
  * Compared to your program, how different is the approach?
  * Is it impressive? Exciting? Innovative?
  * Is there excess code that is commented out, unused, or otherwise in the way?
* Style
  * Are variables named with meaningful and reasonable descriptors (i.e. mnemonic but not overly verbose)?
  * snake_case for variables?
  * Does the program use consistent indentations, spacing, etc.?
  * Are there excessive parentheses?
* Functionality
  * Does it do what the the programmer says it does?
  * Does it do what the assignment asks for?
  * Could it effect anything other than this one program? (side-effects)
* Complexity
  * How long did it take for you to understand the program?
  * Are individual lines too complex?
  * For more complex steps, are there comments describing what the intent?
  * Are there simpler ways to express the idea (i.e. is it over-engineered)?

There's a fifth rubric item that asks whether or not you learned anything from reviewing this student's assignment that you might want to change / use in your own `creature` function if you were asked to revise it.

<details>
  <summary>How do I add a comment?</summary>
  For each rubric category, there's a small "comment bubble." Click on the bubble and it will allow you to add your comment!
  <img alt="screenshot of rubric comment button" src= {{site.url}}/assets/images/hw04/hw4_rubric_bubble.png>
</details>
<br>
* * *

## How will you be graded?

This is a participation-based activity meaning someone's review doesn't affect your grade on the assignment. You will receive credit based off of whether or not you completed your review of a peer's program. <mark>You will lose points if you do not do any of the following</mark>:

* If your comments/rubric selections are random or unthoughtful (as determined by course staff), you will receive a 0. They must be written by you without the aid of any other tools.
* Any comments that violate the Northwestern Student Code of Conduct will be referred to the Dean of Student's office.
* If you do not leave a comment on each of the 4 rubric items, you will receive a 10 point penalty. These comments don't need to be extensive, but they should be meaningful. You can reference particular line numbers of a person's program if you want to refer to something specific.
* Just like a normal homework, these peer reviews should be completed by Friday at 11:59pm CST. If your review is completed after that, you will receive the normal Late Penalty. Peer reviews completed after Sunday at 11:59pm CST will receive a 0.

{% include submission_details.md %}
