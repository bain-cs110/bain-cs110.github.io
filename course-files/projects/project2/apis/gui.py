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


def numeric_input(start_value: int, end_value: int, prompt: str = "Select an option from the dropdown:"):
    '''
    This allows us to ask for a number from our GUI. It pops-up a window with a dropdown menu where a user can select a number between
    `start_value` and `end_value`

    Args:
        start_value (`int`): the first number to present as an option
        end_value (`int`): the last number to present as an option
        prompt (`str`): whatever text you'd like to be shown in the pop-up window.
        
    Returns:
        an `int` that the user selected. If they clicked Cancel it will return `None`.
    '''
    
    list_of_string_numbers = []
    for i in range(start_value, end_value + 1):
        list_of_string_numbers.append(str(i))
    
    dialog = DropdownPopup(app, title="Dropdown Input Pop-Up", prompt=prompt, options=list_of_string_numbers)
    dialog.wm_resizable(True, True)
    dialog.after(200, dialog.focus_force())
    
    # Wait for user input and get the result
    selected_value = dialog.get_input()
    if selected_value is not None:
        return int(selected_value)
    else:
        return None


def _make_button(text="", function=None, grid_row=None, grid_col=None):
    new_button = customtkinter.CTkButton(app, text=text, command=function)
    if grid_row is None or grid_col is None:
        new_button.pack(padx=20, pady=20)
    else:
        new_button.grid(padx=5, pady=5, row=grid_row, column=grid_col)


class DropdownPopup(customtkinter.CTkToplevel):
    def __init__(self, parent, title, prompt, options):
        super().__init__(parent)
        self.title(title)
        self.grab_set()  # Make the dialog modal
        self.focus_force()  # Force focus to the dialog

        self.options = options
        self.result = None

        # Label
        self.label = customtkinter.CTkLabel(self, text=prompt)
        self.label.pack(pady=20)

        # Dropdown (CTkComboBox)
        self.combobox = customtkinter.CTkComboBox(self, values=self.options)
        self.combobox.pack(pady=20)
        self.combobox.set(self.options[0])  # Set default value

        # OK Button
        self.ok_button = customtkinter.CTkButton(
            self, text="OK", command=self.on_ok)
        self.ok_button.pack(pady=10)

    def on_ok(self):
        self.result = self.combobox.get()
        self.destroy()  # Close the dialog

    def get_input(self):
        # Wait for the window to be closed before returning the result
        self.wait_window()
        return self.result

