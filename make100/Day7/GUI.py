from Tkinter import *

window=Tk()

def kg_to_GUI():
    print(e1_value.get())
    Kg=float(e1_value.get())
    grams=Kg*1000
    lbs=Kg*2.204
    oz=Kg*35.274
    t1.delete("1.0",END)
    t2.delete("1.0",END)
    t3.delete("1.0",END)
    t1.insert(END,grams)
    t2.insert(END,lbs)
    t3.insert(END,oz)

b1 = Button(window,text="Convert", command=kg_to_GUI)
b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

e2=Label(window,text="Kg")
e2.grid(row=0,column=2) 

t1=Text(window,height=1,width=1)
t1.grid(row=1,column=0)

g1=Label(window,text="g")
g1.grid(row=1,column=1)

t2=Text(window,height=1,width=5)
t2.grid(row=1,column=2)

g3=Label(window,text="lbs")
g3.grid(row=1,column=3)

t3=Text(window,height=1,width=5)
t3.grid(row=1,column=4)

g3=Label(window,text="Kg")
g3.grid(row=1,column=5)


window.mainloop()
