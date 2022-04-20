## Copyright Yapudpil pour RCorp™
from tkinter import *
from tkinter.ttk import *
import global_var as gv

class End:
	def __init__(self, root, victory, grid):
		self.root = root
		self.victory = victory
		self.grid = grid

		self.frame = self.create_frame()
		self.create_interface()

	def create_frame(self):
		frame = Frame(self.root)
		frame.grid(row=0, column=0, sticky=NSEW, padx=4, pady=4)
		frame.columnconfigure(0, weight=1)
		frame.columnconfigure(3, weight=1)
		frame.columnconfigure(2, pad=20)
		frame.rowconfigure(0, pad=5)
		return frame

	def create_interface(self):
		title = Label(self.frame, text='DÉMINEUR', style='title.TLabel')
		title.grid(column=0, row=0, columnspan=4)

		if self.victory:
			txt = 'BRAVO ! Vous avez gagné'
		else:
			txt = 'Dommage, vous avez perdu. Voici la solution :'
		msg = Label(self.frame, text=txt, style='endMsg.TLabel')
		msg.grid(row=1, column=1, columnspan=4, sticky=W)

		restart_button = Button(self.frame, text='Recommencer', command=self.close_menu)
		restart_button.grid(row=2, column=2)

		close_button = Button(self.frame, text='Quitter', command=lambda: gv.close_game(self.root))
		close_button.grid(row=3, column=2)

	def add_display(self, display):
		self.display = display
		self.display.frame.grid(in_=self.frame, row=2, column=1, rowspan=10)

		for r in range(self.display.rows):
			for c in range(self.display.cols):
				self.display.update(self.grid[r][c], r, c)

	def start(self):
		self.root.mainloop()

	def close_menu(self):
		self.frame.destroy()
		self.root.quit()