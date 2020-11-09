#import tkinter and rotatescreen
from tkinter import *
import rotatescreen

def screenRotation(temp):
    screen = rotatescreen.get_primary_display()
    if temp == "up":
        screen.set_landscape()
    elif temp == "down":
        screen.set_landscape_flipped()
    elif temp == "right":
        screen.set_portrait_flipped()
    elif temp == "left":
        screen.set_portrait()
        
master  = Tk()
master.geometry("100x100")
master.title("Screen Rotation")
master.configure(bg = "light grey")

result = StringVar()

Button(master, text="Up", command= lambda:screenRotation("up"), bg="white").grid(row=0,column = 3)
Button(master, text="Right", command= lambda:screenRotation("right"), bg="white").grid(row=1,column = 6)
Button(master, text="Left", command= lambda:screenRotation("left"), bg="white").grid(row=1,column = 2)
Button(master, text="Down", command= lambda:screenRotation("down"), bg="white").grid(row=3,column = 3)

mainloop()