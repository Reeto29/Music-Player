#This is the backend

from pygame import mixer
from miniwindow import get_file_path
import os
import random
import time


path = get_file_path()

mixer.init()
number=1
muted=0
paused=0



def loading_songs(path):
    songs=[]
    for filename in os.listdir(path):
        if filename.endswith(".mp3"):
            songs.append(os.path.join(path,filename))

    return songs




songs=loading_songs(path)
song_number=0
mixer.music.load(songs[song_number])
volume=1

print ("Welcome to the Music Player!")




while True:
    
    #print(song_number)
    #print(len(songs))

    
    
    
    print ("""

    Type in ONE of the following numbers:

    1. Play
    2. Pause
    3. Stop
    4. Resume
    5. Mute
    6. Unmute
    7. Increase Volume
    8. Decrease Volume 
    9. Skip Song
    10. Exit
    11. BackSkip Song

    """)

    choice=input("Enter number here: ")
    
    if choice == "1":
       mixer.music.play()

    elif choice == "2":

        if mixer.music.get_busy():
            mixer.music.pause()
            paused=1 #song is paused
        else:
            print ("The music is not currently playing")
       
    elif choice == "3":
        
        mixer.music.stop()
        

    elif choice == "4":
        if paused:
            mixer.music.unpause()
            print("Resuming Song...")
        else:
            print("The song is not paused currently")

    elif choice == "5":
        previous_volume=mixer.music.get_volume()
        mixer.music.set_volume(0)

    elif choice == "6":
        mixer.music.set_volume(previous_volume)

    elif choice == "7":
        if volume >=1:
            print ("The volume is already at max")
        else:
            volume=(volume+0.25)
            mixer.music.set_volume(volume)

    elif choice == "8":
        volume=(volume-0.25)
        mixer.music.set_volume(volume)
    elif choice == "9":
        if (song_number + 1) == len(songs):
            continue
        else:
            song_number+=1
            mixer.music.load(songs[song_number])
            mixer.music.play()
    elif choice == "10":
         quit()
    elif choice =="11":
        if (song_number-1) == -1:
            continue
        else:
            song_number-=1
            mixer.music.load(songs[song_number])
            mixer.music.play()

    else:
        print ("Please enter a valid number")        