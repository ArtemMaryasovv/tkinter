from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import asksaveasfile, askopenfile
FILE_NAME = NONE

def new_file():
    global FILE_NAME
    FILE_NAME = "Untitled"
    text.delete('1.0', END)

def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    
    FILE_NAME = inp.name

    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)

def save_file():
    data = text.get('1.0', END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()

def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Oops!", message="Unable to save file....")

def close_file():
    root.destroy()

def clear():
    text.delete(1.0, END)

def show_about():
    second = Tk()
    second.title('About')
    second.resizable(0, 0)
    second.geometry('300x200')
    lb1 = Label(second, text="Version 1.0")
    lb2 = Label(second, text="Made by Artem Maryasov")
    bt1 = Button(second, text="Exit", command=lambda: second.destroy())
    lb1.pack()
    lb2.pack()
    bt1.pack()

def show_help():
    showinfo(title="Help", message="¯\_(ツ)_/¯")

def show_help():
    showinfo(title="Useless", message="¯\_(ツ)_/¯")

root=Tk()
root.title('Notepad')

root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, font='Arial 20')
text.pack()

menuBar =Menu(root)

fileMenu = Menu(menuBar)

menuBar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label = "New", command=new_file)
fileMenu.add_command(label = "Open...", command=open_file)
fileMenu.add_command(label="Save...", command=save_file)
fileMenu.add_command(label="Save as", command=save_as)

fileMenu.add_separator()
fileMenu.add_command(label="Exit", command = close_file)

editMenu = Menu(menuBar)
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label = "Clear", command=clear)

helpMenu = Menu(menuBar)
menuBar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="Help", command=show_help)
helpMenu.add_command(label="About", command=show_about)

UselessButtonMenu = Menu(menuBar)
menuBar.add_cascade(label="UselessButton", menu=UselessButtonMenu)
UselessButtonMenu.add_command(label="AnotherUselessButton",command=show_help)

root.config(menu=menuBar)

root.mainloop()    
