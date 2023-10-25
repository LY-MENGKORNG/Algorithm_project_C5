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

# Feeds
flies = PhotoImage(file='flies.png')
canvas.create_image(200, 50, image=flies, anchor=NW, tags="feed1")
canvas.create_image(100, 150, image=flies, anchor=NW, tags="feed2")
canvas.create_image(500, 250, image=flies, anchor=NW, tags="feed2")
canvas.create_image(700, 50, image=flies, anchor=NW, tags="feed1")
canvas.create_image(500, 500, image=flies, anchor=NW, tags="feed2")
canvas.create_image(900, 300, image=flies, anchor=NW, tags="feed1")
canvas.create_image(300, 300, image=flies, anchor=NW, tags="feed2")

# Walls and Obstacles
wall = PhotoImage(file='wall.png')
wall2 = PhotoImage(file='wall2.png')
obstacles = PhotoImage(file='obstacles.png')
x, y = 0, APP_HEIGHT - wall.height()
while x <= APP_WIDTH:
    if x >= int(APP_WIDTH / 4) and x <= int(APP_WIDTH / 3):
        canvas.create_image(x, y, image=obstacles, anchor=NW, tags= "enemy")
        x += obstacles.width()
    else:
        canvas.create_image(x, y, image=wall, anchor=NW, tags="wall")
        x += wall.width()
x, y = 0, 100
for i in range(5):
    canvas.create_image(x+700, y, image=wall2, anchor=NW, tags="wall")
    x += wall2.width()
x, y = 0, 100
canvas.create_image(x+300, y+100, image=obstacles, anchor=NW, tags="enemy")

# Player
player = canvas.create_image(200, 200, image=stop, anchor=NW)

# Enemy
bee_left = PhotoImage(file='bee_left.png')
bee_right = PhotoImage(file='bee_right.png')
enemy = canvas.create_image(APP_WIDTH - 300, 100, image=bee_left, anchor=NW, tags="enemy")


# Check movement--------------------
def check_movement(direction_x=0, direction_y=0, checkGround=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("wall")
    if coord[0] + direction_x < 0 or coord[0] + direction_x > APP_WIDTH:
        return False

    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+ direction_x, coord[1] + direction_y)
    else:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+stop.width(),coord[1] + stop.height())

    for platform in platforms:
        if platform in overlap:
            return False
    return True

def player_jum(force):
    if force > 0:
        if not check_movement(0, -force):
            # if remember == "Left":
            #     canvas.itemconfig(player, image=jum_left)
            # elif remember == "Right":
            #     canvas.itemconfig(player, image=jump)
            canvas.move(player, 0, -force)
            window.after(5, player_jum, force-1)
    else:
        canvas.itemconfig(player, image=jump2)

def move():
    if KEY_PRESSED != []:
        x = 0
        if KEY_PRESSED[0] != "space":
            remember = KEY_PRESSED[0]
        if "Left" in KEY_PRESSED:
            x -= SPEED
            canvas.itemconfig(player, image=stop2)
        elif "Right" in KEY_PRESSED:
            x += SPEED
            canvas.itemconfig(player, image=stop)
        if "space" in KEY_PRESSED and not check_movement(0, GRAVITY_FORCE, True):
            player_jum(30)
        if check_movement(x):
            canvas.move(player, x, 0)
            window.after(10, move)

def start_move(event):
    if event.keysym not in KEY_PRESSED:
        KEY_PRESSED.append(event.keysym)
        if len(KEY_PRESSED) == 1:
            move()

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