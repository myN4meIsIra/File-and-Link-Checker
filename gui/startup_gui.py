# created by Ira Garrett
"""
startup splash screen
"""

import tkinter as tk
import global_variables

def startup(root, finish, animate):
    # hide main window
    root.withdraw()

    # create and hide new window
    splash_root = tk.Tk()
    splash_root.withdraw()

    # create splash root object
    splash = tk.Toplevel(splash_root)
    splash.title("Loading...")
    canvas = tk.Canvas(splash, width=400, height=200, bg=global_variables.colors["background"])
    canvas.pack()

    # create ball and animate
    ball = canvas.create_oval(50, 80, 100, 130, fill="blue")
    animate(canvas, ball, splash_root, dx=5, dt=0)

    # kill startup screen
    splash.after(global_variables.startup_length,
                 lambda: finish(splash, splash_root)
                 )

