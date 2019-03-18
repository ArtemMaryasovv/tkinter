from tkinter import *
root=Tk()
def summa(event):
    x1=int(e1.get())
    x2=int(e2.get())
    t3['text']=str(x1+x2)

def subtraction(event):
    x1=int(e1.get())
    x2=int(e2.get())
    t3['text']=str(x1-x2)

def multiplication(event):
    x1=int(e1.get())
    x2=int(e2.get())
    t3['text']=str(x1*x2)

def division(event):
    x1=int(e1.get())
    x2=int(e2.get())
    t3['text']=str(x1/x2)

def clear(event):
    e1.delete(0,END)
    e2.delete(0,END)

t1=Label(root,text='Enter the first number')
t1.pack

e1=Entry(root)
e1.pack(pady=5)

t1=Label(root,text='Enter the second number')
t1.pack(pady=5)

e2=Entry(root)
e2.pack(pady=5)

btn1=Button(root,text='Fold',width=10,font='Arial 14')
btn1.pack(pady=5)
btn1.bind("<Button-1>",summa)

btn2=Button(root,text='Subtraction',width=10,font='Arial 14')
btn2.pack(pady=5)
btn2.bind("<Button-1>",subtraction)

btn3=Button(root,text='Multiplication',width=10,font='Arial 14')
btn3.pack(pady=5)
btn3.bind("<Button-1>",multiplication)

btn4=Button(root,text='Division',width=10,font='Arial 14')
btn4.pack(pady=5)
btn4.bind("<Button-1>",division)

btn5=Button(root,text='Clear',width=10,font='Arial 14')
btn5.pack(pady=5)
btn5.bind("<Button-1>",clear)


t3=Label(root,font='Arial 20')
t3.pack()
root.mainloop()
