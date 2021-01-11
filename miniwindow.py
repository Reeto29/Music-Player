#imports tkinter, python's standard GUI
from tkinter import *
import tkinter as tk

#imports the different modules required for playing music
from pygame import mixer
import os
import random
import time
path=r"C:\Users\REETO\Documents\GitHub\ICS3U_Summative\Songs"
mixer.init()
number=1
paused=False
shuffled=False

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

#this loads all the mp3 songs in the ICS3U Summative Folder into the player
def loading_songs(path):
    songs=[]
    for filename in os.listdir(path):
        if filename.endswith(".mp3"):
            songs.append(os.path.join(path,filename))
    return songs

#loads the songs in
songs=loading_songs(path)
song_number=0
random_song_number=0
mixer.music.load(songs[song_number])
volume=1

#These are the commands for when the buttons are clicked
def play_clicked():
    #recognizes paused as a global function
    global paused
    #plays the song

    if paused == True and shuffled == False:
        #unpauses music if it is paused
        #replaces the play button with a pause button
        mixer.music.unpause()
        play.place(x=1000,y=90000)
        paused=False

    else:
        mixer.music.play()
        paused=True
    pause.place(x=175, y=80)

def pause_clicked():
    global paused
    pause.place(x=1000,y=90000)
    play.place(x=175,y=80)
    mixer.music.pause()
    paused = True


def skip_clicked():
    global song_number
    global songs_random
    global paused
    global shuffled
    global random_song_number
    if (song_number + 1) != len(songs):
        paused=False
        song_number+=1
        random_song_number+=1

        if shuffled == False:
            mixer.music.load(songs[song_number])
        else:
            mixer.music.load(songs_random[random_song_number])

        play.place(x=9000,y=8000)
        pause.place(x=175,y=80)
        play_clicked()
   

def backskip_clicked():
    global song_number
    global paused
    global random_song_number
    if (song_number - 1) != -1:
        paused=False
        song_number-=1
        random_song_number-=1

        if shuffled == False:
            mixer.music.load(songs[song_number])
        else:
            mixer.music.load(songs_random[random_song_number])

        play.place(x=9000,y=8000)
        pause.place(x=175,y=80)
        play_clicked()

def shuffle_clicked():
    global shuffled
    global songs_random
    global song_number
    global random_song_number
    global paused
    songs_random=list.copy(songs)


   
    print(songs)
    print(songs_random)


    if shuffled == True:
        shuffled=False
        paused=False
        print("shuffle off")
        mixer.music.unload()
        mixer.music.load(songs[song_number])
        print(songs[song_number])
    else:
        shuffled=True
        paused=True
        random.shuffle(songs_random)
        print("shuffle on")
        mixer.music.unload()
        mixer.music.load(songs_random[random_song_number])
        print(songs_random[random_song_number])
    pause.place(x=1000,y=90000)
    play.place(x=175,y=80)

#placing down the different buttons
backskipimage = PhotoImage(file="BackSkip.png")
backskip = Button(window, image=backskipimage, background="white", borderwidth=0, command=backskip_clicked)
backskip.place(x=125, y=80)

playimage = PhotoImage(file="Play.png")
play = Button(window, image=playimage, background="white", borderwidth=0, command=play_clicked)
play.place(x=175, y=80)

pauseImage = PhotoImage(file="Pause.png")
pause = Button(window, image=pauseImage, background="white", borderwidth=0, command=pause_clicked)

skipimage = PhotoImage(file="Skip.png")
skip = Button(window, image=skipimage, background="white", borderwidth=0, command=skip_clicked)
skip.place(x=225, y=80)

shuffle_image = PhotoImage(file="shuffle.png")
shuffle = Button(window, image=shuffle_image, background="white", borderwidth=0, command=shuffle_clicked)
shuffle.place(x=275, y=82)

window.mainloop()