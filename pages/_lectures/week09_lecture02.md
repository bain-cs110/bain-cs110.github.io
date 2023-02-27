---
layout: module
title: "Error Handling and Using Files"
description:
type: lecture
draft: 0
num: 22
due_date: 2023-03-01
canvas_id: wednesday-lecture-22-pre-recorded-error-handling-and-using-files-mar-1
exercise_url: "lecture22.zip"
videos:
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=baa5ce36-8b72-4ecc-b05d-afb600310c08
     title: "Error Handling"
     duration: "11:49"
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=99fe415d-b85a-4c83-817e-afb6003106b2
     title: "File Intro"
     duration: "4:19"
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=af6053fc-2956-4525-9ddc-afb600310545
     title: "File Basics"
     duration: "6:59"
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9bc2fc3b-b616-4db3-b703-afb60031008d
     title: "Helpful String and List Methods"
     duration: "1:57"
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d825e2be-25cc-46b7-9f23-afb6003100c1
     title: "Line Count Challenge"
     duration: "2:24"
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=463b3f1e-49f4-4433-985f-afb6003100f5
     title: "Word Count Challenge"
     duration: "4:07"
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=fa9d7ee5-c535-4afd-bfbc-afb60031015b
     title: "Data Validation Example (Optional)"
     duration: "4:07"
slides:
   - url: https://docs.google.com/presentation/d/1XXaeUu-3-wYIsnovhBOQVC0H_lT4AbrypPK5gnffiww/edit?usp=sharing
     title: "Error Handling and Using Files"
---

In the pre-recorded lectures today we'll talk about two new programming ideas.

The first is the idea of `try/except`. It would be **enormously bogus** if every time our program ran into an error, it just crashes and stops. Up until now, that's been our only option...but what if we had a "backup plan" ready to go for our program. Is it possible to "gracefully" keep going rather than just crashing?

The second topic is the idea of **file reading and writing**. Last time, we talked about receiving data from the internet. What if we've already got the data in a file on our computer. How can we get that into Python? Or how can we create files from Python?