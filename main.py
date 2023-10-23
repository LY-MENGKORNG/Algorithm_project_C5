from tkinter import *
import random
import time
from pygame import mixer

# Window
window = Tk()
window.title("Frog eat Flies")
icon = PhotoImage(file='frog_icon.png')
window.iconphoto(False, icon)

# constance 
APP_WIDTH = window.winfo_screenwidth()
APP_HEIGHT = window.winfo_screenheight() - 70
X_VELOCITY, Y_VELOCITY = 9, 7
RUNNING = True
GRAVITY_FORCE = 9
JUMP_FORCE = 25
KEY_PRESSED = []
TIMED_LOOP = 15
SPEED = 7
RUNNING = False

# App center
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight() - 70
x_axis = int((screen_width / 2) - (APP_WIDTH / 2))
y_axis = int((screen_height / 2) - (APP_HEIGHT / 2))
window.geometry(f'{APP_WIDTH}x{APP_HEIGHT}+{x_axis}+{y_axis}')

# Frame
frame = Frame(window, width=APP_WIDTH, height=APP_HEIGHT)
frame.pack()

# Canvas
canvas = Canvas(frame,width=APP_WIDTH, height=APP_HEIGHT)
canvas.pack()

# Background image
bg_img = PhotoImage(file='background2.png')
canvas.create_image(0,0, image=bg_img, anchor=NW)

# enemy house
house = PhotoImage(file='bee_house.png')
canvas.create_image(0, 0, image=house, anchor=NW)

# Player score
score = 0
player_score = canvas.create_text(100, 50, text="Score: " + str(score),
                                            font=('Arial 25 bold'), 
                                            fill="red")

# Character
stop = PhotoImage(file='frog_stop.png')
stop2 = PhotoImage(file='frog_stop2.png')
walk = PhotoImage(file='frog_walk.png')
walk2 = PhotoImage(file='frog_walk2.png')
walk_left = PhotoImage(file='frog_walk_left.png')
jump = PhotoImage(file='frog_jump.png')
jump2 = PhotoImage(file='frog_jump2.png')
jum_left = PhotoImage(file='frog_jump_left.png')
jum_left2 = PhotoImage(file='frog_jump_left2.png')
cry = PhotoImage(file='frog_cry.png')

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

# Walls,Obstacles and recall
wall = PhotoImage(file='wall.png')
wall2 = PhotoImage(file='wall2.png')
obstacles = PhotoImage(file='obstacles.png')
recall = PhotoImage(file='recall.png')
x, y = 0, APP_HEIGHT - wall.height()
while x <= APP_WIDTH:
    if (x >= int(APP_WIDTH / 4) and x <= int(APP_WIDTH / 3)-100) or (x >= int(APP_WIDTH - 200) and x <= int(APP_WIDTH - 150)):
        canvas.create_image(x, y, image=obstacles, anchor=NW, tags= "kill")
        x += obstacles.width()
    else:
        canvas.create_image(x, y, image=wall2, anchor=NW, tags="wall")
    x += wall.width()
canvas.create_image(250, 400, image=obstacles, anchor=NW, tags="kill")

x = 100
while x < APP_WIDTH :
    if x < 200:
        canvas.create_image(x, 500, image=wall, tags="wall", anchor=NW)
        canvas.create_image(x+400, 500, image=wall, tags="wall", anchor=NW)
    if x > 200 and x < 400:
        canvas.create_image(x, 400, image=wall, tags="wall", anchor=NW)
        canvas.create_image(x+400, 400, image=wall, tags="wall", anchor=NW)
    if x > 400 and x < 450:
        canvas.create_image(x, 300, image=obstacles, tags="kill", anchor=NW)
        canvas.create_image(x + 400, 400, image=obstacles, tags="kill", anchor=NW)
    if x > 550 and x < 600:
        canvas.create_image(x, 600, image=obstacles, tags="kill", anchor=NW)
        canvas.create_image(x + 500, 350, image=wall, tags="wall", anchor=NW)
    if x > 800 and x < 950:
        canvas.create_image(x, 200, image=wall, tags="wall", anchor=NW)
    if x > 1050 and x < 1100:
        canvas.create_image(x, 600, image=obstacles, tags="kill", anchor=NW)
    if x > 1150 and x < 1200:
        canvas.create_image(x, 100, image=wall, tags="wall", anchor=NW)
        canvas.create_image(x, 300, image=obstacles, tags="kill", anchor=NW)
        canvas.create_image(x - 80, -60, image=recall, tags="recall", anchor=NW)
    x += wall.width()

# Player
player = canvas.create_image(100, 100, image=stop, anchor=NW)

# Enemy
bee_left = PhotoImage(file='bee_left.png')
bee_right = PhotoImage(file='bee_right.png')
enemy = canvas.create_image(APP_WIDTH - 300, 100, image=bee_left, anchor=NW, tags="enemy")
enemy_width = bee_right.width()
enemy_height = bee_right.height()

# FUNCTION-----------------------------------------------------

def delete_interface(event):
    canvas.delete("bg_st")
    canvas.delete("start_game")
    level()

def level():
    gravity()
    enemy_move()
    feed_move()

# Game start 
st_bg = PhotoImage(file='start_bg.png')
button_img = PhotoImage(file='Button.png')
canvas.create_image(0,0, image=st_bg, anchor=NW, tags="bg_st")
canvas.create_image(APP_WIDTH/2 - 120, APP_HEIGHT / 2-80, image=button_img, anchor=NW, tags="start_game")
canvas.tag_bind("start_game","<Button-1>", delete_interface)

# check if player and enemy overlap
def check_overlaping(x_direction=0, y_direction=0, ground=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("wall")
    feed_pfs1 = canvas.find_withtag("feed1")
    feed_pfs2 = canvas.find_withtag("feed2")
    overlap = canvas.find_overlapping(coord[0]+x_direction, coord[1]+y_direction, coord[0]+x_direction, coord[1]+y_direction)
    for plf1 in feed_pfs1:
        if plf1 in overlap:
            change_score(plf1)
    for plf2 in feed_pfs2:
        if plf2 in overlap:
            change_score(plf2)
    if coord[0] + x_direction < 0 or coord[0] + x_direction > APP_WIDTH:
        return False
    if ground:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+ stop.width(), coord[1] + stop.height())
    for platform in platforms:
        if platform in overlap:
            return False
    return True

# underground's gravity on player
def gravity():
    if check_overlaping(0, GRAVITY_FORCE, True) and checkgame_over():
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

# movement of enemy
def enemy_move():
    global X_VELOCITY, Y_VELOCITY
    if checkgame_over():
        enemy_coord = canvas.coords(enemy)
        if (enemy_coord[0] <= 30) or (enemy_coord[0] + enemy_width >= APP_WIDTH - 30):
            X_VELOCITY = -X_VELOCITY
            if X_VELOCITY > 0:
                canvas.itemconfig(enemy, image=bee_right)
            else :
                canvas.itemconfig(enemy, image=bee_left)
        elif (enemy_coord[1] <= 30) or (enemy_coord[1] + enemy_height >= APP_HEIGHT - 30):
            Y_VELOCITY = -Y_VELOCITY
        canvas.move(enemy, X_VELOCITY, Y_VELOCITY)
        window.after(TIMED_LOOP, enemy_move)

def player_jump(force):
    if force > 0:
        if check_overlaping(0, -force):
            canvas.move(player, 0, -force)
            window.after(5, player_jump, force-1)

def move_player():
    if KEY_PRESSED != [] and checkgame_over():
        x = 0
        remember = KEY_PRESSED[0]
        if "Left" in KEY_PRESSED:
            x -= SPEED
            canvas.itemconfig(player, image=stop2)
        elif "Right" in KEY_PRESSED:
            x += SPEED
            canvas.itemconfig(player, image=stop)
        if "space" in KEY_PRESSED and not check_overlaping(0, GRAVITY_FORCE, True):
            jump_sound()
            player_jump(20)
            if remember == "Left":
                canvas.itemconfig(player, image=stop2)
            elif remember == "Right":
                canvas.itemconfig(player, image=stop)
        if check_overlaping(x):
            if int(canvas.coords(player)[0]) % 5 == 0 and "Right" in KEY_PRESSED:
                canvas.itemconfig(player, image=stop)
            elif int(canvas.coords(player)[0]) % 5 != 0 and "Right" in KEY_PRESSED:
                canvas.itemconfig(player, image=walk)
            elif int(canvas.coords(player)[0]) % 2 == 0 and "Left" in KEY_PRESSED:
                canvas.itemconfig(player, image=stop2)
            elif int(canvas.coords(player)[0] % 2 != 0 and "Left" in KEY_PRESSED):
                canvas.itemconfig(player, image=walk_left)
            canvas.move(player, x, 0)
            window.after(10, move_player)

def change_score(platform):
    global score
    score += 1
    canvas.delete(platform)
    eat_sound()
    canvas.itemconfig(player_score, text="score:" + str(score))

def eat_sound():
    mixer.init() #Initialzing pyamge mixer
    mixer.music.load('eat.mp3') #Loading Music File
    mixer.music.play() #Playing Music with Pygame
def over_sound():
    mixer.init() #Initialzing pyamge mixer
    mixer.music.load('lie.mp3') #Loading Music File
    mixer.music.play() #Playing Music with Pygame
    time.sleep(5)
    mixer.music.stop()

def jump_sound():
    mixer.init() #Initialzing pyamge mixer
    mixer.music.load('touch.mp3') #Loading Music File
    mixer.music.play() #Playing Music with Pygame

def game_over():
    canvas.create_rectangle(150, 50, APP_WIDTH-200, APP_HEIGHT-50, fill="skyblue", outline="")
    canvas.create_image(500, 100, image=cry, anchor=NW, tags="cry")
    canvas.create_text(APP_WIDTH  /2, 450, text="YOU LOST!", font=("Ink free 50, bold"), tags="cry")
    # canvas.create_image()
    over_sound()

def checkgame_over():
    coord = canvas.coords(player)
    kill_plf = canvas.find_withtag("kill")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+stop.width(), coord[1]+stop.height())
    print(overlap)
    for plf in kill_plf:
        if plf in overlap:
            return False
    return True
def start_move(event):
    if event.keysym not in KEY_PRESSED:
        KEY_PRESSED.append(event.keysym)
        if len(KEY_PRESSED) == 1:
            move_player()
        
def stop_move(event):
    global KEY_PRESSED
    if event.keysym in KEY_PRESSED:
        KEY_PRESSED.remove(event.keysym)

window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

# Feeds move
def feed_move():
    if checkgame_over():
        canvas.move("feed1", 0, Y_VELOCITY)
        canvas.move("feed2", 0, -Y_VELOCITY)
        canvas.after(TIMED_LOOP, feed_move)
    else :
        game_over()

window.resizable(False, False)
window.mainloop()