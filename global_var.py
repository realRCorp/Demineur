## Copyright Yapudpil pour RCorp™
from tkinter import *
from tkinter.ttk import *
import sys

rows = 3
cols = 3
diff = 'Facile'
victory = None

def close_game(root):
    root.destroy()
    sys.exit()

def create_styles(root):
    s = Style(root)

    # Interface style
    s.configure('title.TLabel', font='TkDefaultFont 13 bold')
    s.configure('endMsg.TLabel', font='TkDefaultFont 11')
    s.configure('error.TLabel', foreground = 'red')

    # Grid style
    s.configure('GridLabel.TLabel', relief='solid', borderwidth=1, font='TkDefaultFont 10 bold', anchor=CENTER) # Common attributes
    s.configure('undiscovered.GridLabel.TLabel', background='#96c1f2')
    s.configure('bomb.GridLabel.TLabel', background = '#000000', foreground='#ffffff')
    s.configure('flag.GridLabel.TLabel', background = '#5adb67')
    s.configure('0.GridLabel.TLabel')  # Useless but may be customized later
    s.configure('1.GridLabel.TLabel', foreground='#2112c4')
    s.configure('2.GridLabel.TLabel', foreground='#0b9e3c')
    s.configure('3.GridLabel.TLabel', foreground='#cc0000')
    s.configure('4.GridLabel.TLabel', foreground='#820075')
    s.configure('5.GridLabel.TLabel', foreground='#f0e400')
    s.configure('6.GridLabel.TLabel', foreground='#14b5ad')
    s.configure('7.GridLabel.TLabel', foreground='#000000')
    s.configure('8.GridLabel.TLabel', foreground='#850049')
