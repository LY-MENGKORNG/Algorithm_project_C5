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
X_VELOCITY, Y_VELOCITY = 7, 5
RUNNING = True
GRAVITY_FORCE = 9
JUMP_FORCE = 25
KEY_PRESSED = []
TIMED_LOOP = 15
SPEED = 6
RUNNING = False
POSITION_CONFIG = [100, -100, 200, -200]


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
bg_level = PhotoImage(file='bg_level.png')
st_bg = PhotoImage(file='start_bg.png')
level2_bg = PhotoImage(file='background3.png')

# enemy house
house = PhotoImage(file='bee_house.png')

# Player score
score = 0

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

# Level 2 player
frog2 = PhotoImage(file='frog2.png')

# Feeds
flies = PhotoImage(file='flies.png')

# Feed  for game 2
flies2 = PhotoImage(file='flies2.png')

# Walls,Obstacles, recall and ground
wall = PhotoImage(file='wall.png')
wall2 = PhotoImage(file='wall2.png')
wall3 = PhotoImage(file='wall3.png')
stone = PhotoImage(file='stone.png')
ground = PhotoImage(file='ground.png')
obstacles = PhotoImage(file='obstacles.png')
recall = PhotoImage(file='recall.png')

# Player


# Enemy
bee_left = PhotoImage(file='bee_left.png')
bee_right = PhotoImage(file='bee_right.png')
bee2_left = PhotoImage(file='bee2_left.png')
enemy_width = bee_right.width()
enemy_height = bee_right.height()

# FUNCTION-----------------------------------------------------
# Delete interface

# Level button
btn_1 = PhotoImage(file='Button1.png')
btn_2 = PhotoImage(file='Button2.png')
btn_3 = PhotoImage(file='Button3.png')

# Game start 
button_img = PhotoImage(file='Button.png')
cancel_btn = PhotoImage(file='cancel_btn.png')
restart_btn = PhotoImage(file='restart_btn.png')
back_btn = PhotoImage(file='back_btn.png')
next_btn = PhotoImage(file='next_btn.png')

def back_start():
    # canvas.create_image(50, 50, image=)
    pass

def quit_game(event):
    window.destroy()

# LEVEL 1
def level1(event):
    canvas.delete(ALL)
    canvas.create_image(0,0, image=bg_img, anchor=NW, tags="first_bg")
    canvas.create_text(150, 30, text="Score: " + str(score),font=('Arial 25 bold'), fill="black", tags="player_score")

    # Enemy
    canvas.create_image(APP_WIDTH - 300, 100, image=bee_left, anchor=NW, tags="enemy")

    # Player
    canvas.create_image(100, 100, image=stop, anchor=NW, tags="player")

    # Back to see the level
    canvas.create_image(5,5, image=back_btn, anchor=NW, tags="back_btn")

    # wall, obstacle and flies
    x, y = 0, APP_HEIGHT - wall.height()
    while x <= APP_WIDTH:
        if (x >= int(APP_WIDTH / 4) and x <= int(APP_WIDTH / 3)-100) or (x >= int(APP_WIDTH - 200) and x <= int(APP_WIDTH - 150)):
            canvas.create_image(x, y, image=obstacles, anchor=NW, tags= "kill")
            x += obstacles.width()
        else:
            canvas.create_image(x, y, image=wall2, anchor=NW, tags="wall")
        x += wall2.width()
    canvas.create_image(200, 100, image=obstacles, anchor=NW, tags="kill")
    canvas.create_image(800, 500, image=obstacles, anchor=NW, tags="kill")
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
            canvas.create_image(x, 300, image=obstacles, tags="kill", anchor=NW)
            canvas.create_image(x - 45, 15, image=recall, tags="recall", anchor=NW)
        x += wall.width()

    # bee house 
    canvas.create_image(0, 0, image=house, anchor=NW)

    # flies
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

    # Back to level
    canvas.create_image(5,5, image=back_btn, anchor=NW, tags="back_btn")
    canvas.tag_bind("back_btn", "<Button-1>", level)

    # Process game
    gravity()
    enemy_move(7, 5)
    feed_move()

# LEVEL 1
def level2(event):
    canvas.delete(ALL)
    canvas.create_image(0,0, image=level2_bg, anchor=NW, tags="background1")
    canvas.create_image(200, 200, image=flies2, anchor=NW, tags="feed3")
    canvas.create_image(400, 200, image=flies2, anchor=NW, tags="feed4")
    canvas.create_image(700, 100, image=flies2, anchor=NW, tags="feed3")
    canvas.create_image(900, 600, image=flies2, anchor=NW, tags="feed4")
    canvas.create_image(100, 100, image=flies2, anchor=NW, tags="feed5")
    canvas.create_image(600, 600, image=flies2, anchor=NW, tags="feed4")
    canvas.create_image(5,5, image=back_btn, anchor=NW, tags="back_btn")

    # Walls and stones
    canvas.create_image(0, APP_HEIGHT - ground.height(), image=ground, anchor=NW, tags="wall")
    canvas.create_image(50, 400, image=stone, anchor=NW, tags="wall")
    canvas.create_image(300, 200, image=stone, anchor=NW, tags="wall")
    canvas.create_image(500, 100, image=stone, anchor=NW, tags="wall")

    # Enemy
    canvas.create_image(APP_WIDTH - 200, 200, image=bee2_left, anchor=NW, tags="enemy")

    # Player
    canvas.create_image(50, 50, image=frog2, anchor=NW, tags="player")

    canvas.tag_bind("back_btn", "<Button-1>", level)

    # Processes
    gravity()
    feed_move()
    enemy_move(7, 5)

# LEVEL 3
def level3(event):
    canvas.delete(ALL)

# ALL LEVEL 
def level(event): # show all level
    canvas.delete(ALL)
    canvas.create_image(0,0, image=bg_level, anchor=NW, tags="bg_st")
    canvas.create_text(APP_WIDTH / 2, 150, text="Choose your levels", font=("Ink free",80, "bold"), fill="yellow", tags="bg_st")
    canvas.create_image(APP_WIDTH / 4, APP_HEIGHT / 2 - 50, image=btn_1, anchor=CENTER, tags="level1")
    canvas.create_image(APP_WIDTH / 2, APP_HEIGHT / 2 - 50, image=btn_2, anchor=CENTER, tags="level2")
    canvas.create_image(APP_WIDTH - (APP_WIDTH / 4), APP_HEIGHT / 2 - 50, image=btn_3, anchor=CENTER, tags="level3")

    canvas.tag_bind("level1", "<Button-1>", level1)
    canvas.tag_bind("level2", "<Button-1>", level2)
    # canvas.tag_bind("level3", "<Button-1>", level3)


def game_start():
    canvas.create_image(0,0, image=st_bg, anchor=NW, tags="bg_st")
    canvas.create_image(APP_WIDTH/2 - 120, APP_HEIGHT / 2-80, image=button_img, anchor=NW, tags="start_game")
    canvas.tag_bind("start_game","<Button-1>", level)
game_start()


# check if player and enemy overlap
def check_overlaping(x_direction=0, y_direction=0, ground=False):
    coord = canvas.coords("player")
    platforms = canvas.find_withtag("wall")
    feed_pfs1 = canvas.find_withtag("feed1")
    feed_pfs2 = canvas.find_withtag("feed2")
    overlap = canvas.find_overlapping(coord[0]+x_direction, coord[1]+y_direction, coord[0]+x_direction, coord[1]+y_direction)
    for plf1 in feed_pfs1:
        if plf1 in overlap:
            change_score(plf1)
            return
    for plf2 in feed_pfs2:
        if plf2 in overlap:
            change_score(plf2)
            return
    if coord[0] + x_direction < 0 or coord[0] + x_direction > APP_WIDTH:
        return False
    if ground:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+ stop.width(), coord[1] + stop.height())
    for platform in platforms:
        if platform in overlap:
            return False
    return True

# Player's jumping
def player_jump(force):
    if force > 0:
        if check_overlaping(0, -force):
            canvas.move("player", 0, -force)
            window.after(5, player_jump, force-1)

def move_player():
    if KEY_PRESSED != [] and checkgame_over() and checkgame_win():
        x = 0
        remember = KEY_PRESSED[0]
        if "Left" in KEY_PRESSED:
            x -= SPEED
            canvas.itemconfig("player", image=stop2)
        elif "Right" in KEY_PRESSED:
            x += SPEED
            canvas.itemconfig("player", image=stop)
        if "space" in KEY_PRESSED and not check_overlaping(0, GRAVITY_FORCE, True):
            jump_sound()
            player_jump(JUMP_FORCE)
            if remember == "Left":
                canvas.itemconfig("player", image=stop2)
            elif remember == "Right":
                canvas.itemconfig("player", image=stop)
        if check_overlaping(x):
            player_possx = int(canvas.coords("player")[0])
            if "Right" in KEY_PRESSED:
                if player_possx % 3 == 0:
                    canvas.itemconfig("player", image=stop)
                else:
                    canvas.itemconfig("player", image=walk)
            elif "Left" in KEY_PRESSED:
                if player_possx % 3 == 0:
                    canvas.itemconfig("player", image=stop2)
                else:
                    canvas.itemconfig("player", image=walk_left)

            canvas.move("player", x, 0)
            window.after(10, move_player)

def change_score(platform):
    global score
    score += 1
    canvas.delete(platform)
    eat_sound()
    canvas.itemconfig("player_score", text="score:" + str(score))

def eat_sound():
    mixer.init() 
    mixer.music.load('eat.mp3')
    mixer.music.play() 
def over_sound():
    mixer.init() 
    mixer.music.load('tf_nemesis.mp3') 
    mixer.music.play() 

def jump_sound():
    mixer.init() 
    mixer.music.load('touch.mp3') 
    mixer.music.play() 

def game_over():
    over_sound()
    canvas.delete(ALL)
    canvas.create_rectangle(0, 0, APP_WIDTH, APP_HEIGHT, fill="skyblue", outline="",tags="over")
    canvas.create_image(550, 100, image=cry, anchor=NW, tags="over")
    canvas.create_text(APP_WIDTH / 2, APP_HEIGHT / 2 + 30, text="YOU LOST!", font=("Ink free", 50, "bold"), fill="red",tags="over")
    score = 0
    canvas.create_text(APP_WIDTH / 2, APP_HEIGHT / 2 + 100, text="Your score: "+ str(score), font=("Ink free", 30, "bold"), fill="green",tags="over")
    canvas.create_image(APP_WIDTH / 2 - 300, APP_HEIGHT / 2 + 150, image=cancel_btn,anchor=NW,tags="cancel")
    canvas.create_image(APP_WIDTH / 2, APP_HEIGHT / 2 + 150, image=restart_btn,anchor=NW,tags="restart")
    canvas.tag_bind("cancel", "<Button-1>", level)
    canvas.tag_bind("restart", "<Button-1>", level1)
    return

def checkgame_over():
    coord = canvas.coords("player")
    kill_plf = canvas.find_withtag("kill")
    enemy_plfs = canvas.find_withtag("enemy")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+stop.width(), coord[1]+stop.height())
    for enemy_plf in enemy_plfs:
        if enemy_plf in overlap:
            game_over()
            return False
    for plf in kill_plf:
        if plf in overlap:
            return False
    return True

def game_win():
    canvas.create_rectangle(0,0,APP_WIDTH, APP_HEIGHT, fill="skyblue")
    canvas.create_text(APP_WIDTH / 2, APP_HEIGHT / 2, text="YOU WON!", font=("Ink free", 70, "bold"))
    canvas.create_text(APP_WIDTH / 2, APP_HEIGHT / 2 - 200, text="Now I know you, you're a Frog!", font=("consolas", 25))
    canvas.create_image(APP_WIDTH / 2, APP_HEIGHT / 2 + 100, image=next_btn, anchor=CENTER, tags="next")
    canvas.tag_bind("next", "<Button-1>", level)
    return

def checkgame_win():
    coord = canvas.coords("player")
    recall_plf = canvas.find_withtag("recall")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0], coord[1])
    for plf in recall_plf:
        if plf in overlap:
            canvas.after(1000, game_win)
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

# Feeds move
def feed_move():
    global Y_VELOCITY
    if checkgame_over():
        if canvas.coords("feed1")[1] <= 0 or canvas.coords("feed1")[1] >= APP_HEIGHT:
            Y_VELOCITY = -Y_VELOCITY
        canvas.move("feed1", 0, Y_VELOCITY)
        canvas.move("feed2", 0, -Y_VELOCITY)
        canvas.move("feed3", Y_VELOCITY, 0)
        canvas.move("feed4", -Y_VELOCITY, 0)
        canvas.after(TIMED_LOOP, feed_move)
    else:
        canvas.after(1000, game_over)

# underground's gravity on player
def gravity():
    if check_overlaping(0, GRAVITY_FORCE, True) and checkgame_over() and checkgame_win():
        canvas.move("player", 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

# movement of enemy
def enemy_move(X_VELOCITY, Y_VELOCITY):
    if checkgame_over() and checkgame_win():
        enemy_coord = canvas.coords("enemy")
        if (enemy_coord[0] <= 30) or (enemy_coord[0] + enemy_width >= APP_WIDTH - 30):
            X_VELOCITY = -X_VELOCITY
            if X_VELOCITY > 0:
                canvas.itemconfig("enemy", image=bee_right)
            else:
                canvas.itemconfig("enemy", image=bee_left)
        elif (enemy_coord[1] <= 30) or (enemy_coord[1] + enemy_height >= APP_HEIGHT - 30):
            Y_VELOCITY = -Y_VELOCITY
        canvas.move("enemy", X_VELOCITY, Y_VELOCITY)
        window.after(TIMED_LOOP, enemy_move, X_VELOCITY, Y_VELOCITY)

window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.resizable(False, False)
window.mainloop()