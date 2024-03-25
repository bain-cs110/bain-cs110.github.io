---
layout: assignment-two-column
title: Project 2 - Yelp
due_date: 2024-03-13
abbreviation: P2Y
draft: 1
---

<table style="width:40%; border:0px;">
  <tr>
    <td><a class="nu-button" href="{{site.url}}/course-files/projects/project2/docs/apis/yelp.html" target="_blank">
    Yelp Docs <i class="fas fa-download"></i>
</a></td>
    <td><a class="nu-button" href="{{site.url}}/course-files/projects/project2/docs/apis/gui.html" target="_blank">
    GUI Docs <i class="fas fa-download"></i>
</a></td>
    <td><a class="nu-button" href="{{site.url}}/course-files/projects/project2/docs/apis/twilio.html" target="_blank">
    Twilio Docs <i class="fas fa-download"></i>
</a></td>
  </tr>
</table>

For this option, you are going to use the Yelp API to create a restaurant recommendation system. I have created a `yelp` module for you, located in the apis folder to help you. All of the `apis/yelp.py` functions <a href="{{site.url}}/course-files/projects/project2/docs/apis/yelp.html" target="_blank">have been documented here</a>. Here is a video of how your program might work:

<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=2cabf881-7873-4b78-a8d6-b125001d9a6b&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

Note: this is only one way of implementing this program, and includes some extra credit features. Feel free to do it **your way!**

Please implement the following (5) required features of your restaurant recommendation system (we encourage you to start with the `restaurant_finder.py` template):

### 1. Allow the user to select among the Yelp restaurant categories

You will give the user the option of selecting one or more restaurant categories that can be used to filter the restaurants. To do this you will do the following:

1. Present the user with some subset from the list of available categories (see `yelp.get_categories` for the complete list).
2. Ask the user to select one or more categories and store their selections and store them in the `user_selections` dictionary.
3. Proved the user with a way to either clear out or update their selected categories.

### 2. Allow the user to set the sorting criteria

How results are ordered really matters in search. Yelp allows 4 different options for sorting results: `best_match`, `rating`, `review_count`, `distance`. Given this, the user should be able to select how they want their results to be filtered.

### 3. Allow user to view restaurants that match the selection criteria at a given location

Given the user’s selected categories and sorting criteria:

1. Retrieve the restaurants, and allow the user to specify a location before executing the search.
2. Show the retrieved restaurants on the GUI in some coherent format.

### 4. Allow the user to preview an individual restaurant

Given the matched restaurants:

1. Allow the user to preview an individual restaurant
2. This should include (a) more detail about the restaurant, and (b) some reviews of the restaurant.
3. Use the `yelp.get_businesses` and `yelp.get_reviews` helper functions to help you.

### 5. Allow the user to email a restaurant recommendation

After the user has previewed a restaurant, ask them if they want to email the restaurant recommendation so someone. If so, email them a link to the restaurant and some details about it (including some reviews). Use the `twilio.send_email` function to help you.

Your email *needs to be readable.* You can either design a custom email or use the `to_html` option of the `yelp.generate_business_table` function.

### Extra Credit Options (Up to 6 Points)

#### [2 Points] Allow the user to add an additional search term

You will give the user the option to specify an additional search term for their query (e.g. `hamburgers`) to further narrow in on particular businesses.

#### [3 Points] Allow the user to set the price filters

You will give the user the option of selecting one or more price filters. The way the filters work: `1=$`, `2=$$`, `3=$$$`, and `4=$$$$`. So, if I only wanted to see $ and $$, my price filter would be: price_filter=1,2. Given this, the user should be able to select one or more price filters, and clear out their price filters if they want.

#### [2 Points] Allow the user to filter by restaurants that are “open now”

Enhance your program by also giving the user the option of specifying only restaurants which are currently open.

#### [3 Points] Allow the user to filter by restaurants that are “hot and new”

Enhance your program by also giving the user the option of specifying only restaurants which are “hot and new.” See the <a href="https://docs.developer.yelp.com/reference/v3_business_search" target="_blank">Yelp documentation (link updated)</a> for more info. (Look under the **attributes** argument)

#### [6 Points] Incorporate another information source

In addition to searching Yelp, try to integrate data from Spotify as well! Maybe generate a playlist that fits the theme of the restaurant!

### Rubric (40 Possible Points)

<table>
    <thead>
        <tr>
            <th>Feature</th>
            <th>Points</th>
            <th>Scoring Guidelines</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Main Program</td>
            <td>5 points</td>
            <td>
                <ul>
                    <li>App handles errors (incorrect inputs). (Note: this applies anywhere you ask the user for input)</li>
                    <li>App prompts the user for their input in various ways</li>
                    <li>App honors user requests</li>
                    <li>App does not exit unless user asks to quit</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Category selection</td>
            <td>8 points</td>
            <td>
                <ul>
                    <li>Displays the user's selected categories(s) if any in the GUI Textbox.</li>
                    <li>Displays the available Yelp categories from which to choose in the GUI Textbox or Popup Window.</li>
                    <li>Allows user to select among categories</li>
                    <li>Allows user to clear out selected categories and start over</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Ordering/Sorting Criteria</td>
            <td>4 points</td>
            <td>
                <ul>
                    <li>Allows user to specify their preferred ordering criteria (best_match, rating, review_count, distance).</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Previewing matching restaurants</td>
            <td>8 points</td>
            <td>
                <ul>
                    <li>Allows the user to specify a location</li>
                    <li>Results honor user’s selected location, categories, and sorting criteria</li>
                    <li>Shows the restaurants to the GUI textbox in some coherent format</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Previewing individual restaurant</td>
            <td>8 points</td>
            <td>
                <ul>
                    <li>Allows user to preview an individual restaurant</li>
                    <li>Includes detail about restaurant</li>
                    <li>Includes restaurant reviews</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Sends email</td>
            <td>3 points</td>
            <td>
                <ul>
                    <li>Successfully emails a restaurant recommendation and its reviews to a user in either a readable plain text format or in the provided HTML format.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Code Quality</td>
            <td>3 points</td>
            <td>
                <ul>
                    <li>All functions, variables, and file_names have mnemonic names / are snake case
                    (up to -2 points)</li>
                    <li>Code is organized and without unused or redundant code. Please remove commented out code that isn’t running (to help our graders)
                    (up to -3 points)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Video</td>
            <td>1 point</td>
            <td>
                <ul>
                    <li>Your video clearly demonstrates the features you implemented.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Extra credit</td>
            <td>Up to 6 points</td>
            <td>
                <ul>
                    <li>Students completed various EC options according to the specifications above.</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
