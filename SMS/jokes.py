import tkinter as tk

import pyjokes


def joke():
    textbox.configure(state="normal")
    textbox.delete("1.0", tk.END)
    textbox.insert("1.0", pyjokes.get_joke("en", "neutral"))
    textbox.configure(state="disabled")


def root_window():
    global textbox

    # root window
    root = tk.Tk()
    root.title("PyJokes Generator")
    root.geometry("500x200")

    # window label
    label = tk.Label(root, text="PyJokes Generator")
    label.pack(side="top", pady=10)

    # joke textbox
    textbox = tk.Text(root, height=5, width=60)
    textbox.pack(side="top", pady=10)
    textbox.configure(state="disabled")

    joke()
    tk.mainloop()


root_window()
