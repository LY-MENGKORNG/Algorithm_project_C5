from tkinter import *
import random
import time
from pygame import mixer

window = Tk()
window.title("Frog eat Flies")
icon = PhotoImage(file='frog_icon.png')
window.iconphoto(False, icon)

# constance 
APP_WIDTH = window.winfo_screenwidth()
APP_HEIGHT = window.winfo_screenheight() - 70
X_VELOCITY, Y_VELOCITY = 6, 4
RUNNING = True
GRAVITY_FORCE = 9
JUMP_FORCE = 25
KEY_PRESSED = []
TIMED_LOOP = 30
SPEED = 7
RUNNING = True


# App center
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight() - 70
x = int((screen_width / 2) - (APP_WIDTH / 2))
y = int((screen_height / 2) - (APP_HEIGHT / 2))
window.geometry(f'{APP_WIDTH}x{APP_HEIGHT}+{x}+{y}')

# Frame
frame = Frame(window, width=APP_WIDTH, height=APP_HEIGHT)
frame.pack()

# Canvas
canvas = Canvas(frame,width=APP_WIDTH, height=APP_HEIGHT, bg="lightseagreen")
canvas.pack()

# Background image
bg_img = PhotoImage(file='background.png')
# canvas.create_image(0,0, image=bg_img, anchor=NW)

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
canvas.create_image(1000, 50, image=flies, anchor=NW, tags="feed1")
canvas.create_image(1100, 500, image=flies, anchor=NW, tags="feed2")
canvas.create_image(900, 300, image=flies, anchor=NW, tags="feed1")
canvas.create_image(1200, 700, image=flies, anchor=NW, tags="feed2")

# Walls and Obstacles
wall = PhotoImage(file='wall.png')
wall2 = PhotoImage(file='wall2.png')
obstacles = PhotoImage(file='obstacles.png')
x, y = 0, APP_HEIGHT - wall.height()
while x <= APP_WIDTH:
    if (x >= int(APP_WIDTH / 4) and x <= int(APP_WIDTH / 3)) or (x >= int(APP_WIDTH - 200) and x <= int(APP_WIDTH - 150)):
        canvas.create_image(x, y, image=obstacles, anchor=NW, tags= "kill")
        x += obstacles.width()
    else:
        canvas.create_image(x, y, image=wall, anchor=NW, tags="wall")
    x += wall.width()
canvas.create_image(250, 400, image=obstacles, anchor=NW, tags="kill")
x = 1200
while x < APP_WIDTH :
    canvas.create_image(x, 100, image=wall, tags="wall", anchor=NW)
    x += wall.width()

# Player
player = canvas.create_image(100, 100, image=stop, anchor=NW)

# Enemy
bee_left = PhotoImage(file='bee_left.png')
bee_right = PhotoImage(file='bee_right.png')
enemy = canvas.create_image(APP_WIDTH - 300, 100, image=bee_left, anchor=NW, tags="enemy")
enemy_width = bee_right.width()
enemy_height = bee_right.height()


# FUNCTION---------------------

# check if player and enemy overlap
def check_overlaping(x_direction=0, y_direction=0, ground=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("wall")
    if coord[0] + x_direction < 0 or coord[0] + x_direction > APP_WIDTH:
        return False
    if ground:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+ stop.width(), coord[1] + stop.height())
    else:
        overlap = canvas.find_overlapping(coord[0]+x_direction, coord[1]+y_direction, coord[0]+x_direction, coord[1]+y_direction)
    for platform in platforms:
        if platform in overlap:
            return False
    return True

# underground's gravity on player
def gravity():
    if check_overlaping(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
        window.after(TIMED_LOOP, gravity)
gravity()

# movement of enemy
def enemy_move():
    global X_VELOCITY, Y_VELOCITY
    enemy_coord = canvas.coords(enemy)
    if (enemy_coord[0] <= 30) or (enemy_coord[0] + enemy_width >= APP_WIDTH - 30):
        X_VELOCITY = -X_VELOCITY
    elif (enemy_coord[1] <= 30) or (enemy_coord[1] + enemy_height >= APP_HEIGHT - 30):
        Y_VELOCITY = -Y_VELOCITY
    canvas.move(enemy, X_VELOCITY, Y_VELOCITY)
    window.after(TIMED_LOOP, enemy_move)
enemy_move()

def move_player(x, y):
    pass

def check_direction(direction):
    pass
def player_jump():
    pass

def change_score():
    pass

def play_sound():
    pass

def check_winner():
    pass

def new_game():
    pass

def start_move(event):
    if event.keysym not in KEY_PRESSED:
        KEY_PRESSED.append(event.keysym)
        if len(KEY_PRESSED) == 1:
            check_direction(event.keysym)
        
def stop_move(event):
    global KEY_PRESSED
    print(event.keysym)
    if event.keysym in KEY_PRESSED:
        KEY_PRESSED.remove(event.keysym)


window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.resizable(False, False)
window.mainloop()

