from apis import spotify, twilio, gui
import customtkinter

def main_menu():
    gui.show_text("Select an action via a button!", append=True)

def quit_program():
    app.destroy()

def select_categories():
    print('Handle category selection here')
    # 1. Allow user to select one or more categories using the
    #    yelp.get_categories() function
    # 2. Allow user to store / modify / retrieve categories
    #    in order to filter restaurants


    # Once done, go back to the main_menu
    main_menu()

def select_ordering():
    print('Handle ordering preference here...')
    # Allow the user to determine how they want to sort the search results
    # Available options include: best_match, rating, review_count, distance.
    
    
    # Once done, go back to the main_menu
    main_menu()

def discover_new_restaurants():
    print('Retrieve matching restaurants...')
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
