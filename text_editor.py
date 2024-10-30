import os
from tkinter import *
from tkinter import font
from tkinter.messagebox import *
from tkinter.filedialog import *
from utils import change_color, change_font

class TextEditor:
    def __init__(self, window):
        self.window = window
        self.file = None

        self.window_width = 500
        self.window_height = 500
        self.screen_width = window.winfo_screenwidth()
        self.screen_height = window.winfo_screenheight()

        x = int((self.screen_width / 2) - (self.window_width / 2))
        y = int((self.screen_height / 2) - (self.window_height / 2))

        self.window.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, x, y))

        self.font_name = StringVar(window)
        self.font_name.set("Arial")

        self.font_size = StringVar(window)
        self.font_size.set("25")

        self.text_area = Text(window, font=(self.font_name.get(), self.font_size.get()))

        self.scroll_bar = Scrollbar(self.text_area, command=self.text_area.yview)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        self.text_area.grid(sticky=N + E + S + W)

        frame = Frame(window)
        frame.grid()

        color_button = Button(frame, text="Text colour", command=lambda: change_color(self.text_area))
        color_button.grid(row=0, column=0)

        font_box = OptionMenu(frame, self.font_name, *font.families(), command=lambda _: change_font(self.text_area, self.font_name, self.font_size))
        font_box.grid(row=0, column=1)

        size_box = Spinbox(frame, from_=1, to=100, textvariable=self.font_size, command=lambda: change_font(self.text_area, self.font_name, self.font_size))
        size_box.grid(row=0, column=2)

        self.scroll_bar.pack(side="right", fill="y")
        self.text_area.config(yscrollcommand=self.scroll_bar.set)

    def new_file(self):
        self.window.title("Untitled")
        self.text_area.delete(1.0, END)

    def open_file(self):
        file = askopenfilename(defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")])

        try:
            self.window.title(os.path.basename(file))
            self.text_area.delete(1.0, END)

            with open(file, "r") as file:
                self.text_area.insert(1.0, file.read())
        except Exception as e:
            showerror("Couldn't read the file", str(e))

    def save_file(self):
        file = asksaveasfilename(initialfile='untitled.txt',
                                 defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])

        if file is None:
            return
        else:
            try:
                self.window.title(os.path.basename(file))
                with open(file, "w") as file:
                    file.write(self.text_area.get(1.0, END))
            except Exception as e:
                showerror("Couldn't save the file", str(e))

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def about(self):
        showinfo("About", "This is a Python-based text editor written by a Python guru :<)")

    def quit(self):
        self.window.destroy()