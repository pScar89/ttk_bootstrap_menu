import tkinter as tk


class FileMenu(tk.Menu):
    def __init__(self, parent, window):
        super().__init__(parent, tearoff=False)
        self.window = window
        self.add_command(
            label='N' + "\u0332" + 'ew',
            command=lambda: print('New File'))
        self.add_command(
            label='O' + "\u0332" + 'pen...',
            command=lambda: print('Open File'))
        self.add_command(
            label='C' + "\u0332" + 'lose',
            command=lambda: print('Open File'))

        self.add_separator()

        self.add_command(label='Exit', command=self.window.destroy)
