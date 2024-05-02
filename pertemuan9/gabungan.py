from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("300x300")

# Frame 1
frame1 = Frame(top)
frame1.pack()

def helloCallBack():
    msg=messagebox.showinfo("Hello Python", "Hello World")

B = Button(frame1, text="Hello", command=helloCallBack)
B.pack(pady=10)

# Frame 2
frame2 = Frame(top)
frame2.pack()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(frame2, text="Music", variable=CheckVar1, onvalue=1, offvalue=0)
C1.pack(side=LEFT, padx=10)

C2 = Checkbutton(frame2, text="Video", variable=CheckVar2, onvalue=1, offvalue=0)
C2.pack(side=LEFT, padx=10)

# Frame 3
frame3 = Frame(top)
frame3.pack()

L1 = Label(frame3, text="User Name")
L1.pack(side=LEFT, padx=10)

E1 = Entry(frame3, bd=5)
E1.pack(side=LEFT, padx=10)

# Frame 4
frame4 = Frame(top)
frame4.pack()

frame41 = Frame(frame4)
frame41.pack(side=TOP)

frame42 = Frame(frame4)
frame42.pack(side=BOTTOM)

redbutton = Button(frame41, text="Red", fg="red")
redbutton.pack(side=LEFT, padx=10)

greenbutton = Button(frame41, text="Brown", fg="brown")
greenbutton.pack(side=LEFT, padx=10)

bluebutton = Button(frame41, text="Blue", fg="blue")
bluebutton.pack(side=LEFT, padx=10)

blackbutton = Button(frame42, text="Black", fg="black")
blackbutton.pack(side=BOTTOM, pady=10)

top.mainloop()
