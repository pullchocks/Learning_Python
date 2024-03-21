import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=1000, height=1000)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(1, 61):
    canvas.move(1, 5, 5)
    tk.update()
    time.sleep(0.05)
    
for x in range(1, 61):
    canvas.move(1, -5, -5)
    tk.update()
    time.sleep(0.05)
    
canvas.create_text(150, 150, text="Use arrow keys to move triangle.", font=("Times", 12))
    
def movetriangle_right(event):
    canvas.move(1, 5, 0)
    
def movetriangle_left(event):
    canvas.move(1, -5, 0)
    
def movetriangle_up(event):
    canvas.move(1, 0, -5)
    
def movetriangle_down(event):
    canvas.move(1, 0, 5)
    
canvas.bind_all('<KeyPress-Right>', movetriangle_right)
canvas.bind_all('<KeyPress-Left>', movetriangle_left)
canvas.bind_all('<KeyPress-Up>', movetriangle_up)
canvas.bind_all('<KeyPress-Down>', movetriangle_down)

tk.mainloop()