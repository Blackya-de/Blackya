import tkinter as tk
import threading
#from file_dir_path import *
from Receive import *
from tkinter import filedialog,messagebox
from Sender import Send,file_sel

window = tk.Tk()

window.geometry('1250x500+70+150')
window.resizable(width=False,height=False)
window.title("Sender file")
window.configure(bg="#282828")
#window.iconbitmap('images/success.ico')

header = Label(window,width=1200,bg="#141414",padx=50,pady=13).place(x=0,y=0)

#Section of file Sending:
button = Button(text ="Send a file",fg ='white', bg='black', relief=FLAT,width = 24 , height = 1,command =lambda: file_sel(window),borderwidth=0).place(x = 200,y = 80)
host = Label(window,text="Host:   ",fg='white',bg="#282828",width=7,).place(x=185,y=180)
ip=Entry(window,width=20)
ip.place(x=240,y=180)


#Button that lunch the execution of sending the file
SendBtn = Button(window,text="Send",fg='white', bg='black', relief=FLAT,width = 14 , height = 1,command=lambda:Send(ip.get(),window)).place(x=240,y=250)
#Section of Receive files:
name = Label(window,text="File name:     ",fg='white',bg="#282828",width=20,).place(x=790,y=150)
e = Entry(window,width=24)
e.place(x=815,y=180)

button2 = Button(window,text ="Receive File",fg ='white', bg = 'black', relief=FLAT,width=24 ,height = 1,command = threading.Thread(target=Receive,args=(window,e)).start).place(x = 800, y=80)

copyright = Label (window , text ="Copyright C 2020 Blackya . All right reserverd",fg="white",bg="#282828").place(x=500,y=470)

window.mainloop()