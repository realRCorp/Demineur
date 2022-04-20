## Copyright Yapudpil pour RCorp™
from tkinter import *
from tkinter.ttk import *
import global_var as gv


class Launcher:
    def __init__(self,root):
        self.root = root
        self.frame = self.create_frame()
        self.rows = IntVar(self.frame, 1)
        self.cols = IntVar(self.frame, 1)
        self.diff = StringVar(self.frame, 'Facile')
        self.create_interface()
        self.root.mainloop()

    def create_interface(self):
        title = Label(self.frame,text='DÉMINEUR', style='title.TLabel')
        title.grid(column=0, row=0, columnspan=2)

        self.row_input()
        self.col_input()
        self.diff_input()

        button = Button(self.frame, text='Valider', command=self.close_menu)
        button.grid(column=0,row=4, columnspan=2)

        info = Label(self.frame, text = ("A titre indicatif, voici la taille du démineur Google pour chacune des difficultés :\n"
                                         "-Facile : 10 colonnes, 8 lignes\n"
                                         "-Moyen : 18 colonnes, 14 lignes\n"
                                         "-Difficile : 24 colonnes, 20 lignes"))
        info.grid(row=5, column=0, columnspan=2)

    def create_frame(self):
        frame = Frame(self.root)
        frame.grid(column=0, row=0, sticky=NSEW, padx=4, pady=4)
        frame.columnconfigure(0,weight=1, pad=4)
        frame.columnconfigure(1,weight=1)
        frame.rowconfigure(1, pad=4)
        frame.rowconfigure(2, pad=4)
        frame.rowconfigure(3, pad=4)
        return frame

    def row_input(self):
        label = Label(self.frame, text='Nombre de lignes :')
        spin = Spinbox(self.frame, from_=1, to=30, textvariable=self.rows, wrap=True, state='readonly')
        label.grid(column=0, row=1, sticky=W)
        spin.grid(column=1, row=1, sticky=E)

    def col_input(self):
        label = Label(self.frame, text='Nombre de colonnes :')
        spin = Spinbox(self.frame, from_=1, to=30, textvariable=self.cols, wrap=True, state='readonly')
        label.grid(column=0, row=2, sticky=W)
        spin.grid(column=1, row=2, sticky=E)

    def diff_input(self):
        label = Label(self.frame, text='Difficulté :')
        cbox = Combobox(self.frame, values=('Facile', 'Moyen', 'Difficile'), textvariable=self.diff, state='readonly')
        label.grid(column=0, row=3, sticky=W)
        cbox.grid(column=1, row=3, sticky=E)

    def close_menu(self):
        gv.rows = self.rows.get()
        gv.cols = self.cols.get()
        gv.diff = self.diff.get()
        self.frame.destroy()
        self.root.quit()
