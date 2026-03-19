from apis import movies, twilio, gui
import customtkinter

##### EXTRA CREDIT OPTIONS
## Explain which you chose here...
#####

def main_menu():
    gui.clear()
    gui.print("Select an action via a button!")
    gui.print("Add more here if you want something")
    gui.print("to be displayed when going back to the main menu")

def quit_program():
    app.destroy()

def select_genres():
    gui.clear()
    gui.print("Select favorite genres here...")
    # 1. Allow user to select one or more genres using the
    #    movies.get_genres() function
    # 2. Allow user to store / clear / modify / retrieve genres
    #    from user_selections to be used in the watchlist

def select_upcoming_movies():
    gui.clear()
    gui.print("Select favorite upcoming movies here...")
    # 1. Allow user to search for an upcoming movie using
    #    movies.get_upcoming_movies() function
    # 2. Allow user to store / clear / modify / retrieve movies
    #    from user_selections to be used in the watchlist
          

def make_watchlist():
    gui.clear()
    gui.print("Show watchlist here...")
    # 1. Allow user to generate a watchlist using the
    #    movies.generate_watchlist() function
    # 2. Show them to the user
    # 3. Ask if you want to email them!


### GLOBAL VARIABLES
user_selections = {
    'genres': [],
    'movies': {}
}

actions = {
    "Main Menu": main_menu,
    "Quit": quit_program,
    "Select Genres": select_genres,
    "Select Upcoming Movies": select_upcoming_movies,
    "Make Watchlist!": make_watchlist,
}

######### YOUR CODE ABOVE HERE #################################################
## DO NOT EDIT BELOW THIS LINE WITHOUT ASKING PROF. BAIN FIRST
app = customtkinter.CTk()
gui._setup_window(app, title="Watchlist Maker")
gui._setup_buttons(actions)
main_menu()
app.mainloop()
