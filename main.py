## Copyright Yapudpil pour RCorp™
from tkinter import *
from tkinter.ttk import *

import global_var as gv
import launcher
import display
import game_front
import game_manager
import game_end

root = Tk()
root.iconbitmap('assets/logo.ico')
root.title('Démineur')
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
root.protocol("WM_DELETE_WINDOW", lambda: gv.close_game(root))

gv.create_styles(root)

while True:
	gv.victory = None
	launcher.Launcher(root)

	game = game_front.Game(root)
	manager = game_manager.Manager(game, gv.rows, gv.cols, gv.diff)
	game_display = display.Display(gv.rows, gv.cols, manager)
	game.add_display(game_display)
	game.start()

	if gv.victory is not None:
		# Selects which grid must be displayed on the end screen
		if gv.victory:
			grid = manager.player_grid
		else:
			grid = manager.solution
		end = game_end.End(root, gv.victory, grid)
		end_display = display.Display(gv.rows, gv.cols, manager=None)
		end.add_display(end_display)
		end.start()