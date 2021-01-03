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
blue="#f3faff"

#background
canvas['bg']="#fbfbfb"
#shapes
canvas.create_rectangle(-10,-10,370,270,fill=blue,outline=blue)
canvas.create_rectangle(30,260,340,300,fill=blue,outline=blue)
#rounded edges
canvas.create_oval(2, 250, 52, 300, fill=blue,outline=blue)
canvas.create_oval(312, 250, 362, 300, fill=blue,outline=blue)
canvas.create_rectangle(100,36,260,206,fill="#388eb7",outline=blue) #canvas.create_rectangle(50, 0, 100, 50, fill='red')

#text
music_title = Label(window, text="MUSIC PLAYER", font=("Calibri", 14), background=blue)
music_title.place(x=121, y=3)
song_title = Label(window, text="SONG 1", font=("Calibri", 14), background=blue)
song_title.place(x=150, y=210)  

buttons = PhotoImage(file="Buttons.png")
label = Label(window, image=buttons, background=blue)
label.place(x=140, y=240)
############################################################################Gonna need to figue out pause button

#lines
for i in range (340,681,40):
    canvas.create_line(25,i,335,i,fill="#ececec")
    
window.mainloop()