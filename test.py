from tkinter import*
import time
window = Tk()

WIDTH = window.winfo_screenwidth()
HEIGHT = window.winfo_screenheight()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

bg= PhotoImage(file='background.png')
canvas.create_image(0, 0, image=bg,anchor=NW, tags="background1")
canvas.create_image(WIDTH, 0, image=bg,anchor=NW, tags="background2")

def bg_scroll():
    if canvas.coords("background2")[0] <= 0:
        canvas.move("background2", WIDTH, 0)
    if canvas.coords("background1")[0] + bg.width() == 0:
        canvas.move("background1", WIDTH, 0)
    canvas.move("background2", -2, 0)
    canvas.move("background1", -2, 0)
    window.after(15, bg_scroll)
bg_scroll()

window.mainloop()