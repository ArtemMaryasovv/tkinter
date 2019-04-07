from tkinter import *
root=Tk()
def summa(event):
    x1=int(e1.get())
    x2=int(e2.get())
    t3['text']=str(x1+x2)

def subtraction(event):
    x1=int(e1.get())
    x2=int(e2.get())
    s=str(x1-x2)
    v2.set(s)

def multiplication(event):
    x1=int(e1.get())
    x2=int(e2.get())
    t5['text']=str(x1*x2)

def division(event):
    x1=int(e1.get())
    x2=int(e2.get())
    t6['text']=str(x1/x2)

def clear(event):
    e1.delete(0,END)
    e2.delete(0,END)

t1=Label(root,text='Enter the first number')
t1.pack

e1=Entry(root)
e1.pack(pady=5)

t2=Label(root,text='Enter the second number')
t2.pack(pady=5)

e2=Entry(root)
e2.pack(pady=5)

btn1=Button(root,text='Fold',width=10,font='Arial 14')
btn1.pack(pady=5)
btn1.bind("<Button-1>",summa)

t3=Label(root,font='Arial 20')
t3.pack()
root.mainloop()

btn2=Button(root,text='Subtraction',width=10,font='Arial 14')
btn2.pack(pady=10)
btn2.bind("<Button-1>",subtraction)

v2=StringVar()
t4=Label(root,font='Arial 20')
t4.pack()
root.mainloop()

btn3=Button(root,text='Multiplication',width=10,font='Arial 14')
btn3.pack(pady=15)
btn3.bind("<Button-1>",multiplication)

t5=Label(root,font='Arial 20')
t5.pack()
root.mainloop()

btn4=Button(root,text='Division',width=10,font='Arial 14')
btn4.pack(pady=20)
btn4.bind("<Button-1>",division)

t6=Label(root,font='Arial 20')
t6.pack()
root.mainloop()

btn5=Button(root,text='Clear',width=10,font='Arial 14')
btn5.pack(pady=25)
btn5.bind("<Button-1>",clear)



