import tkinter as tk


def set_massage():
    text = text_input.get()
    title_window.configure(text=text)

window = tk.Tk()
window.title('My window')
window.minsize(400,400)

title_window = tk.Label(master=window, text='Shay ')
title_window.pack()

text_input = tk.Entry(master=window)
text_input.pack()


btn = tk.Button(master=window,text='value',command=set_massage)
btn.pack()

window.mainloop()