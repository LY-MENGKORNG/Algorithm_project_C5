from tkinter import *
import random

window = Tk()
window.title("Frog catch Flies")
icon = PhotoImage(file='frog_icon.png')
window.iconphoto(False, icon)

# constance 
APP_WIDTH = 1280
APP_HEIGHT = 650
BG_FRAME = "gray"
BG_CANVAS = "lightseagreen"

# App center
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight() - 70
x = int((screen_width / 2) - (APP_WIDTH / 2))
y = int((screen_height / 2) - (APP_HEIGHT / 2))
window.geometry(f'{APP_WIDTH}x{APP_HEIGHT}+{x}+{y}')

# Frame
frame = Frame(window, width=APP_WIDTH, height=APP_HEIGHT, bg=BG_FRAME)
frame.pack()

# Canvas
canvas = Canvas(frame,width=APP_WIDTH, height=APP_HEIGHT, bg=BG_CANVAS)
canvas.pack()

# Clouds
cloud_img = PhotoImage(file='clound.png')
canvas.create_image(10, 100, image=cloud_img, anchor=NW,  tags="cloud")
canvas.create_image(300, 200, image=cloud_img, anchor=NW, tags="cloud")
canvas.create_image(800, 250, image=cloud_img, anchor=NW, tags="cloud")

# Sun 
sun_img = PhotoImage(file='sun.png')
canvas.create_image(10, 10, image=sun_img, anchor=NW, tags="sun")

# Character
stop = PhotoImage(file='frog_stop.png')
walk = PhotoImage(file='frog_walk.png')
walk2 = PhotoImage(file='frog_walk2.png')
jump = PhotoImage(file='frog_jump.png')
jump2 = PhotoImage(file='frog_jump2.png')

# Walls
wall = PhotoImage(file='wall.png')
x, y = 0, APP_HEIGHT - wall.height()
while x <= APP_WIDTH:
    canvas.create_image(x, y, image=wall, anchor=NW, tags="wall")
    x += wall.width()

# Player
player = canvas.create_image(200, 200, image=stop, anchor=NW)

# Enemy

# Feeds
flies = PhotoImage(file='flies.png')
canvas.create_image(200, 50, image=flies, anchor=NW, tags="feed")
canvas.create_image(100, 150, image=flies, anchor=NW, tags="feed")
canvas.create_image(500, 250, image=flies, anchor=NW, tags="feed")
canvas.create_image(700, 50, image=flies, anchor=NW, tags="feed")
canvas.create_image(500, 500, image=flies, anchor=NW, tags="feed")
canvas.create_image(900, 300, image=flies, anchor=NW, tags="feed")
canvas.create_image(300, 300, image=flies, anchor=NW, tags="feed")


window.resizable(False, False)
window.mainloop()