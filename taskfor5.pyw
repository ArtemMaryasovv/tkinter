from tkinter import *
root=Tk()
root.geometry("350x200")
fr1=Frame(root)
fr1.pack(side='top', fill='both')
fr2=Frame(root)
fr2.pack(side='bottom', fill='both')
btn1=Button(fr1, text='Ok_1', width=10, height=2, bg='white',fg='black')
btn1.pack(side='left')
btn2=Button(fr1, text='Ok_2', width=10, height=2, bg='white',fg='black')
btn2.pack(side='right')
btn3=Button(fr2, text='Ok_3', width=10, height=2, bg='white',fg='black')
btn3.pack(side='left')
btn4=Button(fr2, text='Ok_4', width=10, height=2, bg='white',fg='black')
btn4.pack(side='right')
root.mainloop()
