---
layout: assignment-two-column
title: Project 2 - Spotify
due_date: 2024-03-13
abbreviation: P2S
draft: 1
---

<table style="width:40%; border:0px;">
  <tr>
    <td><a class="nu-button" href="{{site.url}}/course-files/projects/project2/docs/apis/spotify.html" target="_blank">
    Spotify Docs <i class="fas fa-download"></i>
</a></td>
    <td><a class="nu-button" href="{{site.url}}/course-files/projects/project2/docs/apis/gui.html" target="_blank">
    GUI Docs <i class="fas fa-download"></i>
</a></td>
    <td><a class="nu-button" href="{{site.url}}/course-files/projects/project2/docs/apis/twilio.html" target="_blank">
    Twilio Docs <i class="fas fa-download"></i>
</a></td>
  </tr>
</table>

For option 2, you are going to use the Spotify API to create a music recommendation system. I have created a spotify module for you, located in the apis folder to help you. All of the `apis/spotify.py` functions <a href="{{site.url}}/course-files/projects/project2/docs/apis/spotify.html" target="_blank">have been documented here</a>. Here is a demo video of how your program should work:

<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=81a5f135-ea0b-47e9-bc6b-b125001d9a48&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=true&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

Note: this is only one way of implementing this program, and includes some extra credit features. Feel free to do it ***your way!***

Please implement the following (3) required features of your restaurant recommendation system (we encourage you to start with the `music_finder.py` template):

### 1. Allow the user to select one or more genres of music

You will give the user the option of selecting one or more genres that can be used to “seed” the Spotify song recommendations system. To do this you will do the following:

1. Present the user with a list of available genres using the `spotify.get_genres` function — feel free to modify it.
2. Ask the user to select one or more genres and store their genre selections in a list variable called “genres”
3. The user should be able to clear out this selection.

### 2. Allow the user to select one or more artists

You will also give the user the option of selecting one or more artists that can also be used to “seed” the Spotify song recommendations system. To do this you will do the following:

1. Provide a way for the user to search for and display artists (use the `spotify.get_artists` function)
2. Provide a way for the user to select the artists they’re interested in and store the corresponding artist objects in a list variable called “artists”
3. Allow the user to either clear out or append artists to their artists list.

### 3. Generate and email song recommendations

Given the user’s selected genres and artists:

1. Retrieve the recommended tracks using the `spotify.get_similar_tracks` function.
2. Print the retrieved tracks to the GUI in some coherent format.
3. Ask the user if they want to email the tracks to someone, and if so, send an email (use the `twilio.send_email` function to help you) of the list of track recommendations. Use the `spotify.generate_tracks_table` function to help you build a nice tracklist (see the video) that can be emailed.

> **NOTE:** The `spotify.get_similar_tracks` function’s job is to get recommendations based on seed data. It has very specific requirements about what inputs it needs to work. Make sure to look at the spotify api documentation linked near the starter files.

Your email *needs to be readable.* You can either design a custom email or use the `to_HTML` option of the `generate_tracks_table` function.

### Extra Credit Options (Up to 6 Points)

#### [3 Points] Allow the user to select one or more tracks

If you have time and need extra credit, you may enhance your program by also giving the user the option of selecting one or more tracks to “seed” the Spotify song recommendations system. To do this, you will do the following:

1. Provide a way for the user to search for and display tracks
1. Provide a way for the user to select the tracks they’re interested in and store the corresponding track objects in a list variable called “tracks”
1. Allow the user to either clear out or append tracks to their tracks list.

#### [2 Points] Extra Credit: Search for similar artists

Allow the user to discover artists who are similar to a given artist.

#### [2 Points] Extra Credit: Search for playlists by keyword

Allow the user to find playlists based on a keyword search and show their contents or a link to them.

#### [3 Points] Extra Credit: Generate an HTML file

Generate an HTML file with the table of recommended tracks as well as some information about the artists (and tracks) that went into seeding the playlist. Consider embedding images of artists, albums, and/or audio players into the file.

#### [3 Points] Extra Credit: Save a player to an HTML file

Generate some Player HTML (either for a track, artist, or playlist) and output it to a file (you don't have to know how HTML works to make this happen – the key will be identifying which functions in the api you can use and then remembering how to write to a file!).

#### [5 Points] Extra Credit: Allow the user to download a preview of a song

Allow the user to download an mp3 file of the song preview of at least one of their recommendations.

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
            <td>Main Program Loop</td>
            <td>5 points</td>
            <td><ul>
                <li>Loop handles errors (incorrect inputs) (Note: this applies anywhere you ask the user for input)</li>
                <li>Loop prompts the user for their input</li>
                <li>Loop honors user requests</li>
                <li>Loop does not exit unless user asks to quit</li></ul>
            </td>
        </tr>
        <tr>
            <td>Genre Selection</td>
            <td>8 points</td>
            <td>
                <ul>
                    <li>Displays the user's selected genre(s) if any</li>
                    <li>Displays available genres</li>
                    <li>Allows user to select among the genres that are presented (and no others)</li>
                    <li>Allows user to clear out their selected genres and start over</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Artist Selection</td>
            <td>12 points</td>
            <td>
                <ul>
                    <li>Allows user to search for artist</li>
                    <li>Allows user to select among artists returned from Spotify</li>
                    <li>Allows user to clear out selected artists and start over</li>
                    <li>Displays the names of the user's selected artists</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>Generate and email recommendations</td>
            <td>11 points</td>
            <td><ul>
                <li>Correctly passes arguments of correct type into the get_similar_tracks() function.</li>
                <li>Displays recommendations to GUI (including track name and artist name).</li>
                <li>Successfully emails the recommendation list.</li></ul>
            </td>
        </tr>
        <tr>
            <td>Code Quality</td>
            <td>3 points</td>
            <td><ul>
                <li>All functions, variables, and file_names have mnemonic names / are snake case
                (up to -2 points)</li>
                <li>Code is organized and without unused or redundant code. Please remove commented out code that isn’t running (to help our graders)
                (up to -3 points)</li></ul>
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
            <td><ul>
                <li>Students completed various EC options according to the specifications above.</li></ul>
            </td>
        </tr>
    </tbody>
</table>
