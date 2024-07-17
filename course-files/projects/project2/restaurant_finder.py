from apis import yelp, twilio, gui
import customtkinter

def main_menu():
    gui.clear()
    gui.print("Select an action via a button!")

def quit_program():
    # Don't modify this one unless you want to
    # change the behavior when quitting.
    app.destroy() 

def select_categories():
    gui.clear()
    gui.print('Handle category selection here...')
    # 1. Allow user to select one or more categories using the
    #    yelp.get_categories() function
    # 2. Allow user to store / modify / retrieve categories
    #    in order to filter restaurants


def select_ordering():
    gui.clear()
    gui.print('Handle ordering preference here...')
    # Allow the user to determine how they want to sort the search results
    # Available options include: best_match, rating, review_count, distance.

def discover_new_restaurants():
    gui.clear()
    gui.print('Retrieve matching restaurants...')
    # 1. Allow user to retrieve restaurant recommendations using the
    #    yelp.get_businesses() function
    # 2. Show them to the user
    # 3. Ask if they want to email the results to anyone
    

### GLOBAL VARIABLES
user_selections = {
    'categories': [],
    'sort_order': '',
    'businesses': {}
}

actions = {
    "Main Menu": main_menu,
    "Quit": quit_program,
    "Select Categories": select_categories,
    "Select Ordering": select_ordering,
    "Discover New Restaurants": discover_new_restaurants,
}

######### YOUR CODE ABOVE HERE #################################################
## DO NOT EDIT BELOW THIS LINE WITHOUT ASKING PROF. BAIN FIRST
app = customtkinter.CTk()
gui._setup_window(app, title="Yelp Explorer")
gui._setup_buttons(actions)
main_menu()
app.mainloop()
