import tkinter as tk
# from file_menu import FileMenu
from .file_menu import FileMenu
from .prefs_menu import PrefsMenu
from .help_menu import HelpMenu


class BaseMenu(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        self.file_menu = FileMenu(self, parent)
        self.add_cascade(label='File', menu=self.file_menu)

        self.prefs_menu = PrefsMenu(self, parent)
        self.add_cascade(label='Preferences', menu=self.prefs_menu)

        self.help_menu = HelpMenu(self)
        self.add_cascade(label='Help', menu=self.help_menu)
