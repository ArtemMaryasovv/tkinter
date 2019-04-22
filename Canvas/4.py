from tkinter import *
from random import randint,choice
colors=['green','blue','red','yellow','violet']
root=Tk()
canv=Canvas(root,width=500,height=500)
canv.pack()
for i in range(12):
    R=randint(10,40)
    x=randint(R,300-R)
    y=randint(R,300-R)
    color=choice(colors)
    canv.create_oval(x-R,y-R,x+R,y+R,fill=color)
root.mainloop()
