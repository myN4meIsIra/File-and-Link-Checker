# created by Ira Garrett
"""
    main window
"""

import global_variables
import tkinter as tk

def main_page(choose_file, submit, root):
    root.title(global_variables.program_name)

    tk.Label(root, text='Enter URL:').grid(row=0, column=0, padx=5, pady=5, sticky='w')
    url_var = tk.StringVar()
    tk.Entry(root, textvariable=url_var, width=50).grid(row=0, column=1, padx=5, pady=5)

    tk.Button(root, text='Choose File...', command=lambda: choose_file(file_label)).grid(row=1, column=0, padx=5,
                                                                                              pady=5)
    file_label = tk.Label(root, text='No file selected', anchor='w')
    file_label.grid(row=1, column=1, padx=5, pady=5, sticky='w')

    tk.Button(root, text='Submit', command=lambda: submit(url_var, file_label)).grid(row=2, column=0, columnspan=2,
                                                                                          pady=10)

    root.mainloop()