---
layout: module
title: "Error Handling and Using Files"
description: "(Mini-Quiz 12)"
type: lecture
draft: 0
num: 21
due_date: 2024-02-28
canvas_id: 1371705
exercise_url: "lecture21.zip"
lec_assignment: 1
canvas_assignment_group: "Mini-Quiz"
canvas_points_possible: 10
canvas_allowed_extensions: "py"
canvas_submission_types: "external_tool"
canvas_id: 
canvas_title: Lecture 21 (Pre-Recorded) - Error Handling and Using Files - Mini-Quiz 12
videos:
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=bc00df70-c934-4f67-849a-b1220011d86b
     title: "Error Handling"
     duration: "8:00"
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d0be9d1e-7c11-4648-b65c-b1220011d6e7
     title: "File Intro"
     duration: "3:50"
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d68fe717-c7b3-4223-8983-b1220011cfa4
     title: "Files Syntax + Helpful Methods"
     duration: "4:33"
   - url: ""
     title: "Reading from Files (<b>Use LOAD button to access MQ</b>)"
     duration: "11:57"
     quiz: 1
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=3b5d58e1-14f5-4315-99bb-b1220011cfca
     title: "Writing Files Challenges"
     duration: "3:19"
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=4312f46f-dfd2-46fe-a75c-b1220011cff5
     title: "(Bonus) Data Validation Example"
     duration: "14:20"
slides:
   - url: https://docs.google.com/presentation/d/16n_VDeh13SPEPL26XKP4MMvMciuH0P2LSjukke19is4/edit?usp=sharing
     title: "Error Handling and Using Files"
---

In the pre-recorded lectures today we'll talk about two new programming ideas.

The first is the idea of `try/except`. It would be **enormously bogus** if every time our program ran into an error, it just crashes and stops. Up until now, that's been our only option...but what if we had a "backup plan" ready to go for our program. Is it possible to "gracefully" keep going rather than just crashing?

The second topic is the idea of **file reading and writing**. Last time, we talked about receiving data from the internet. What if we've already got the data in a file on our computer. How can we get that into Python? Or how can we create files from Python?