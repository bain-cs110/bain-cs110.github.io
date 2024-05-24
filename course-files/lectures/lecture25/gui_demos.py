from apis import gui
import customtkinter
from random import randint

## A short example on how to use the GUI library!
def main_menu():
    gui.clear()
    gui.print("I'm thinking of a number between 1 and 100...")
    gui.print("Your current guess is:", brain['current_guess'])

def quit_program():
    app.destroy()

def reset():
    brain["secret_number"] = randint(0, 100)
    brain['current_guess'] = None
    main_menu()

def enter_a_guess():
    user_input = gui.input("Please enter a guess (number between 0 and 100)!")

    try: 
        brain['current_guess'] = int(user_input)
    except:
        gui.popup("Uh oh..." + user_input + "isn't an integer! Try again.", kind="error")

    main_menu()

def check_the_guess():
    if brain["current_guess"] == brain["secret_number"]:
        gui.popup("You've won!!!!!")
    else:
        gui.popup("Not even close.", kind = "warning")
    main_menu()

def cheat():
    lower_num = brain['secret_number'] - randint(0, 5)
    higher_num = brain['secret_number'] + randint(0, 5)
    gui.print("The number I'm thinking of is between", lower_num, "and", higher_num, ".")

brain = {
    "secret_number": randint(0, 100),
    "current_guess": None
}

actions = {
    "Main Menu": main_menu,
    "Quit": quit_program,
    "Enter a Guess!": enter_a_guess,
    "Check my Guess!": check_the_guess,
    "..cheat...": cheat,
    "Reset the Game": reset
}

######### YOUR CODE ABOVE HERE #################################################
## DO NOT EDIT BELOW THIS LINE WITHOUT ASKING PROF. BAIN FIRST
app = customtkinter.CTk()
gui._setup_window(app, title="Guessing Game")
gui._setup_buttons(actions)
main_menu()
app.mainloop()
