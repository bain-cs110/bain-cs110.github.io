from apis import spotify, twilio, gui
import customtkinter

def main_menu():
    gui.show_text("Select an action via a button!")

def quit_program():
    app.destroy()

def select_favorite_genres():
    print("Select favorite genres here...")
    # 1. Allow user to select one or more genres using the
    #    spotify.get_genres_abridged() function
    # 2. Allow user to store / modify / retrieve genres
    #    in order to get song recommendations

    # Once done, go back to the main_menu
    main_menu()
          
def select_favorite_artists():
    print("Select favorite artists here...")
    # 1. Allow user to search for an artist using
    #    spotify.get_artists() function
    # 2. Allow user to store / modify / retrieve artists
    #    in order to get song recommendations

    # Once done, go back to the main_menu
    main_menu()

def discover_new_music():
    print("Show recommendations here...")
    # 1. Allow user to retrieve song recommendations using the
    #    spotify.get_similar_tracks() function
    # 2. Show them to the user
    # 3. Ask if you want to email them!


### GLOBAL VARIABLES
    
user_selections = {
    'genres': [],
    'artists': {}
}

actions = {
    "Main Menu": main_menu,
    "Quit": quit_program,
    "Select Favorite Genres": select_favorite_genres,
    "Select Favorite Artists": select_favorite_artists,
    "Discover New Music": discover_new_music,
}

######### YOUR CODE ABOVE HERE #################################################
## DO NOT EDIT BELOW THIS LINE WITHOUT ASKING PROF. BAIN FIRST
app = customtkinter.CTk()
gui._setup_window(app, title="Spotify Explorer")
gui._setup_buttons(actions)
main_menu()
app.mainloop()
