from tkinter import *
from tkinter import messagebox
import random

master=Tk()
master.title("Tic-Tac-Toe Game")
master.geometry("420x350")
count=0

def play_game(i,j,b):
    global value,count
    value=str(random.choice(['X','O']))
    b["text"]=value
    if value=='X':
        b["bg"]="Blue"
    else:
        b["bg"] = "Yellow"
    count+=1
    if count==9:
        check_game()

def check_game():
    if b1["text"]=='X' and b2["text"]=='X' and b3["text"]=='X':
        b1.config(bg="Red")
        b2.config(bg="Red")
        b3.config(bg="Red")
        messagebox.showinfo(title="Tic-Tac-Toe",message="Congrats!!X Won")
    elif b4["text"] == 'X' and b5["text"] == 'X' and b6["text"] == 'X':
        b4.config(bg="Red")
        b5.config(bg="Red")
        b6.config(bg="Red")
        messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!X Won")
    elif b7["text"] == 'X' and b8["text"] == 'X' and b9["text"] == 'X':
        b7.config(bg="Red")
        b8.config(bg="Red")
        b9.config(bg="Red")
        messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!X Won")
    elif b1["text"] == 'X' and b4["text"] == 'X' and b7["text"] == 'X':
        b1.config(bg="Red")
        b4.config(bg="Red")
        b7.config(bg="Red")
        messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!X Won")
    elif b2["text"] == 'X' and b5["text"] == 'X' and b8["text"] == 'X':
         b2.config(bg="Red")
         b5.config(bg="Red")
         b8.config(bg="Red")
         messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!X Won")
    elif b3["text"] == 'X' and b6["text"] == 'X' and b9["text"] == 'X':
        b3.config(bg="Red")
        b6.config(bg="Red")
        b9.config(bg="Red")
        messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!X Won")
    elif b1["text"] == 'X' and b5["text"] == 'X' and b9["text"] == 'X':
        b1.config(bg="Red")
        b5.config(bg="Red")
        b9.config(bg="Red")
        messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!X Won")
    elif b1["text"] == 'X' and b2["text"] == 'X' and b3["text"] == 'X':
        b1.config(bg="Red")
        b2.config(bg="Red")
        b3.config(bg="Red")
        messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!X Won")
    else:
        if b1["text"] == 'O' and b2["text"] == 'O' and b3["text"] == 'O':
            b1.config(bg="Red")
            b2.config(bg="Red")
            b3.config(bg="Red")
            messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!O Won")
        elif b4["text"] == 'O' and b5["text"] == 'O' and b6["text"] == 'O':
            b4.config(bg="Red")
            b5.config(bg="Red")
            b6.config(bg="Red")
            messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!O Won")
        elif b7["text"] == 'O' and b8["text"] == 'O' and b9["text"] == 'O':
            b7.config(bg="Red")
            b8.config(bg="Red")
            b9.config(bg="Red")
            messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!O Won")
        elif b1["text"] == 'O' and b4["text"] == 'O' and b7["text"] == 'O':
            b1.config(bg="Red")
            b4.config(bg="Red")
            b7.config(bg="Red")
            messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!O Won")
        elif b2["text"] == 'O' and b5["text"] == 'O' and b8["text"] == 'O':
            b2.config(bg="Red")
            b5.config(bg="Red")
            b8.config(bg="Red")
            messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!O Won")
        elif b3["text"] == 'O' and b6["text"] == 'O' and b9["text"] == 'O':
            b3.config(bg="Red")
            b6.config(bg="Red")
            b9.config(bg="Red")
            messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!O Won")
        elif b1["text"] == 'O' and b5["text"] == 'O' and b9["text"] == 'O':
            b1.config(bg="Red")
            b5.config(bg="Red")
            b9.config(bg="Red")
            messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!O Won")
        elif b1["text"] == 'O' and b2["text"] == 'O' and b3["text"] == 'O':
            b1.config(bg="Red")
            b2.config(bg="Red")
            b3.config(bg="Red")
            messagebox.showinfo(title="Tic-Tac-Toe", message="Congrats!!O Won")

        else:
            messagebox.showinfo(title="Tic-Tac-Toe", message="Better Luck Next Time!!")




b1=Button(master,text="",bg="Grey",command=lambda:play_game(0,0,b1))
b2=Button(master,text="",bg="Grey",command=lambda:play_game(0,1,b2))
b3=Button(master,text="",bg="Grey",command=lambda:play_game(0,2,b3))

b4=Button(master,text="",bg="Grey",command=lambda:play_game(1,0,b4))
b5=Button(master,text="",bg="Grey",command=lambda:play_game(1,1,b5))
b6=Button(master,text="",bg="Grey",command=lambda:play_game(1,2,b6))

b7=Button(master,text="",bg="Grey",command=lambda:play_game(2,0,b7))
b8=Button(master,text="",bg="Grey",command=lambda:play_game(2,1,b8))
b9=Button(master,text="",bg="Grey",command=lambda:play_game(2,2,b9))

b1.grid(row=0,column=0,ipadx=60,ipady=45)
b2.grid(row=0,column=1,ipadx=60,ipady=45)
b3.grid(row=0,column=2,ipadx=60,ipady=45)

b4.grid(row=1,column=0,ipadx=60,ipady=45)
b5.grid(row=1,column=1,ipadx=60,ipady=45)
b6.grid(row=1,column=2,ipadx=60,ipady=45)

b7.grid(row=2,column=0,ipadx=60,ipady=45)
b8.grid(row=2,column=1,ipadx=60,ipady=45)
b9.grid(row=2,column=2,ipadx=60,ipady=45)


master.mainloop()
