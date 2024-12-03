import tkinter as tk
from tkinter import PhotoImage

# The Function
def handle_submit():
    n = 0
    input = entry.get()
    input_clone = input.lower()
    split = [char for char in input_clone]
    for item in split:
        if item == 'r':
            n+=1
    if n == 0:
        result_label.config(text=f"The word {input} has no instances of the letter R")
    else:
        result_label.config(text=f"The word {input} has {n} instances of the letter R")
    entry.delete(0, tk.END)

# Window Settings
window = tk.Tk()
window.resizable(False, False)
window.title("The R Detector") 
window.geometry("450x400")
window.iconbitmap("icon.ico")
icon = PhotoImage(file="pngicon.png")
window.iconphoto(True, icon)
# The GUI buttons and stuff
title = tk.Label(
    text="The R Detector",
    font=("Helvetica", 20),
)
label = tk.Label(
    text="Enter Word",
    foreground = "black",
    width = 45,
    height = 1
    )
entry = tk.Entry(
    fg="black",
    bg="lightgray", 
    width=60,
)
submit_button = tk.Button(
    text="Submit",
    command=handle_submit,
    fg="black",
    bg="lightgray",
    width= 30,
    height= 2
)
result_label = tk.Label(
    text="",
    fg="black",
    bg="lightgray",
    width=60,
    height=2
)
blurb = tk.Label(
    text= "This application was made as a joke. The context is when comparing to AI models\n (as of 2024) a lot of them including some from OpenAI as well as Apple Inteligence\n and Gemini could not accuratly tell us how many instances of the letter R were in\n the word Strawberry."
)

# Building the window
title.pack()
tk.Label(window, text="", height=1).pack()
label.pack()
tk.Label(window, text="", height=1).pack()
entry.pack()
tk.Label(window, text="", height=1).pack()
submit_button.pack(pady=5)  # Add padding
tk.Label(window, text="", height=1).pack()
result_label.pack(pady=10)
tk.Label(window, text="", height=1).pack()
tk.Label(window, text="", height=1).pack()
blurb.pack()
window.mainloop()