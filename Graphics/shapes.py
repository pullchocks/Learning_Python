from tkinter import *
from tkinter import colorchooser
import random

tk = Tk()

canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_line(0, 0, 500, 500)
canvas.create_rectangle(100, 100, 300, 300)
canvas.create_rectangle(10, 10, 300, 50)
canvas.create_rectangle(10, 10, 50, 300)

def rec_color():
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'black']
    return random.choice(colors)

def random_rectangle():
    x1 = random.randrange(500)
    y1 = random.randrange(500)
    x2 = random.randrange(500)
    y2 = random.randrange(500)
    canvas.create_rectangle(x1, y1, x2, y2, fill=rec_color())
    
btn = Button(tk, text="click me", command=random_rectangle)
btn.pack()
    
def random_rectangle_picked():
    x1 = random.randrange(500)
    y1 = random.randrange(500)
    x2 = random.randrange(500)
    y2 = random.randrange(500)
    c = colorchooser.askcolor()
    canvas.create_rectangle(x1, y1, x2, y2, fill=c[1])

btn = Button(tk, text="pick color", command=random_rectangle_picked)
btn.pack()

tk.mainloop()