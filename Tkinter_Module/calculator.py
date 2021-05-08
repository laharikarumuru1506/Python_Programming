"""displays a calculator in gui application
   program using tkinter module
   """
from tkinter import *

exp=""
def input_num(num,eq):
    global exp
    exp+=str(num)
    eq.set(exp)

def evaluate_num(eq):
    global exp
    res=str(eval(exp))
    eq.set(res)

def clear_all(num,eq):
    global exp
    exp=""
    eq.set(exp)

#creating a instance of tkinter module
m=Tk()
m.title("Calculator")
m.geometry("237x210")
eq=StringVar()
Entry(m,textvariable=eq).grid(columnspan=4,ipadx=55,ipady=10)
Button(m,text=7,height=2,width=7,command=lambda:input_num(7,eq)).grid(row=1,column=0)
Button(m,text=8,height=2,width=7,command=lambda:input_num(8,eq)).grid(row=1,column=1)
Button(m,text=9,height=2,width=7,command=lambda:input_num(9,eq)).grid(row=1,column=2)
Button(m,text='/',height=2,width=7,command=lambda:input_num('/',eq)).grid(row=1,column=3)
Button(m,text=4,height=2,width=7,command=lambda:input_num(4,eq)).grid(row=2,column=0)
Button(m,text=5,height=2,width=7,command=lambda:input_num(5,eq)).grid(row=2,column=1)
Button(m,text=6,height=2,width=7,command=lambda:input_num(6,eq)).grid(row=2,column=2)
Button(m,text='*',height=2,width=7,command=lambda:input_num('*',eq)).grid(row=2,column=3)
Button(m,text=1,height=2,width=7,command=lambda:input_num(1,eq)).grid(row=3,column=0)
Button(m,text=2,height=2,width=7,command=lambda:input_num(2,eq)).grid(row=3,column=1)
Button(m,text=3,height=2,width=7,command=lambda:input_num(3,eq)).grid(row=3,column=2)
Button(m,text='-',height=2,width=7,command=lambda:input_num('-',eq)).grid(row=3,column=3)
Button(m,text=0,height=2,width=7,command=lambda:input_num(0,eq)).grid(row=4,column=0)
Button(m,text='X',height=2,width=7,command=lambda:clear_all('X',eq)).grid(row=4,column=1)
Button(m,text='+',height=2,width=7,command=lambda:input_num('+',eq)).grid(row=4,column=2)
Button(m,text='=',height=2,width=7,command=lambda:evaluate_num(eq)).grid(row=4,column=3)
m.mainloop()
