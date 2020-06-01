from tkinter import *
from tkinter import filedialog

def file_sel(window):
    global filePath
    filePath = filedialog.askopenfilename(initialdir="",title="Select a file")
    nameFile = Label(window,text="File Path:{}".format(filePath),bg="#282828",fg="white").place(x= 200,y= 140)
    

def ask_directory():
    dirName = filedialog.askdirectory()
    nameDir = Label(window,text="Directory Path: {}".format(dirName)).place(x=200,y=140)