#imports tkinter, python's standard GUI
from tkinter import * 
import tkinter as tk 

#the main tkinter window
window = tk.Tk()
window.title("MusicPlayer")

#creating the gui background
canvas=tk.Canvas(master=window, width=360, height=120)
canvas.pack()

#the two main background colors
blue="#f3faff"
canvas['bg']="white"

#album cover placeholder
canvas.create_rectangle(0,0,120,120,fill="#388eb7",outline=blue)

#placing the song, album, and artists names onto the player
song_title = Label(window, text="Ballin", font=("Calibri", 20), background="white", bd=0)
song_title.place(x=125, y=1)

album_name = Label(window, text="Perfect 10", font=("Calibri", 12), fg = "#3f3f3f", background="white", bd =0)
album_name.place(x=125, y=30)

artist_name = Label(window, text="Mustard, Roddy Ricch", font=("Calibri", 12), fg = "#3f3f3f", background="white", bd =0)
artist_name.place(x=125, y=50)

#These are the commands for when the buttons are clicked (nothing is here yet)
def play_clicked():
    print("Play button has been clicked")
def skip_clicked():
    print("Skip button has been clicked")
def backskip_clicked():
    print("Backskip button has been clicked")
def shuffle_clicked():
    print("Shuffle button has been clicked")

#placing down the different buttons
backskipimage = PhotoImage(file="BackSkip.png")
backskip = Button(window, image=backskipimage, background="white", borderwidth=0, command=backskip_clicked)
backskip.place(x=125, y=80)

playimage = PhotoImage(file="Play.png")
play = Button(window, image=playimage, background="white", borderwidth=0, command=play_clicked)
play.place(x=175, y=80)

skipimage = PhotoImage(file="Skip.png")
skip = Button(window, image=skipimage, background="white", borderwidth=0, command=skip_clicked)
skip.place(x=225, y=80)

shuffleimage = PhotoImage(file="shuffle.png")
shuffle = Button(window, image=shuffleimage, background="white", borderwidth=0, command=shuffle_clicked)
shuffle.place(x=275, y=82)

window.mainloop()