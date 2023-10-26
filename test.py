<<<<<<< HEAD
<<<<<<< HEAD
from tkinter import*
=======
<<<<<<< HEAD
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

=======
from tkinter import *
import random
>>>>>>> d368dc20a8f3feff36f645d76b851c5b7f247dc8
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

<<<<<<< HEAD
=======
# Character
stop = PhotoImage(file='frog_stop.png')
stop2 = PhotoImage(file='frog_stop2.png')
walk = PhotoImage(file='frog_walk.png')
walk2 = PhotoImage(file='frog_walk2.png')
jump = PhotoImage(file='frog_jump.png')
jump2 = PhotoImage(file='frog_jump2.png')
jum_left = PhotoImage(file='frog_jump_left.png')
jum_left2 = PhotoImage(file='frog_jump_left2.png')
=======
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
>>>>>>> feature-1

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

<<<<<<< HEAD
def stop_move(event):
    global KEY_PRESSED
    if event.keysym in KEY_PRESSED:
        KEY_PRESSED.remove(event.keysym)


# Check position of enemy
def check_enemymove(enemy):
    player_coords = canvas.coords(player)
    enemy_overlap = canvas.find_overlapping(enemy[0], enemy[1], enemy[0]+bee_left.width(), enemy[1]+bee_left.height())
    stop_overlap = canvas.find_overlapping(player_coords[0], player_coords[1], player_coords[0]+stop.width(), player_coords[1]+stop.height())
    for overlap in enemy_overlap:
        if overlap in stop_overlap:
            return False
    return True

# Enemy move Function ------------------------
def enemy_move():
    global X_VELOCITY, Y_VELOCITY
    enemy_coord = canvas.coords(enemy)
    if(enemy_coord[0] < 50 or enemy_coord[0] + bee_left.width() + 50 > APP_WIDTH):
        if X_VELOCITY > 0:
            canvas.itemconfig(enemy, image=bee_left)
        else:
            canvas.itemconfig(enemy, image=bee_right)
        X_VELOCITY = -X_VELOCITY
    elif(enemy_coord[1] < 50 or enemy_coord[1] + bee_left.height() + 50 > APP_HEIGHT):
        Y_VELOCITY = -Y_VELOCITY
    if check_enemymove(enemy_coord):
        canvas.move(enemy, X_VELOCITY, Y_VELOCITY)
        canvas.after(10, enemy_move)
    else:
        game_over()

def move_feed():
    canvas.move("feed1", 0, -Y_VELOCITY)
    canvas.move("feed2", 0, Y_VELOCITY)
    canvas.after(30, move_feed)

def over_sound():
    mixer.init() #Initialzing pyamge mixer
    mixer.music.load('lie.mp3') #Loading Music File
    mixer.music.play() #Playing Music with Pygame
    time.sleep(4)
    mixer.music.stop()


def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(10, gravity)

def game_over():
    canvas.delete(ALL)
    over_sound()
    label = Label(frame, text="GAME OVER!", font=("BLOMBERG", 70, "bold"), fg="red", bg="lightseagreen")
    label.place(x=APP_WIDTH / 3, y=APP_HEIGHT / 3)
    restart_btn = Button(frame, text="RESTART GAME")
    restart_btn.place(x=APP_WIDTH / 2, y=APP_HEIGHT / 2)

gravity()
enemy_move()
move_feed()

window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.resizable(False, False)
>>>>>>> 1c62e4ea8c24fe6c742812e40871f5e9eafd5bf6
>>>>>>> d368dc20a8f3feff36f645d76b851c5b7f247dc8
window.mainloop()
=======
window.mainloop()
>>>>>>> feature-1
