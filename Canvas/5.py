from tkinter import *
from random import randint,choice
colors=['green','blue','red']
root=Tk()
canv=Canvas(root,width=500,height=500)
canv.pack()
count=0
for i in range(20):
    R=randint(10,40)
    x=randint(R,500-R)
    y=randint(R,500-R)
    color=choice(colors)
    canv.create_oval(x-R,y-R,x+R,y+R,fill=color)
    if color == 'red':
        count+=1
print(count)
    
root.mainloop()
