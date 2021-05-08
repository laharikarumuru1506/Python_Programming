"""program that counts the time and displays time after every second on the screen
  importing time module and tkinter module
  """
import time
from tkinter import *
from tkinter import messagebox
#creating a instance of tkinter module
m=Tk()
m.title("Timer Clock")
m.geometry("250x170")
hour=IntVar()
min=IntVar()
sec=IntVar()
hour.set("00")
min.set("00")
sec.set("00")
Entry(m,textvariable=hour,width=3).place(x=70 ,y=50)
Entry(m,textvariable=min,width=3).place(x=110 ,y=50)
Entry(m,textvariable=sec,width=3).place(x=150 ,y=50)
#function that defines the time after every second 
def countdown():
    temp=hour.get()*3600+min.get()*60+sec.get()
    while temp>-1:
        mins,secs=divmod(temp,60)
        hours=0
        if mins>60:
            hours,mins=divmod(mins,60)
        hour.set("{0:02d}".format(hours))
        min.set("{0:02d}".format(mins))
        sec.set("{0:02d}".format(secs))
        m.update()
        time.sleep(1)
        if temp==0:
            messagebox.showinfo(title="countdown time",message="Time's up")
        temp-=1
Button(m,text="set countdown",command=countdown,width=20).place(x=50,y=100)

m.mainloop()
