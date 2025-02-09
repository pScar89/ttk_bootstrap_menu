import tkinter as tk
from .themes_menu import ThemesMenu


class PrefsMenu(tk.Menu):
    def __init__(self, parent, window):
        super().__init__(parent)

        self.themes_menu = ThemesMenu(self, window)
        self.add_cascade(label='Theme', menu=self.themes_menu)
