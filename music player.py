from tkinter import *
from tkinter import StringVar
import pygame
import os

root = Tk()
root.geometry("720x480")
root.title("Music Player")


status = StringVar()


pygame.init()
pygame.mixer.init()

def playsong():
    songtrack.config(state=NORMAL)
    songtrack.delete('1.0',END)
    songtrack.insert('1.0',playlist.get(ACTIVE))
    songtrack.config(state=DISABLED)

    status.set("Playing")

    pygame.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.music.play()

def stopsong():
    songtrack.config(state=NORMAL)
    songtrack.delete('1.0',END)
    songtrack.config(state=DISABLED)

    status.set("Stopped")

    pygame.mixer.music.stop()

def pausesong():
    status.set("Paused")
    pygame.mixer.music.pause()

def unpausesong():
    status.set("Playing")
    pygame.mixer.music.unpause()

def nextsong():
    status.set("next")
    pygame.mixer.music.next()

trackframe = LabelFrame(root, text='track name', font=("Arial", 15, "bold"),
 bg='red', fg='black',bd=5, relief=GROOVE)
trackframe.place(x=0, y=200, width=720, height=275)

songtrack = Text(trackframe, width=40, height=2, font=("Arial", 15),
bg='black', fg='white', state=DISABLED)

songtrack.grid(row=0, column=0, padx=10, pady=5)

trackstatus = Label(trackframe, textvariable= status,font=("Sans-serif", 12),
bg='black', fg='white')
trackstatus.grid(row=0, column=1, padx=10, pady=5)

buttonframe = LabelFrame(root, text='Panel', font=('Arial',15,'bold'), 
bg='black', fg='white', bd=5 , relief=GROOVE, pady=10)
buttonframe.place(x=0,y=320, width=720, height=175)

playbtn = Button(buttonframe, text='Play', width=7, height=2, font=('Arial', 16), 
fg='white', bg='red', command=playsong)
playbtn.grid(row=0, column=1, padx=10, pady=5)

nextbtn = Button(buttonframe, text='next', width=7, height=0, font=('Arial', 16), 
fg='white', bg='red', command=nextsong)
nextbtn.grid(row=0, column=2, padx=10, pady=5)

pasuebtn = Button(buttonframe, text='Pause', width=7, height=2, font=('Arial', 16), 
fg='white', bg='red', command=pausesong)
pasuebtn.grid(row=0, column=3, padx=10, pady=5)

unpasuebtn = Button(buttonframe, text='Unpause', width=7, height=0, font=('Arial', 16), 
fg='white', bg='red', command=unpausesong)
unpasuebtn.grid(row=0, column=4, padx=10, pady=5)

stopbtn = Button(buttonframe, text='Stop', width=7, height=2, font=('Arial', 16), 
fg='white', bg='red', command=stopsong)
stopbtn.grid(row=0, column=5, padx=10, pady=5)

songsframe = LabelFrame(root, text='Playlist', font=('Arial', 15, 'bold'),
bg='red', fg='white', bd=5, relief=GROOVE)
songsframe.place(x=0,y=0,width=720, height=200)

scroll_y = Scrollbar(songsframe, orient=VERTICAL)
playlist = Listbox(songsframe, selectbackground="black", selectmode=SINGLE,
font=('Arial', 12), bg='white', fg='black', bd=5, relief=GROOVE, yscrollcommand=scroll_y.set)
scroll_y.config(command=playlist.yview)
scroll_y.pack(side=RIGHT, fill=Y)
playlist.pack(fill=BOTH)

os.chdir(r"D:\khodi\music\music")
songtracks = os.listdir()
for track in songtracks:
    if ".mp3" in track:
        playlist.insert(END,track )
    else:
        pass

root.mainloop()