# -*- coding: utf-8 -*-
import tkinter as tk

class Application(tk.Frame):
    """docstring for Application"""
    def __init__(self):
        super (Application, self).__init__()
        self.grid()
        self.grid_Label = tk.Label(self, text = '.grid() func')
        self.grid_Label.grid()

app = Application()
app.mainloop()