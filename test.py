from tkinter import *
import pygame
from pygame.locals import *

window = Tk()
window.title("Frog catch Flies")

# constance 
APP_WIDTH = 1000
APP_HEIGHT = 600

# App center
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (APP_WIDTH / 2))
y = int((screen_height / 2) - (APP_HEIGHT / 2))
window.geometry(f'{APP_WIDTH}x{APP_HEIGHT}+{x}+{y}')


# Quit program
button_quit = Button(window, text="Exit Program", command=window.quit)
button_quit.pack()


window.mainloop()