import tkinter as tk
import ttkbootstrap.themes.standard as ttk_themes

THEMES = ttk_themes.STANDARD_THEMES


class ThemesMenu(tk.Menu):
    def __init__(self, parent, window):
        super().__init__(parent)

        self.window = window

        self.dark_themes = tk.Menu(self)
        self.light_themes = tk.Menu(self)

        self.add_theme_options(self.dark_themes, 'dark')
        self.add_theme_options(self.light_themes, 'light')

        self.add_cascade(label='Dark Themes', menu=self.dark_themes)
        self.add_cascade(label='Light Themes', menu=self.light_themes)

    def add_theme_options(self, menu, color) -> None:
        for theme, settings in THEMES.items():
            if settings['type'] == color:
                menu.add_radiobutton(
                    label=theme.capitalize(),
                    command=lambda theme_code=theme:
                        self.window.style.theme_use(themename=theme_code))
