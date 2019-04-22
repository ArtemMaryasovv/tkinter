from tkinter import *
from random import randint,choice
colors=['green','blue','red','yellow','violet']
root=Tk()
canv=Canvas(root,width=500,height=500)
canv.pack()
count_red=0
count_green=0
for i in range(20):
    R=randint(10,40)
    x=randint(R,500-R)
    y=randint(R,500-R)
    color=choice(colors)
    canv.create_oval(x-R,y-R,x+R,y+R,fill=color)
    if color == 'red':
        count_red+=1
    if color == 'green':
        count_green+=1
print(count_red, "red oval")
print(count_green, "green oval")
    
root.mainloop()
