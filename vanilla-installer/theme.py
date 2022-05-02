import os
import tkinter
import darkdetect
import tkinter.messagebox

FILE = 'data/theme.txt'

def init():
    """Checks if the theme file exists and creates it if not. Also checks the theme of the OS and edits the file accordingly.
    """
    if not os.path.exists('theme.txt'):
        open(FILE, 'w').write('dark' if darkdetect.isDark() else 'light')

def is_dark(to: bool=None) -> bool:
    """Change or get the status of dark mode.

    Args:
        to (bool, optional): Status. Defaults to None (just get status, without editing it).

    Returns:
        bool: theme
    """
    if to: # change
        open(FILE, 'w').write('dark' if to else 'light')
    return open(FILE).read() == 'dark'

def load() -> dict:
    """Returns the current theme dictionary.

    Returns:
        _type_: _description_
    """
    if is_dark():
        return {
            'fg': 'white',
            'bg': '#0E0F13',
            'light': '#008AE6',
            'warn': '#fc9d19',
            'critical': '#fc3b19',
            'ok': '#28ff02'
        }
    else:
        return {
            'fg': 'black',
            'bg': 'white',
            'light': '#008AE6',
            'warn': '#fc9d19',
            'critical': '#fc3b19',
            'ok': '#28ff02'
        }

def toggle(popup: bool=True):
    """Switches between dark and light theme

    Args:
        popup (bool, optional): Wether to show a informational popup which asks to exit the program. Defaults to True.
    """
    is_dark(not is_dark())

    if popup:
        if tkinter.messagebox.askyesno(title='Theme Toggle', message='The changes will apply after restarting.\nExit program now? (You need to start the program again for yourself.'):
            exit()
            
init()