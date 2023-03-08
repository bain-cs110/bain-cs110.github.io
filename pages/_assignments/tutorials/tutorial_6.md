---
layout: assignment-two-column
title: Getting Started on Project 2
type: tutorial
abbreviation: Tutorial 6
draft: 0
num: 6
points: 100
canvas_id: 1174719
due_date: 2023-03-08

---

In this week's tutorial, we'll be working on [Project 2](../assignments/p2). This includes:

1. Setting our computers up to work on P2.
2. Practicing using some of the modules that have been provided for you inside of the apis directory.

NOTE: While you may complete the Project submissions as a team, this tutorial should be completed solo (i.e. everyone needs to setup their computer so it's capable of working on the project).

Please complete the following steps:

* * *
## Getting Setup

Complete the "Setup" section of [Project 2](../assignments/p2).

When you're done, complete one of the two options (either / or) listed below:

* * *

## Option 1: Yelp Option
Create a brand new file called `tutorial06.py` directly inside of your `project02` folder (the location matters). Your directory structure should look like this:

```bash
├── apis
├── restaurant_finder.py
├── tests
└── tutorial06.py
```

Next, paste the following code into your `tutorial06.py` file and run it.

```python
from apis import yelp

businesses = yelp.get_businesses("Evanston, IL")
print(businesses)
```

You should see some Evanston restaurants print to the screen (as a list of dictionaries).
### Practice Outputting Dictionary Values
1. Output just the `name` of each business to the screen
2. Output the `name`, `rating`, and `review_count` to the screen

### Using Helper Functions
There is also a helper function inside of the <a href="/course-files/projects/project02/docs/apis/yelp.html" target="_blank">apis.yelp</a> module that can help you output businesses to the screen, which you are welcome to modify:

```python
table_text = yelp.get_formatted_business_list_table(businesses)
print(table_text)
```

### Practice Querying
When you're done outputting the data, open the `apis/yelp.py` and navigate down to the `get_businesses` function definition. Note all of the keyword  (optional) parameters that the function accepts.

Next, go back to your `tutorial06.py` file and modify the get_businesses(...) function call by:
1. Use the various keyword arguments (`price`, `category`, and/or `location`) to change which results get displayed.
2. Use the `sort_by` keyword argument to change the sort order.

{:.blockquote-no-margin}
> ### Learning more about the yelp module (apis/yelp.py)
> You can also learn more about the yelp module by:
> * Looking at the online documentation here: <a href="/course-files/projects/project02/docs/apis/yelp.html" target="_blank">/project02/docs/apis/yelp.html</a>

* * *

## Option 2: Spotify Option
Create a brand new file called `tutorial06.py` directly inside of your `project02` folder (the location matters). Your directory structure should look like this:

```bash
├── apis
├── music_finder.py
├── tests
└── tutorial06.py
```

Next, paste the following code into your `tutorial06.py` file and run it.

```python
from apis import spotify
artists = spotify.get_artists('Beyonce')
print(artists)
```

You should see some search results relating to Beyonce print to the screen (as a list of dictionaries).

## Practice Outputting Dictionary Values
1. Output just the `name` of each artist to
2. Output the `name`, `genres`, and `share_url` to the screen

### Practice Querying
When you're done outputting the data, open the `apis/spotify.py` file and navigate down to the `get_similar_tracks` function definition. Note all of the keyword (optional) parameters that the function accepts.

While each parameter is technically optional, this function needs some seed data in order to give you song recommendations. Up to 5 seed values may be provided in any combination of seed_artists, seed_tracks and seed_genres. In other words: <br>`len(artist_ids) + len(track_ids) + len(genres)` must be between 1 and 5.

Next, go back to your `tutorial06.py` file and try invoking the `spotify.get_similar_tracks` function as follows:

```python
track_recommendations = spotify.get_similar_tracks(artist_ids=['6vWDO969PvNqNYHIOW5v0m'])
print(track_recommendations)
```
* Try passing in different Artist IDs
* Try passing in a list of genres (see the `apis.spotify.get_genres_abridged` function to get some valid genre categories).

There is also a helper function inside of the `apis.spotify` module that can help you output the tracks to the screen:

```python
table_text = spotify.get_formatted_tracklist_table(track_recommendations)
print(table_text)
```

If you still have time, please experiment with some of the other built-in functions:
* get_tracks
* get_top_tracks_by_artist
* get_related_artists
* get_playlists

{:.blockquote-no-margin}
> #### Learning more about the spotify module (apis/spotify.py)
> Checkout the documentation here: <a href="/course-files/projects/project02/docs/apis/spotify.html" target="_blank">Spotify Library</a>

* * *

## Other General Reminders

Some other things that might be useful during project 2!

```python
# Printing all of the different things in a list one on each line:
counter = 0
my_list = ["a", "b", "c", "d"]
for item in my_list:
    print(counter, item)
    counter = counter + 1

# Printing all of the different key value pairs in a dictionary one by one:
my_dict = {"a": 1, "b":2, "c": 3}
for key in my_dict:
    print(key, my_dict[key])
```

```python
# Splitting a string of numbers separated by commas into a list of strings
test = "1,2,3,4,5"
my_list = test.split(",")
```

```python
# Making a list of numbers or things into a string separated by commas.
my_list = [1, 2, 3, 4, 5]
my_string = ",".join(my_list)
```

```python
# Converting strings to an integer
a_string = "1"
an_int = int(a_string)
```

```python
# Saving something someone entered into a dictionary
test = {"keyboard_entry": ""}
some_input = input("Please type in something.")
test['keyboard_entry'] = some_input
```

```python
# Short circuiting a function...
def example_function(a_number):
    if a_number == 2:
        return None
    print("I'll only print if the nubmer isn't 2")
    return "hello"
```

* * *
## Getting Credit for Your Work

If you're in class you don't need to submit a `.py` file on Canvas. Instead, find one other person in your group that is finished and peer review each other's work. Here are the things to check:

1. Does their code look readable and neat?
1. Can you understand what their code does by reading it?
1. How was their solution different from yours (if at all)?
1. Did they do anything cool?

Once you've each taken a look, take a second to debrief. Anything either of you found difficult? Easy? Fun? Mind-blowing? Once you've debriefed, **both of you should fill out this** <a href="https://docs.google.com/forms/d/e/1FAIpQLScFw18yE8C1L2te7MPFCvcbGCFkIdURc0aMonRGQ8-X0FJkwQ/viewform?usp=sf_link" target="_blank">attendance Google Form</a>. **NOTE: You will need the NetID of the person's whose code you reviewed.** You're free to go after you're finished, though we hope that you might consider sticking around and helping others in your group.

If you're submitting remotely, you MUST submit your completed tutorial to Canvas and it will be graded. Make sure that all of your functions are named correctly and that they use the EXACT parameter order, names, and types as specified.

Please turn in your completed `tutorial06.py` file on Canvas by Wednesday night at midnight. ONLY SUBMIT the file you worked in and no other files.