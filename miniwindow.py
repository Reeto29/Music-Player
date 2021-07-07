"""
Tanner Farkas & Reeto Ghosh
***
January 26th, 2021
***
Description: In our summative task, we developed an application interface to
             replicate an MP3 player. The program takes .mp3 files from the
             user's computer and adds them to the music player. The user will
             have access to a variety of features such as playing, pausing,
             skipping, backskipping, volume control and several other built in
             features!

             We hope you enjoy our game!
***
"""






#imports tkinter, python's standard GUI
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk

#imports the different modules required for playing music
from mutagen.mp3 import MP3
from pygame import mixer
import os
import random
import time

#This path goes straight to you song folder
#You will have to change this, as it is specific to your device

path=r"C:\Users\REETO\OneDrive\Documents\GitHub\ICS3U_Summative\Songs"
mixer.init()
paused=False
shuffled=False
volume=1
resized=False
converted_current_time=""
converted_total_length=""

#the main tkinter window
window = tk.Tk()
window.title("MusicPlayer")

canvas = Canvas(window, width=585, height=160)
canvas.place(x=0,y=0)

#creating the gui background
window.geometry("365x160")
canvas.create_rectangle(365,0,585,160,fill="white",outline="")

#the background
canvas['bg']="white"

#album cover placeholder
maxframes = 15

#List of all of the gif files
gif_list=["city_explosion.gif","cityscape.gif","gundam.gif","motorcycle.gif","porsche.gif","robot_man.gif"]
gif_index=0

#PhotoImage is mainly meant for images
#This means that for GIFS, one must render each frame
#This program renders each frame
frames = [PhotoImage(file=('gifs\\'+gif_list[gif_index]),format = 'gif -index %i' %(i)) for i in range(maxframes)]
def next_picture(frame_count):

    frame = frames[frame_count]
    frame_count += 1
    if frame_count == maxframes:
        frame_count = 0
    gif_image.configure(image=frame)
    window.after(100, next_picture, frame_count)

gif_image = Label(window,borderwidth=0)
gif_image.place(x=0,y=0)
window.after(0, next_picture, 0)

#This  Program loads all the mp3 songs in the ICS3U Summative Folder into the player
def loading_songs(path):
    songs=[]
    for filename in os.listdir(path):
        if filename.endswith(".mp3"):
            songs.append(os.path.join(path,filename))
        
    return songs
    
#Loads the songs in
songs=loading_songs(path)
song_number=0
random_song_number=0
mixer.music.load(songs[song_number])

#Grab Song Length
def play_time():
    #Grab current song time
    current_time = mixer.music.get_pos() / 1000

    #Temporary Label to get data
    slider_label.config(text=f'Slider: {int(song_progress_bar.get())} and Song Pos: {int(current_time)}') 

    #convert to time format
    global converted_current_time
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
    
    #Get CUrrently Playing Song
    if shuffled == False:
        current_song = os.path.splitext(songs[song_number])

    else:
        current_song = os.path.splitext(songs_random[random_song_number])
        
    # Get Song with Mutagen
    if shuffled == False:
        audio=MP3(songs[song_number])
    else:
        audio=MP3(songs_random[random_song_number])
    global total_length
    total_length = audio.info.length
    
    #Convert to Time format
    global converted_total_length
    converted_total_length = time.strftime('%M:%S', time.gmtime(total_length))
   
    #Output time to status bar
    def song():
        status_bar.config(text=f'Time Elapsed: {converted_current_time} of  {converted_total_length}')
        song_progress.config(text=f'{converted_current_time} of  {converted_total_length}')
        song_length.config(text=converted_total_length)
        #updating slider position to proper position in song
        song_progress_bar.config(value=int(current_time))
    song()
    
    

       #updates time
    status_bar.after(1000, play_time)
    
#placing the song, album, and artists names onto the player
def text():
    global song_title
    global title_album_name
    try:
        if shuffled == False:
            #Cuts the string out from the last instance of a "\\" up to the .mp3 file extension
            title_album_name=(songs[song_number])[((songs[song_number]).rindex('\\')+1):-4]
        else:
            #Cuts the string out from the last instance of a "\\" up to the .mp3 file extension
            title_album_name=(songs_random[random_song_number])[((songs_random[random_song_number]).rindex('\\')+1):-4]

        space_count=(19-(len(title_album_name[(title_album_name.index("_")+1):title_album_name.rindex("_")])))

        #Music File Layout Goes: ArtistName_SongTitle_AlbumName
        #Cuts the string out from the first underscore to the second underscore
        song_title = Label(window, text=(title_album_name[(title_album_name.index("_")+1):title_album_name.rindex("_")]+(" "*space_count)), font=("Calibri", 18), background="white", bd=0) #length 20
        song_title.place(x=125, y=1)

        #Cuts the string out from the last underscore to the end of the string
        album_name = Label(window, text=(title_album_name[title_album_name.rindex("_")+1:]+" "*30), font=("Calibri", 12), fg = "#3f3f3f", background="white", bd =0)
        album_name.place(x=125, y=30)

        #Cuts the string out from the beggining og the string to the first underscore
        artist_name = Label(window, text=(title_album_name[0:title_album_name.index("_")]+" "*30), font=("Calibri", 12), fg = "#3f3f3f", background="white", bd =0)
        artist_name.place(x=125, y=50)

    except ValueError:

        #In case music file layout is not followed, this program will write state it as 'unknown'
        song_title = Label(window, text=("Unknown Song" + " "*40), font=("Calibri", 18), background="white", bd=0)
        song_title.place(x=125, y=1)

        album_name = Label(window, text=("Unknown Album" + " "*40), font=("Calibri", 12), fg = "#3f3f3f", background="white", bd =0)
        album_name.place(x=125, y=30)

        artist_name = Label(window, text=("Unknown Artist" + " "*40), font=("Calibri", 12), fg = "#3f3f3f", background="white", bd =0)
        artist_name.place(x=125, y=50)

def set_vol(val):
    #casting value so that it can be detected as a value from 0-1 for the mixer
    volume = int(val)/100
    #setting the volume  
    mixer.music.set_volume(volume)

#These are the commands for when the buttons are clicked

#This outputs the queue onto the screen
def queue_list():
    global shuffled
    global songs_random
    song_shortened_list=[]

    if shuffled==True:
        for i in range(len(songs_random)):
            canvas.create_line(365,i*30,545,i*30)
            song_shortened_list.append(((songs_random)[i])[((songs_random[i]).rindex('\\')+1):-4])
            song_shortened_list=(','.join(song_shortened_list))
            song_shortened_list=song_shortened_list.replace("_"," ")
            album_name = Label(window, text=(f"{song_shortened_list+(' '*19)}"), font=("Calibri", 9), fg = "#3f3f3f", background="white", bd =0)   
            album_name.place(x=365, y=((i+0.25)*30))
            song_shortened_list=[]
            canvas.create_line(365,i*30,545,i*30)
    else:
        for i in range(len(songs)):
            canvas.create_line(365,i*30,545,i*30)

            song_shortened_list.append(((songs)[i])[((songs[i]).rindex('\\')+1):-4])
            song_shortened_list=(','.join(song_shortened_list))
            song_shortened_list=song_shortened_list.replace("_"," ")
            album_name = Label(window, text=(f"{song_shortened_list+(' '*19)}"), font=("Calibri", 9), fg = "#3f3f3f", background="white", bd =0)   
            album_name.place(x=365, y=((i+0.25)*30))
            song_shortened_list=[]
    canvas.create_line(365,150,545,150)

def skip_clicked():
    global song_number
    global songs_random
    global paused
    global shuffled
    global random_song_number
    global gif_index
    global frames

    #Skips the songs
    #If statement ensures that it doesn't skip out of range
    if (song_number + 1) != len(songs):
        paused=False
        #Adds one to the variable so that it goes 1 over in the song queue
        song_number+=1
        gif_index+=1


        #If the shuffle is on, it will follow the randomized shuffle queue
        if shuffled == False:
            mixer.music.load(songs[song_number])
        else:
            random_song_number+=1
            mixer.music.load(songs_random[random_song_number])

        #switches out the buttons
        frames = [PhotoImage(file=('gifs\\'+gif_list[gif_index]),format = 'gif -index %i' %(i)) for i in range(maxframes)]

        play.place(x=9000,y=8000)
        pause.place(x=175,y=80)
        play_clicked()
        text()


def backskip_clicked():
    global song_number
    global paused
    global random_song_number
    global gif_index
    global frames


    if (song_number - 1) != -1:
        paused=False
        #Adds one to the variable so that it goes 1 over in the song queue
        song_number-=1
        gif_index-=1

        #If the shuffle is on, it will follow the randomized shuffle queue
        if shuffled == False:
            mixer.music.load(songs[song_number])
        else:
            random_song_number-=1
            mixer.music.load(songs_random[random_song_number])
        
        frames = [PhotoImage(file=('gifs\\'+gif_list[gif_index]),format = 'gif -index %i' %(i)) for i in range(maxframes)]

        #switches out the buttons
        play.place(x=9000,y=8000)
        pause.place(x=175,y=80)
        play_clicked()
        text()

def play_clicked():
    global converted_current_time
    global converted_total_length
    
    #recognizes paused as a global function
    global paused
    #plays the song
    
    if paused == True and shuffled == False or paused == True and shuffled == True:
        #unpauses music if it is paused
        #replaces the play button with a pause button
        mixer.music.unpause()
        play.place(x=1000,y=90000)
        
        paused=False
        
        mixer.music.play
    else:
        #plays the music if it was previously paused
        mixer.music.play()
        
        paused=True

    if converted_current_time == converted_total_length:
        song_progress_bar.config(value=0)

        
    text()
    
    pause.place(x=175, y=80)
    #calling the play_time function to get the song length
    play_time()
    #update slider to proper position
    slider_position = int(total_length)
    song_progress_bar.config(to=slider_position, value=0)
   
def pause_clicked():
    #pauses the music and replaces the pause button with the play
    global paused
    pause.place(x=1000,y=90000)
    play.place(x=175,y=80)
    mixer.music.pause()
    paused = True




def shuffle_clicked():
    song_progress_bar.config(value=0)
    global shuffled
    global songs_random
    global song_number
    global random_song_number
    global paused
    #makes a copy of the song queue
    songs_random=list.copy(songs)
        
    #randomizes the song queue
    if shuffled == True:
        play_time()
        shuffled=False
        paused=False
        mixer.music.unload()
       
        mixer.music.load(songs[song_number])
    else:
        play_time()
        shuffled=True
        paused=True
        random.shuffle(songs_random)
        mixer.music.unload()
        mixer.music.load(songs_random[random_song_number])
    text()
    queue_list()
    play_time()
    
    skip_clicked()
    backskip_clicked()

    

def slide(x):
    
    slider_label.config(text=f'{int(song_progress_bar.get())} of {int(total_length)}')
    songs=loading_songs(path)
    song_number=0
    random_song_number=0
  
#resizes the canvas
def resize():
    global resized
    global title_album_name
    if resized == False:
        window.geometry("585x160")
        resized = True
    else:
        window.geometry("365x160")
        resized = False

    queue_list()
    
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

shuffleimage = PhotoImage(file="shuffle.png")
shuffle = Button(window, image=shuffleimage, background="white", borderwidth=0, command=shuffle_clicked)
shuffle.place(x=275, y=82)

queueimage=PhotoImage(file="Queue.png")
queue=Button(window,image=queueimage,background="white",borderwidth=0,command=resize)
queue.place(x=325,y=83)

#placing down the text
text()

#placing down the song position labels and sliders
song_progress=Label(window,text="0:00",font=("Calibri", 9), background="white", bd=0)
song_progress.place(x=2,y=136)

song_length=Label(window,text="0:00",font=("Calibri", 9), background="white", bd=0) 
song_length.place(x=336,y=136)

#this configues the white background for the ttk slider
style=ttk.Style()
style.configure('.', background='white')

status_bar = Label(window, text="", bd=1, relief=GROOVE, anchor=E )

#This is the song position slider
song_progress_bar = ttk.Scale(window, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=300)
song_progress_bar.place(x=32,y=132)

slider_label = Label(window, text="0")

#This is the volume scale slider
volume_scale = Scale(window, from_=0, to=100,orient = VERTICAL, command= set_vol,bg="white",borderwidth=0,highlightthickness=0)
volume_scale.set(100)
volume_scale.place(x=545,y=30)

window.mainloop()