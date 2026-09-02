import tkinter as tk
from tkinter import filedialog
import time

import global_variables

def choose_file(file_label):
	path = filedialog.askopenfilename()
	file_label.config(text=path if path else "No file selected")

def submit(url_var, file_label):
	print('URL:', url_var.get())
	print('File:', file_label.cget('text'))

import tkinter as tk


# animate
'''
	canvas
	ball
	root
	dx == delta x for ball position (speed)
	dt == time transpired by this animation script
'''

def animate(canvas, ball, root, dx, dt):
	if dt > global_variables.startup_length:
		return

	canvas.move(ball, dx, 0)
	x1, y1, x2, y2 = canvas.coords(ball)
	if x2 > 400 or x1 < 0:
		dx = -dx
	root.after(30, lambda: animate(canvas, ball, root,dx, dt+30))

class Gui:
	def __init__(self):
		self.root = tk.Tk()


	def finish(self, splash):
		splash.destroy()
		self.root.deiconify()


	def startup(self):
		# hide main window
		self.root.withdraw()

		# create splash root object
		splash = tk.Toplevel(self.root)
		splash.title("Loading...")
		canvas = tk.Canvas(splash, width=400, height=200, bg=global_variables.colors["background"])
		canvas.pack()

		# create ball and animate
		ball = canvas.create_oval(50, 80, 100, 130, fill="blue")
		animate(canvas, ball, self.root, dx=5, dt=0)

		# kill
		splash.after(global_variables.startup_length, lambda: self.finish(splash))





	def main_page(self):
		self.root.title(global_variables.program_name)

		tk.Label(self.root, text='Enter URL:').grid(row=0, column=0, padx=5, pady=5, sticky='w')
		url_var = tk.StringVar()
		tk.Entry(self.root, textvariable=url_var, width=50).grid(row=0, column=1, padx=5, pady=5)

		tk.Button(self.root, text='Choose File...', command=lambda: choose_file(file_label)).grid(row=1, column=0, padx=5, pady=5)
		file_label = tk.Label(self.root, text='No file selected', anchor='w')
		file_label.grid(row=1, column=1, padx=5, pady=5, sticky='w')

		tk.Button(self.root, text='Submit', command=lambda: submit(url_var, file_label)).grid(row=2, column=0, columnspan=2, pady=10)

		self.root.mainloop()