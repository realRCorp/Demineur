## Copyright Yapudpil pour RCorp™
from tkinter import *
from tkinter.ttk import *

class Display:
    def __init__(self, rows, cols, manager):
        self.rows = rows
        self.cols = cols
        self.manager = manager

        self.frame = Frame()
        self.childs = []
        self.fill_frame()

    def fill_frame(self):
        for r in range(self.rows):
            for c in range(self.cols):
                square = Label(self.frame, text='', width=2, style='undiscovered.GridLabel.TLabel')
                square.grid(row=r, column=c, sticky=NSEW)
                self.childs.append(square)
                if self.manager is not None:  # No manager -> no interactive buttons (usefull for displaying solution)
                    square.bind('<1>', self.left_click(r,c))
                    square.bind('<3>', self.right_click(r,c))

    def left_click(self, r, c):
        return lambda event: self.manager.discover(r,c)

    def right_click(self, r, c):
        return lambda event: self.manager.flag(r,c)

    def update(self, value, r, c):
        # Note: the square of coordinates (r,c) corresponds to the label of index (r * cols + c) in the childs list
        text_index = {-3:'B', -2:'D', -1:'', 0:' ', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8'}
        style_index= {-3:'bomb', -2:'flag', -1:'undiscovered', 0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8'}

        self.childs[r * self.cols + c]['text']  = text_index[value]
        self.childs[r * self.cols + c]['style'] = style_index[value] + '.GridLabel.TLabel'