import customtkinter
from tkinter import messagebox 

app = None
textbox = None

__docformat__ = "google"

def _setup_window(in_app, title):
    global app
    app = in_app
    app.title(title)
    app.minsize(1400, 700)
    app.grid_columnconfigure(0, weight=10)
    app.grid_rowconfigure((0,1,2,3), weight=1, uniform=1)
    global textbox
    textbox = customtkinter.CTkTextbox(app, font=("Courier New", 14))
    textbox.grid(row=0, column=0, rowspan=4, columnspan=1, padx=10, pady=(10, 10), sticky="nsew")
    
def _setup_buttons(some_actions):
    button_count = 0
    for button in some_actions:
        _make_button(text=button, function=some_actions[button], grid_row=button_count // 2, grid_col=button_count % 2 + 1)
        button_count += 1
        
def clear():
    '''
    This allows us to "clear" text from the textbox on the GUI.

    Returns:
        `None` but instead updates the GUI's textbox appropriately.
    '''
    global textbox
    textbox.configure(state="normal")
    textbox.delete("0.0", "end") 
    textbox.configure(state="disabled")
           

def print(*txt, sep=" ", end="\n"):
    '''
    This allows us to "print" text to the textbox on the GUI.

    Args:
        txt (`str`): whatever text you'd like printed to the screen (note: like the `print` function you can give it as many inputs as you'd like!)
        sep (`str`): default separator to be used with multiple text arguments (like `print`)
        end (`str`): default ending character to be used (like `print`)

    Returns:
        `None` but instead updates the GUI's textbox appropriately.
    '''
    global textbox
    textbox.configure(state="normal")

    plain_text = []
    for x in txt:
        tmp_x = x
        if isinstance(x, type({}.keys())):
            tmp_x = list(x)
        plain_text.append(str(tmp_x))

    textbox.insert("insert", sep.join(plain_text) + end)
    textbox.configure(state="disabled")

def popup(message:str, title:str="Pop-Up", kind="info"):
    '''
    This allows us to create a pop-up a window without any prompt.

    Args:
        message (`str`): whatever text you'd like to be shown in the pop-up window.
        title (`str`): the title of the window.
        kind (`str`): Either `"info"`, `"warning"`, or `"error"`. Just changes the icon in the pop-up.

    Returns:
        `None` just shows the window.
    '''
    if kind not in ['info', 'warning', 'error']:
        raise Exception("Not a valid popup type!")

    if kind == "info":
        messagebox.showinfo(title=title, message=message)
    elif kind == "warning":
        messagebox.showwarning(title=title, message=message)
    elif kind == "error":
        messagebox.showerror(title=title, message=message)
        
def input(prompt=""):
    '''
    This allows us to ask for "input" from our GUI. It pops-up a window with a given prompt.

    Args:
        prompt (`str`): whatever text you'd like to be shown in the pop-up window.
        
    Returns:
        a `str` containing what the user typed in the pop-up window. If they didn't enter anything or if they clicked Cancel it will return `None`.
    '''
    dialog = customtkinter.CTkInputDialog(text=prompt, title="Input Popup")
    dialog.wm_resizable(True, True)
    dialog.after(200, dialog.focus_force())
    text = dialog.get_input()
    if text == "":
        text = None
    return text

def _make_button(text="", function=None, grid_row=None, grid_col=None):
    new_button = customtkinter.CTkButton(app, text=text, command=function)
    if grid_row is None or grid_col is None:
        new_button.pack(padx=20, pady=20)
    else:
        new_button.grid(padx=5, pady=5, row=grid_row, column=grid_col)
