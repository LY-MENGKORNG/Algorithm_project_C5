from tkinter import *

window = Tk()
window.geometry("800x600")
canvas = Canvas(window, width=800, height=600)
canvas.pack()

canvas.create_rectangle(100, 100, 150, 600, fill="red", tags="wall")
canvas.create_rectangle(400, 100, 450, 600, fill="red", tags="wall")

get_img = PhotoImage(file="frog2.png")
canvas.create_image(200, 300, image=get_img, anchor=NW, tags="player")

def check_move(event):
    if event.keysym == "Left":
        Move_left(-10, 0)
    elif event.keysym == "Right":
        Move_right(10, 0)

def check_overlap():
    coord = canvas.coords("player")
    plfs = canvas.find_withtag("wall")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + get_img.width(), coord[1]+get_img.height())
    for plf in plfs:
        if plf in overlap:
            return False
    return True

def Move_left(x, y):
    if check_overlap():
        canvas.move("player", x, y)

def Move_right(x, y):
    if check_overlap():
        canvas.move("player", x, y)

window.bind("<Key>", check_move)

window.mainloop()
