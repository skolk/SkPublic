from tkinter import *

window=Tk()

def km_to_miles():
    print(e1_value.get())
    miles=float(e1_value.get())
    miles=miles**1.60
    t1.insert(END,miles)

b1 = Button(window,text="Execute", command=km_to_miles)
b1.grid(row=2,column=1)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=5)
t1.grid(row=0,column=3)


window.mainloop()
