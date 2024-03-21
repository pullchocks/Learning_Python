def hello():
    print('Hello, world')

from tkinter import *
tk = Tk()
btn = Button(tk, text="click me", command=hello)
btn.pack()

tk.mainloop()