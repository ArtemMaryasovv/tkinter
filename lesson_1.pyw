from tkinter import *
root=Tk()
root.geometry("350x200")
btn1=Button(root, text='Button 1', width=10, height=5, bg='white',fg='black')
btn1.pack(side='left')
btn2=Button(root, text='Button 2', width=10, height=5, bg='white',fg='black')
btn2.pack(anchor='ne')
root.mainloop()
