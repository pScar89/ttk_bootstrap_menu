import tkinter as tk
import ttkbootstrap as ttk
import ttkbootstrap.themes.standard as ttk_themes


window = ttk.Window(themename='solar')

window.title('Menus')
window.geometry('1000x1000')
window.bind('<KeyPress-Escape>', lambda event: window.destroy())


menu_bar = tk.Menu(window)

file_menu = tk.Menu(menu_bar)
file_menu.add_command(label='New', command=lambda: print('New File'))
file_menu.add_command(label='Open...', command=lambda: print('Open File'))
file_menu.add_command(label='Close', command=lambda: print('Open File'))

file_menu.add_separator()

file_menu.add_command(
    label='Exit',
    command=window.destroy
)

menu_bar.add_cascade(label='File', menu=file_menu)

help_menu = tk.Menu(menu_bar)
help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

menu_bar.add_cascade(label='Help', menu=help_menu)

help_check_str = tk.StringVar()
help_menu.add_checkbutton(
    label='Tutorial Mode',
    onvalue='on',
    offvalue='off',
    variable=help_check_str,)

menu_button = ttk.Menubutton(window, text='Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button)
button_sub_menu.add_command(label='Entry', command=lambda: print('test'))
button_sub_menu.add_checkbutton(label='Check 1')
menu_button.configure(menu=button_sub_menu)

edit_menu = tk.Menu(menu_bar)

edit_menu.add_command(label='Undo       ctrl+z',
                      command=lambda: print('Undo'))
edit_menu.add_command(label='Redo       ctrl+y', command=lambda: print('Redo'))

edit_menu.add_separator()

edit_menu.add_command(
    label='Cut        ctrl+x',
    command=lambda: print('Cut'))
edit_menu.add_command(
    label='Copy       ctrl+c',
    command=lambda: print('Copy'))
edit_menu.add_command(
    label='Paste      ctrl+v',
    command=lambda: print('Paste'))

edit_menu.add_separator()

prefs_menu = tk.Menu(edit_menu)

prefs_menu.add_checkbutton(
    label='Dark Mode',
    command=lambda: print('Dark Mode On'))
prefs_menu.add_checkbutton(
    label='Big Text Mode',
    command=lambda: print('Big Text On'))

edit_menu.add_cascade(label='Preferences', menu=prefs_menu)

menu_bar.add_cascade(label='Edit', menu=edit_menu)

themes_menu = tk.Menu(menu_bar)

themes = {
    'Solar': 'solar',
    'Superhero': 'superhero',
    'Darkly': 'darkly',
    'Vapor': 'vapor',
    'Cosmo': 'cosmo',
    'Flatly': 'flatly',
    'Journal': 'journal',
    'Litera': 'litera',
    'Lumen': 'lumen',
    'Morph': 'morph',
}
themes = ttk_themes.STANDARD_THEMES


def add_theme_options() -> None:
    for theme in themes:
        themes_menu.add_radiobutton(
            label=theme.capitalize(),
            command=lambda theme_code=theme:
                window.style.theme_use(themename=theme_code))


add_theme_options()

menu_bar.add_cascade(label='Themes', menu=themes_menu)

window.configure(menu=menu_bar)

window.mainloop()
