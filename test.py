"""
#imports tkinter, python's standard GUI
from tkinter import * 
import tkinter as tk 

#the main tkinter window
window = tk.Tk()
window.title("MusicPlayer")

#creating the gui background
canvas=tk.Canvas(master=window, width=360, height=680)
canvas.pack()

#######################
color="green"
canvas.create_rectangle(-10,-10,370,270,fill=color)

def myclick():
    print("aaa")
    global color="blue"
    color="blue"

myButton = Button(canvas, text = "Click Me!",command=myclick)
myButton.place(x=100,y=200)



window.mainloop()
"""

