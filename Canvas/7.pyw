from tkinter import *
from random import randint,choice
colors=['green','blue','red','yellow','violet']
root=Tk()
canv=Canvas(root,width=500,height=500)
canv.pack()
count_bluebig=0
count_redsmall=0
for i in range(20):
    R=randint(10,40)
    x=randint(R,500-R)
    y=randint(R,500-R)
    color=choice(colors)
    canv.create_oval(x-R,y-R,x+R,y+R,fill=color)
    if R > 50 and color=='blue':

        count_bluebig+=1
    if R<20 and color == 'red':
        count_redsmall+=1
print(count_bluebig, "blue and big oval")
print(count_redsmall, "red and small oval")
    
root.mainloop()
