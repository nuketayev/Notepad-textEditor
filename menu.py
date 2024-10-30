from tkinter import *

def create_menus(window, editor):
    menu_bar = Menu(window)
    window.config(menu=menu_bar)

    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="New", command=editor.new_file)
    file_menu.add_command(label="Open", command=editor.open_file)
    file_menu.add_command(label="Save", command=editor.save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=editor.quit)

    edit_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    edit_menu.add_command(label="Copy", command=editor.copy)
    edit_menu.add_command(label="Paste", command=editor.paste)
    edit_menu.add_command(label="Cut", command=editor.cut)

    help_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    help_menu.add_command(label="About", command=editor.about)