from apis import audio, twilio, gui
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
    #    audio.get_genres() function
    # 2. Allow user to store / clear / modify / retrieve genres
    #    from user_selections to be used in the mixtape

def select_artists():
    gui.clear()
    gui.print("Select favorite artists here...")
    # 1. Allow user to search for an artist using
    #    audio.search_for_artists() function
    # 2. Allow user to store / clear / modify / retrieve artists
    #    from user_selections to be used in the mixtape
          

def make_mixtape():
    gui.clear()
    gui.print("Show recommendations here...")
    # 1. Allow user to retrieve song recommendations using the
    #    audio.generate_mixtape() function
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
    "Select Genres": select_genres,
    "Select Artists": select_artists,
    "Make Mixtape!": make_mixtape,
}

######### YOUR CODE ABOVE HERE #################################################
## DO NOT EDIT BELOW THIS LINE WITHOUT ASKING PROF. BAIN FIRST
app = customtkinter.CTk()
gui._setup_window(app, title="Mixtape Maker")
gui._setup_buttons(actions)
main_menu()
app.mainloop()
