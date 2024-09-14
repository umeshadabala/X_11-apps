from tkinter import *
from tkinter import PhotoImage
import subprocess
import time
from PIL import Image, ImageTk
import platform
import os
# Initialize window
s = Tk()
s.title('X_11 GUI')
s.geometry('500x500')
s.resizable(0, 0)

# Load and set the background image
bg_image = Image.open("images/bg.jpg")
bg_image = bg_image.resize((500, 500))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(s, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Resize and load button images to fit well within 500x500 canvas
button_size = (80, 80)  # Define a standard size for buttons
calc_img = ImageTk.PhotoImage(Image.open("images/calc.png").resize(button_size))
paint_img = ImageTk.PhotoImage(Image.open("images/paint.png").resize(button_size))
browser_img = ImageTk.PhotoImage(Image.open("images/browser.png").resize(button_size))
todo_img = ImageTk.PhotoImage(Image.open("images/todo.png").resize(button_size))
XoX_img = ImageTk.PhotoImage(Image.open("images/game.png").resize(button_size))
snake_img = ImageTk.PhotoImage(Image.open("images/snake.png").resize(button_size))
notepad_img = ImageTk.PhotoImage(Image.open("images/notepad.png").resize(button_size))
ide_img = ImageTk.PhotoImage(Image.open("images/ide.png").resize(button_size))
file_img = ImageTk.PhotoImage(Image.open("images/file.png").resize(button_size))
cam_img = ImageTk.PhotoImage(Image.open("images/camera.png").resize(button_size))
player_img = ImageTk.PhotoImage(Image.open("images/player.png").resize(button_size))
sheets_img = ImageTk.PhotoImage(Image.open("images/sheets.png").resize(button_size))
sudoku_img = ImageTk.PhotoImage(Image.open("images/sudoku.png").resize(button_size))
info_img = ImageTk.PhotoImage(Image.open("images/info.png").resize(button_size))
shutdown_img = ImageTk.PhotoImage(Image.open("images/shutdown.png").resize(button_size))
restart_img = ImageTk.PhotoImage(Image.open("images/restart.png").resize(button_size))

# Functions to run apps
def calc():
    subprocess.run(['python3', 'scripts/calc.py'])
def col():
    subprocess.run(['python3', 'scripts/paint.py'])
def browser():
    subprocess.run(["python3", "scripts/browser.py"])
def notepad():
    subprocess.run(["python3", "scripts/notepad.py"])
def todo():
    subprocess.run(["python3", "scripts/todo.py"])
def snake():
    subprocess.run(["python3", "scripts/snake.py"])
def XoX():
    subprocess.run(["python3", "scripts/XoX.py"])
def ide():
    subprocess.run(["python3", "scripts/python.py"])
def file():
    subprocess.run(["python3", "scripts/files.py"])
def cam():
    subprocess.run(["python3", "scripts/camera.py"])
def player():
    subprocess.run(["python3", "scripts/media.py"])
def sheets():
    subprocess.run(["python3", "scripts/sheets.py"])
def sudoku():
    subprocess.run(["python3", "scripts/sudoku.py"])
def info():
    subprocess.run(["python3", "scripts/info.py"])


def shutdown():
    if platform.system() == "Windows":
        os.system('shutdown -s')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("shutdown -h now")
    else:
        print("Os not supported!")

def restart():
    if platform.system() == "Windows":
        os.system("shutdown -t 0 -r -f")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('reboot now')
    else:
        print("Os not supported!")

# Create a grid layout with 4 apps per row and 4 rows (to accommodate 13 buttons)
# Row and column positions for buttons
positions = [
    (0, 0), (1, 0), (2, 0), (3, 0),
    (0, 1), (1, 1), (2, 1), (3, 1),
    (0, 2), (1, 2), (2, 2), (3, 2),
    (0,3),  (1,3),  (2,3)]

# Button image references for easy access
buttons = [
    (calc_img, calc), (paint_img, col), (browser_img, browser), (todo_img, todo),
    (XoX_img, XoX), (snake_img, snake), (notepad_img, notepad), (ide_img, ide),
    (file_img, file), (cam_img, cam), (player_img, player), (sheets_img, sheets), (info_img, info), (shutdown_img, shutdown),
    (restart_img, restart)
]

# Placing the buttons in grid (4x4)
for index, (image, command) in enumerate(buttons):
    row, col = positions[index]
    Button(s, image=image, command=command).place(x=col * 120 + 10, y=row * 120 + 20)

# Display time
def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")

    my_label.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
    my_label.after(1000, clock)

# Add time label
my_label = Label(s, text="", font=("Helvetica", 15), fg="green", bg="black")
my_label.place(x=360, y=450)
clock()

# Keep references to images to prevent garbage collection
s.image_refs = [calc_img, paint_img, browser_img, todo_img, XoX_img, snake_img, notepad_img, ide_img, file_img, cam_img, player_img, sheets_img,info_img,shutdown_img,restart_img, bg_photo]

# Main loop
s.mainloop()
