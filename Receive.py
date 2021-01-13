import socket 
import threading
from tkinter import *
from tkinter import messagebox

def Receive(window,e):
    filename=e.get()
    #hostname = socket.gethostname()
    #host = socket.gethostbyname(hostname)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("127.0.0.1",9999))
    s.listen(5)
    info = Label(window,text="Waiting the send of file",width=30,fg="white",bg="black").place(x=790,y=120)
    c, addr =s.accept()
    data = c.recv(1024)
    filesize = len(data)
    if not filename:
        print("please insert a filename")
    else:
        f=open(str(filename),'wb')
        data = c.recv(1024)
        totalReceive = len(data)
        f.write(data)
        while totalReceive < filesize :
            data = c.recv(1024)
            totalReceive += len(data)
            f.write(data)
        #complet = Label(window,text="Download Complet")
        c.send(b'Downlaod completed')
        print("Download has complete")
        completed = Label(window,text="Download has complete",fg="white",bg="black",width=35).place(x=785,y=210)
    s.close()
    #messagebox.showinfo("Succesful Receive","Download has been completed")
