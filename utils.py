from tkinter import colorchooser

def change_color(text_area):
    color = colorchooser.askcolor(title="Pick a color: ")
    text_area.config(fg=color[1])

def change_font(text_area, font_name, font_size):
    text_area.config(font=(font_name.get(), font_size.get()))