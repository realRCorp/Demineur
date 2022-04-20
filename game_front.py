## Copyright Yapudpil pour RCorp™
from tkinter import *
from tkinter.ttk import *
import global_var as gv

class Game:
	def __init__(self, root):
		self.root = root

		self.frame = self.create_frame()
		self.flags = IntVar(self.frame)
		self.error_msg = StringVar(self.frame)
		self.create_interface()

	def create_frame(self):
		frame = Frame(self.root)
		frame.grid(column=0, row=0, sticky=NSEW, padx=4, pady=4)
		frame.columnconfigure(0, weight=1)
		frame.columnconfigure(4, weight=1)
		frame.columnconfigure(2, pad=2)
		frame.rowconfigure(0, pad=5)
		return frame

	def create_interface(self):
		title = Label(self.frame, text='DÉMINEUR', style='title.TLabel')
		title.grid(column=0, row=0, columnspan=5)

		flag_text = Label(self.frame, text='Drapeaux restants : ')
		flag_count = Label(self.frame, textvariable=self.flags)
		flag_text.grid(row=1, column=2, sticky=S)
		flag_count.grid(row=1, column=3, sticky=S)

		restart_button = Button(self.frame, text='Recommencer', command=self.close_menu)
		restart_button.grid(row=2, column=2, columnspan=2)

		close_button = Button(self.frame, text='Quitter', command=lambda: gv.close_game(self.root))
		close_button.grid(row=3, column=2, columnspan=2, sticky=N)

		error_lbl = Label(self.frame, textvariable=self.error_msg)
		error_lbl.grid(row=20, column=0, columnspan=5)

	def add_display(self, display):
		self.display = display
		self.display.frame.grid(in_=self.frame, row=1, column=1, rowspan=10)

	def start(self):
		self.root.mainloop()

	def close_menu(self):
		self.display.frame.grid_forget()
		self.frame.destroy()
		self.root.quit()
