import socket
import os
from tkinter import *
from tkinter import filedialog

def file_sel(window):
    global filePath
    filePath = filedialog.askopenfilename(initialdir="",title="Select a file")
    nameFile = Label(window,text="File Path:{}".format(filePath),bg="#282828",fg="white").place(x= 200,y= 140)

def Send(ip,window):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,9999))
        filesize = os.path.getsize(filePath)
        s.send(str(filesize))
        with open(filePath,'rb')as f:
            bytesToSend = f.read(1024)
            s.send(bytesToSend)
            while bytesToSend !="":
                bytesToSend = f.read(1024)
                s.send(bytesToSend)
            state = s.recv(1024)
            complish = Label(window,text=state,fg ='white', bg='black',width=35).place(x=200 ,y=210)
    except:
        error = Label(window,text="Host is down",fg ='white', bg='black',width=20).place(x=240 ,y=210)
