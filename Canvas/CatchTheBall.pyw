from tkinter import *
from random import randrange as rnd, choice

color=['green','red','blue','black','limegreen','midnightblue','gold']

x=0
y=0
r=0
points=0
miss=0

def ball():
    global x, y, r, res
    canv.delete(ALL)
    x=rnd(100,700)
    y=rnd(100,500)
    r=rnd(30,50)
    res=canv.create_text(60, 20, text=str(points)+'/'+str(miss), font='Arial 20')
    canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(color), width=0)
    root.after(1000,ball)

def click(event):
    global points, miss, res
    if abs(x-event.x)<r and abs(y-event.y) <r:
        points+=1
        canv.delete(ALL)
        res=canv.create_text(60, 20, text=str(points)+'/'+str(miss), font='Arial 20')
    else:
        miss+=1
        canv.delete(ALL)
        res=canv.create_text(60, 20, text=str(points)+'/'+str(miss), font='Arial 20')

root=Tk()
root.geometry('800x550')
root.title('CatchTheBall')
canv=Canvas(root,width=800,heigh=550,bg='darkblue')
canv.pack()

root.config(cursor='heart')
root.after(1000,ball)
canv.bind('<Button-1>', click)

root.mainloop()
        
    
