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



# animate
'''
	canvas
	ball
	root
	dx == delta x for ball position (speed)
	dt == time transpired by this animation script
'''
def animate(canvas, ball, root, dx, dt):
	if dt > global_variables.startup_length-30:
		return

	canvas.move(ball, dx, 0)
	x1, y1, x2, y2 = canvas.coords(ball)
	if x2 > 400 or x1 < 0:
		dx = -dx
	root.after(30, lambda: animate(canvas, ball, root,dx, dt+30))




class Gui:
	def __init__(self):
		self.root = tk.Tk()


	# finish
	"""
		finish a TK root and/or splashscreen
		splash: the screen
		splash_root: root 
	"""
	def finish(self, splash, splash_root):
		splash.destroy()
		splash_root.destroy()

		# make root visible again
		self.root.deiconify()



	# startup
	"""
		startup script with visuals
		point to script which runs this
	"""
	def startup(self):
		import gui.startup_gui as startup
		startup.startup(self.root, self.finish, animate)



	# main page
	"""
		this is the page most operations will run through
		point to script which runs this
	"""
	def main_page(self):
		import gui.main_gui as main_gui
		main_gui.main_page(choose_file, submit, self.root)