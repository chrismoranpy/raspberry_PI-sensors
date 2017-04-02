from tkinter import *
from tkinter import messagebox

def helloCallBack():
    msg = messagebox.showinfo('hello python','hello world')

root=Tk()
root.geometry('500x500')

mb = Menubutton(root, text = 'File')
mb.grid()
mb.menu = Menu(mb, tearoff = 0)
mb['menu'] = mb.menu

mayoVar  = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton ( label = "mayo",
                          variable = mayoVar )
mb.menu.add_checkbutton ( label = "ketchup",
                          variable = ketchVar )
mb.pack()



b = Button(root, text= 'ok', command= helloCallBack)
b.place(x=125,y=50)


l = Label(root, text ='open the message box',bd=2)
l.place(x=0, y=50)

w = Listbox(root, selectmode = BROWSE)
w.pack()
w.insert(1,'python')
w.insert(2,'listbox')


root.mainloop()