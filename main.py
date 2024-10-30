from tkinter import Tk
from text_editor import TextEditor
from menu import create_menus

def main():
    window = Tk()
    window.title("Text Editor")

    editor = TextEditor(window)
    create_menus(window, editor)

    window.mainloop()

if __name__ == "__main__":
    main()