from tkinter import *
import tkinter as tk
##
import time
import os
window = tk.Tk()



maxframes = 15

gif_list=["city_explosion.gif","cityscape.gif","gundam.gif","motorcycle.gif","porsche.gif","robot_man.gif"]
gif_index=3
frames = [PhotoImage(file=('gifs\\'+gif_list[gif_index]),format = 'gif -index %i' %(i)) for i in range(maxframes)]
canvas=tk.Canvas(master=window, width=360, height=120)
canvas.pack()

def next_picture(frame_count):

    frame = frames[frame_count]
    frame_count += 1
    if frame_count == maxframes:
        frame_count = 0
    gif_image.configure(image=frame)
    window.after(100, next_picture, frame_count)

gif_image = Label(window)
gif_image.place(x=0,y=0)
window.after(0, next_picture, 0)

###
window.mainloop()