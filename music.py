from tkinter import *
import os
import pygame
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3

root = Tk()  #a window in tkinter initialized
root.minsize(1000, 1000)   #size of window
root.title("Indie Music Player")

listofsongs = []
songnames = []
index = 0
no_of_songs = 0

v = StringVar()
songlabel = Label(root,textvariable = v,width = 35)


def directory_chooser():
    global no_of_songs
    directory = askdirectory()  # choosing of directory
    os.chdir(directory)  # chooses current working directory

    for file in os.listdir(directory):  # os.listdir() lists all the files in the variable object directory
        if file.endswith(".mp3"):
            listofsongs.append(file)
            #whole_path = os.path.realpath(file)
            #song = ID3(whole_path)
            #songnames.append(song['TIT2'].text[0])
    no_of_songs = len(listofsongs)

def play():  #=> using separate function to play a song
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
    updatelabel()

def next(event):    #for index range out of range go back to first song. Add this feature later
    global no_of_songs,index
    index += 1
    index = index % no_of_songs
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def previous(event):
    global index,no_of_songs
    index += no_of_songs - 1
    index = index % no_of_songs
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def pause(event):
    pygame.mixer.music.pause()
    updatelabel()

def unpause(event):
    pygame.mixer.music.unpause()
    updatelabel()

def updatelabel():
    global index
    v.set(listofsongs[index])


directory_chooser()

label = Label(root, text="Indie Music Station")  # Displays the name
label.pack(pady=10)

listbox = Listbox(root)  # creates an area where songs are being displayed
listbox.pack(pady=10)

listofsongs.reverse()
for item in listofsongs:
    listbox.insert(0, item)  # 0 indicates starting from left
listofsongs.reverse()

nextsong = Button(root, text="  Next  " , bg="cyan")  # next button
nextsong.pack(fill=X,padx=10,pady=10)

previoussong = Button(root, text="Previous" , bg="cyan")  # previous button
previoussong.pack(fill=X,padx=10,pady=10)

pausesong = Button(root, text=" Pause  " , bg="cyan")  # stopbutton
pausesong.pack(fill=X,padx=10,pady=10)

unpausesong = Button(root, text = "Unpause " , bg="cyan")
unpausesong.pack(fill=X,padx=10,pady=10)
songlabel.pack()

nextsong.bind("<Button-1>",next)
previoussong.bind("<Button-1>",previous)
pausesong.bind("<Button-1>",pause)
unpausesong.bind("<Button-1>",unpause)
play()
root.mainloop()
