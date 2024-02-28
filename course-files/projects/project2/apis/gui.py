import customtkinter

app = None
textbox = None

__docformat__ = "google"

def _setup_window(in_app, title):
    global app
    app = in_app
    app.title(title)
    app.minsize(1000, 400)
    app.grid_columnconfigure(0, weight=10)
    app.grid_rowconfigure((0,1,2,3), weight=1, uniform=1)
    global textbox
    textbox = customtkinter.CTkTextbox(app)
    textbox.grid(row=0, column=0, rowspan=4, columnspan=1, padx=10, pady=(10, 10), sticky="nsew")
    
def _setup_buttons(some_actions):
    button_count = 0
    for button in some_actions:
        _make_button(text=button, function=some_actions[button], grid_row=button_count // 2, grid_col=button_count % 2 + 1)
        button_count += 1
        
def show_text(txt, append=False):
    '''
    This allows us to "print" text to the textbox on the GUI.

    Args:
        txt (`str`): whatever text you'd like printed to the screen.
        append (`bool`): whether or not you'd like to append the text to what's there currently.

    Returns:
        `None` but instead updates the GUI's textbox appropriately.
    '''
    global textbox
    textbox.configure(state="normal")
    if not append:
        textbox.delete("0.0", "end")
    textbox.insert("insert", txt + "\n")
    textbox.configure(state="disabled")

def popup_input(prompt=""):
    '''
    This allows us to ask for "input" from our GUI. It pops-up a window with a given prompt.

    Args:
        prompt (`str`): whatever text you'd like to be shown in the pop-up window.
        
    Returns:
        a `str` containing what the user typed in the pop-up window. If they didn't enter anything or if they clicked Cancel it will return `None`.
    '''
    dialog = customtkinter.CTkInputDialog(text=prompt, title="Input Popup")
    return dialog.get_input()

def _make_button(text="", function=None, grid_row=None, grid_col=None):
    new_button = customtkinter.CTkButton(app, text=text, command=function)
    if grid_row is None or grid_col is None:
        new_button.pack(padx=20, pady=20)
    else:
        new_button.grid(padx=5, pady=5, row=grid_row, column=grid_col)
