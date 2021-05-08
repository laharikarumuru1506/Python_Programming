"""program that generates a password...
   it's a gui application using tkinter module
   random module is used to display random password in a given range of set of values
   pyperclip module is used to copy and paste the generated password
   """
import random
import pyperclip as pc
import string
from tkinter import *
#cretaing a instance of tkinter module
master=Tk()
var=StringVar()
var1=IntVar()
master.title("PASSWORD GENERATOR")
master.geometry("420x370")
Label(master,text="PASSWORD GENERATOR APPLICATION").place(x=100,y=10)
Label(master,text="PASSWORD LENGTH").place(x=150,y=40)
Spinbox(master,from_=4,to=10,textvariable=var1).place(x=150,y=70)
def rand_password():
    list=""
    password=""
    list=string.printable
    num=var1.get()
    for i in range(num):
        password+=random.choice(list)
    var.set(password)
def copy_clip():
    password1=var.get()
    pc.copy(password1)

Entry(master,textvariable=var).place(x=154 ,y=140)
Button(master,text="GENERATE PASSWORD",width=20,command=rand_password).place(x=140 ,y=110)
Button(master,text="COPY TO CLIPBOARD",width=20,command=copy_clip).place(x=140 ,y=170)

master.mainloop()
