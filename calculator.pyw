from tkinter import *
import math
root=Tk()
root.title("Calculator")
root.geometry("260x380")
root.resizable(0,0)

frame1 = Frame(root)
frame1.pack(side=TOP, pady=5)
frame2 = Frame(root)
frame2.pack(side=LEFT, anchor=N, pady=5, padx=5)

text1=Entry(frame1, font='Arial 30', justify='right', bd=15, insertwidth=-1)
text1.pack(side=RIGHT, anchor=N)

def number_button(num):
    text1.insert(END, str(num))

def clear():
    text1.delete(0,END)

def clear2():
    n=text1.get()
    text1.delete(len(n)-1)

def sqrt():
    try:
        s=int(text1.get())
        f=math.sqrt(s)
        clear()
        text1.insert(0,f)
    except Exception:
        clear()
        text1.insert(0,"Error")

def factorial():
    try:
        s=int(text1.get())
        f=1
        for i in range(1,s+1):
            f*=i
            clear()
            text1.insert(0,f)
    except Exception:
        clear()
        text1.insert(0,"Error")


def equal():
    s=text1.get()
    try:
        result=eval(s)
        clear()
        text1.insert(0,result)
    except Exception:
        clear()
        text1.insert(0,"Error")
    
btn1=Button(frame2,text='(', width=5,bd=4,height=2,bg='MintCream',command = lambda : number_button('('))
btn1.grid(row=2)
btn2=Button(frame2,text=')', width=5,bd=4,height=2,bg='MintCream',command = lambda : number_button(')'))
btn2.grid(row=2,column=1)
btn3=Button(frame2,text='^', width=5,bd=4,height=2,bg='MintCream',command = lambda : number_button('**'))
btn3.grid(row=2, column=3)
btn4=Button(frame2,text='n!', width=5,bd=4,height=2,bg='MintCream',command=factorial)
btn4.grid(row=2,column=4)
btn5=Button(frame2,text='M-', width=5,bd=4,height=2,bg='MintCream')
btn5.grid(row=2,column=5)

btn6=Button(frame2,text='←', width=5,bd=4,height=2,bg='GhostWhite')
btn6.grid(row=3,pady=2)
btn7=Button(frame2,text='CE', width=5,bd=4,height=2,bg='GhostWhite',command=clear)
btn7.grid(row=3,column=1)
btn8=Button(frame2,text='C', width=5,bd=4,height=2,bg='GhostWhite', command=clear2)
btn8.grid(row=3, column=3)
btn9=Button(frame2,text='±', width=5,bd=4,height=2,bg='GhostWhite')
btn9.grid(row=3,column=4)
btn10=Button(frame2,text='√', width=5,bd=4,height=2,bg='MintCream',command=sqrt
             )
btn10.grid(row=3,column=5)

btn11=Button(frame2,text='7', width=5,bd=4,height=2,bg='WhiteSmoke',command = lambda : number_button(7))
btn11.grid(row=4)
btn12=Button(frame2,text='8', width=5,bd=4,height=2,bg='WhiteSmoke',command = lambda : number_button(8))
btn12.grid(row=4,column=1)
btn13=Button(frame2,text='9', width=5,bd=4,height=2,bg='WhiteSmoke',command = lambda : number_button(9))
btn13.grid(row=4, column=3)
btn14=Button(frame2,text='/', width=5,bd=4,height=2,bg='GhostWhite',command = lambda : number_button('/'))
btn14.grid(row=4,column=4)
btn15=Button(frame2,text='%', width=5,bd=4,height=2,bg='MintCream',command = lambda : number_button('%'))
btn15.grid(row=4,column=5)

btn16=Button(frame2,text='4', width=5,bd=4,height=2,bg='WhiteSmoke',command = lambda : number_button(4))
btn16.grid(row=5,pady=2)
btn17=Button(frame2,text='5', width=5,bd=4,height=2,bg='WhiteSmoke',command = lambda : number_button(5))
btn17.grid(row=5,column=1)
btn18=Button(frame2,text='6', width=5,bd=4,height=2,bg='WhiteSmoke',command = lambda : number_button(6))
btn18.grid(row=5, column=3)
btn19=Button(frame2,text='*', width=5,bd=4,height=2,bg='GhostWhite',command = lambda : number_button('*'))
btn19.grid(row=5,column=4,padx=1)
btn20=Button(frame2,text='1/x', width=5,bd=4,height=2,bg='MintCream')
btn20.grid(row=5,column=5)

btn21=Button(frame2,text='1', width=5,bd=4,height=2,bg='WhiteSmoke',command = lambda : number_button(1))
btn21.grid(row=6,pady=2)
btn22=Button(frame2,text='2', width=5,bd=4,height=2,bg='WhiteSmoke',command = lambda : number_button(2))
btn22.grid(row=6,column=1)
btn23=Button(frame2,text='3', width=5,bd=4,height=2,bg='WhiteSmoke',command = lambda : number_button(3))
btn23.grid(row=6, column=3)
btn24=Button(frame2,text='-', width=5,bd=4,height=2,bg='GhostWhite',command = lambda : number_button('-'))
btn24.grid(row=6,column=4)
btn25=Button(frame2,text='=', width=5,bd=4,height=5,bg='MintCream',command=equal)
btn25.grid(row=6,column=5,rowspan=2)
btn26=Button(frame2,text='0', width=12,bd=4,height=2,bg='WhiteSmoke',command = lambda : number_button(0))
btn26.grid(row=7,columnspan=2)
btn28=Button(frame2,text=',', width=5,bd=4,height=2,bg='WhiteSmoke',command = lambda : number_button('.'))
btn28.grid(row=7, column=3)
btn29=Button(frame2,text='+', width=5,bd=4,height=2,bg='GhostWhite',command = lambda : number_button('+'))
btn29.grid(row=7,column=4)
root.mainloop()

