from tkinter import *
root=Tk()
canv=Canvas(root,width=200,height=100)
canv.pack()
canv.create_oval(100,25,150,75,fill='black')
root.mainloop()
