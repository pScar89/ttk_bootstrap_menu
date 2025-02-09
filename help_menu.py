import tkinter as tk


class HelpMenu(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        self.add_command(label='Welcome')
        self.add_command(label='About...')
