from tkinter import *
import random
import time
from pygame import mixer

window = Tk()
window.title("Frog catch Flies")
icon = PhotoImage(file='frog_icon.png')
window.iconphoto(False, icon)

# constance 
APP_WIDTH = window.winfo_screenwidth()
APP_HEIGHT = window.winfo_screenheight() - 70
X_VELOCITY, Y_VELOCITY = 6, 5
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
obstacles = PhotoImage(file='obstacles.png')
x, y = 0, APP_HEIGHT - wall.height()
while x <= APP_WIDTH:
    if x >= int(APP_WIDTH / 4) and x <= int(APP_WIDTH / 3):
        canvas.create_image(x, y, image=obstacles, anchor=NW, tags= "obstacles")
        x += obstacles.width()
    else:
        canvas.create_image(x, y, image=wall, anchor=NW, tags="wall")
        x += wall.width()
x = 0

# Player
player = canvas.create_image(200, 200, image=stop, anchor=NW)

# Enemy
bee_left = PhotoImage(file='bee_left.png')
bee_right = PhotoImage(file='bee_right.png')
enemy = canvas.create_image(APP_WIDTH - 300, 100, image=bee_left, anchor=NW, tags="enemy")

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
        enemy_touch()
        if X_VELOCITY > 0:
            canvas.itemconfig(enemy, image=bee_left)
        else:
            canvas.itemconfig(enemy, image=bee_right)
        X_VELOCITY = -X_VELOCITY
    elif(enemy_coord[1] < 50 or enemy_coord[1] + bee_left.height() + 50 > APP_HEIGHT):
        enemy_touch()
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

# Gravity Function-------------------
def gravity():
    player_coords = canvas.coords(player)
    overlap = canvas.find_overlapping(player_coords[0], player_coords[1], player_coords[0]+stop.width(), player_coords[1]+stop.height())
    platforms = canvas.find_withtag("wall")
    for platform in platforms:
        if platform in overlap:
            canvas.itemconfig(player, image=stop)
            return
    canvas.move(player, 0, 9)
    window.after(20, gravity)

# Movement Function
def move_left(event):
    canvas.move(player, -12, 0)
    canvas.itemconfig(player, image=stop2)
def move_right(event):
    canvas.move(player, 12, 0)
    canvas.itemconfig(player, image=stop)
    
def jump_player(event):
    for i in range(10):
        canvas.move(player, 0, -12)
        canvas.itemconfig(player, image=jump)
        canvas.itemconfig(player, image=jump2)
        window.update()
        time.sleep(0.01)
    gravity()

def over_sound():
    mixer.init() #Initialzing pyamge mixer
    mixer.music.load('lie.mp3') #Loading Music File
    mixer.music.play() #Playing Music with Pygame
    time.sleep(4)
    mixer.music.stop()

def enemy_touch():
    mixer.init() #Initialzing pyamge mixer
    mixer.music.load('touch.mp3') #Loading Music File
    mixer.music.play() #Playing Music with Pygame
    time.sleep(0.01)
    # mixer.music.stop()

def game_over():
    canvas.delete(ALL)
    label = Label(window, text="GAME OVER!", font=("Arial", 70, "bold"), fg="red", bg="lightseagreen")
    label.place(y=APP_HEIGHT / 3, x=APP_HEIGHT / 2)
    over_sound()

gravity()
enemy_move()
move_feed()


window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
window.bind("<space>", jump_player)

window.resizable(False, False)
window.mainloop()