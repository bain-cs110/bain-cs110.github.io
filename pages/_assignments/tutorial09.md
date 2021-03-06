---
layout: assignment-two-column
title: Getting Started on Project 2
type: tutorial
abbreviation: Tutorial 9
draft: 0
num: 9
points: 3
due_date: 2022-06-01

---

{:.blockquote-no-margin}
> #### Video Walk Through (Optional)
> Depending on your comfort level, these videos may go by too quickly or too slowly for you. Feel
> free to pause and speed-up as you see fit. The first video goes through step 1 - Setup. The 2nd
> and 3rd videos cover the Yelp and Spotify sections respectively. While there's no need to watch/work
> through both, this would be a great chance to get extra practice working with dictionary data.

<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=d32c7312-9141-4b4b-b7cf-aea50072962b&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=cdca875c-0e6c-4b57-8e6b-aea5007295f1&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=089795c9-6252-42b1-baef-aea5007295c0&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

> While the videos walk through the basics of using each library, we HIGHLY encourage you to spend
> some time using the various function each API provides as this will greatly reduce the amount of
> time you have to spend doing this same thing when you sit down to actually complete the project.



## Background
In this week's tutorial, you will be getting a preview of [Project 2](../assignments/p2). This includes:

1. Installing some python dependencies using PIP.
2. Downloading <a href="https://canvas.northwestern.edu/files/13557351/download?download_frd=1">my_token.py</a> from Canvas and save it in your `apis` folder. This is the course API master token. Your project won't work without it.
3. Practicing using some of the modules that have been provided for you inside of the apis directory.

NOTE: While you may complete the HW and Project submissions as a team, this tutorial must be submitted solo (i.e. everyone needs to setup their computer so it's capable of working on the project).

Please complete the following steps:

## Step 1: Setup

Complete Steps A, B, C, and D in the "Setup" section of [Project 2](../assignments/p2#setup-please-read-carefully).

If you have set everything up correctly, running the `tests/run_verification.py` python file will display the following output AND you will get an email at the address you enter:

```bash
test_token (tests.test_authentication.TestAuthentication) ... ok
test_get_key (tests.test_authentication.TestAuthentication) ... ok
test__issue_get_request_only_one (tests.test_spotify.TestSpotify) ...
Loading: https://api.spotify.com/v1/search?q=beyonce&type=track
ok
test_execute_business_queries_just_one_simplified (tests.test_yelp.TestYelp) ... https://api.yelp.com/v3/businesses/search?location=Tallahassee, FL&limit=10
ok
test_can_import_sendgrid (tests.test_sendgrid.TestSendgrid) ... ok
test_can_import_sendgrid_api_module (tests.test_sendgrid.TestSendgrid) ... ok
test_can_send_email (tests.test_sendgrid.TestSendgrid) ... Please enter your email address:
your_email@email.com
Email sent. You may need to check your spam folder.
ok

----------------------------------------------------------------------
Ran 7 tests in 9.106s

OK
```

## Step 2
When you're done, complete one of the two options (either / or) listed below:

### Option 1: Yelp Option
Create a brand new file called `tutorial09.py` directly inside of your `project02` folder (the location matters). Your directory structure should look like this:

```bash
????????? apis
????????? music_finder.py
????????? restaurant_finder.py
????????? tests
????????? tutorial09.py
```

Next, paste the following code into your `tutorial09.py` file and run it.

```python
from apis import yelp

businesses = yelp.get_businesses()
print(businesses)
```

You should see some Evanston restaurants print to the screen (as a list of dictionaries).

#### Practice Outputting Dictionary Values
1. Output just the `name` of each business to the screen
2. Output the `name`, `rating`, and `review_count` to the screen

**TIP:** You can use the string's build-in `format` function to create nice columns:

```python
template = '{name:<30}{rating:>10}{review_count:>20}'

print('-' * 60)
print(template.format(name='NAME', rating='RATING', review_count='REVIEW COUNT'))
print('-' * 60)
print(template.format(name='Giordannos Pizza', rating=3.5, review_count=280))
print(template.format(name='Lou Malnati\'s Pizza', rating=3.7, review_count=190))
print('-' * 60)
```
The greater than / less than signs refer to whether the output is left or right justified, and the number refers to the column width.

There is also a helper function inside of the <a href="/course-files/projects/project02/docs/apis/yelp.html" target="_blank">apis.yelp</a> module that can help you output businesses to the screen, which you are welcome to modify:

```python
table_text = yelp.get_formatted_business_list_table(businesses)
print(table_text)
```

#### Practice Querying
When you're done outputting the data, open the `apis/yelp.py` and navigate down to the `get_businesses` function definition. Note all of the keyword  (optional) parameters that the function accepts.

Next, go back to your `tutorial09.py` file and modify the get_businesses(...) function call by:
1. Use the various keyword arguments (`price`, `category`, and/or `location`) to change which results get displayed.
2. Use the `sort_by` keyword argument to change the sort order.

{:.blockquote-no-margin}
> #### Learning more about the yelp module (apis/yelp.py)
> You can also learn more about the yelp module by:
> * Looking at the online documentation here: <a href="/course-files/projects/project02/docs/apis/yelp.html" target="_blank">/project02/docs/apis/yelp.html</a>
> * Running this command using python: **`help(apis.yelp)`**

### Option 2: Spotify Option
Create a brand new file called `tutorial09.py` directly inside of your `project02` folder (the location matters). Your directory structure should look like this:

```bash
????????? apis
????????? music_finder.py
????????? restaurant_finder.py
????????? tests
????????? tutorial09.py
```

Next, paste the following code into your `tutorial09.py` file and run it.

```python
from apis import spotify
artists = spotify.get_artists('Beyonce')
print(artists)
```

You should see some search results relating to Beyonce print to the screen (as a list of dictionaries).

#### Practice Outputting Dictionary Values
1. Output just the `name` of each artist to
2. Output the `name`, `genres`, and `share_url` to the screen

**TIP:** You can use the string's build-in `format` function to create nice columns:

```python
template = '{name:<30}{id:<25}{genres:<35}'

print('-' * 90)
print(template.format(name='NAME', id='ID', genres='GENRES'))
print('-' * 90)
print(template.format(name='Beyonc??', id='6vWDO969PvNqNYHIOW5v0m', genres='dance pop, pop, r&b'))
print(template.format(name='Beyonce as Shine', id='3mjguRNN96bC8zvaTwHoqE', genres=''))
print('-' * 90)
```

The greater than / less than signs refer to whether the output is left or right justified, and the number refers to the column width. The code above outputs like this:

```bash
------------------------------------------------------------------------------------------
NAME                          ID                       GENRES                             
------------------------------------------------------------------------------------------
Beyonc??                       6vWDO969PvNqNYHIOW5v0m   dance pop, pop, r&b                
Beyonce as Shine              3mjguRNN96bC8zvaTwHoqE                                      
------------------------------------------------------------------------------------------
```


#### Practice Querying
When you're done outputting the data, open the `apis/spotify.py` file and navigate down to the `get_similar_tracks` function definition. Note all of the keyword  (optional) parameters that the function accepts.

While each parameter is technically optional, this function needs some seed data in order to give you song recommendations. Up to 5 seed values may be provided in any combination of seed_artists, seed_tracks and seed_genres. In other words: <br>`len(artist_ids) + len(track_ids) + len(genres)` must be between 1 and 5.

Next, go back to your `tutorial09.py` file and try invoking the `spotify.get_similar_tracks` function as follows:

```python
track_recommendations = spotify.get_similar_tracks(artist_ids=['6vWDO969PvNqNYHIOW5v0m'])
print(track_recommendations)
```
* Try passing in different Artist IDs
* Try passing in a list of genres (see the `apis.spotify.get_genres_abridged` function to get some valid genre categories).

There is also a helper function inside of the `apis.spotify` module that can help you output the tracks to the screen, which you are welcome to modify:

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
> You can also learn more about the yelp module by:
> * Looking at the online documentation here: <a href="/course-files/projects/project02/docs/apis/spotify.html" target="_blank">/project02/docs/apis/spotify.html</a>
> * Running this command using python: **`help(apis.spotify)`**


## What to Turn In
Please turn in your completed tutorial exercise(s) on Canvas. To do this:

1. Zip your entire `project02` folder (with your edited files inside)
2. Rename your zip file to `tutorial09`
3. Upload your zip file to Canvas.
