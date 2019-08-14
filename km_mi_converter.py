from tkinter import *

root=Tk()
root.title('Kilometre <-> Mile Converter')

def km_to_mi():
    mi=float(e1_value.get())*0.621371
    t1.insert(END,mi)

def mi_to_km():
    km=float(e2_value.get())*1.609344
    t2.insert(END,km)


l1_km=Label(root, text = 'Kilometres')
l1_km.grid(row=0,column=1)

l1_mi=Label(root, text = 'Miles')
l1_mi.grid(row=0,column=2)

b1=Button(root,text="Km -> Mi",command=km_to_mi)
b1.grid(row=1,column=0)

e1_value=StringVar()
e1=Entry(root,textvariable=e1_value)
e1.grid(row=1,column=1)

t1=Text(root,height=1,width=20)
t1.grid(row=1,column=2)

l2_mi=Label(root, text = 'Miles')
l2_mi.grid(row=2,column=1)

l2_km=Label(root, text = 'Kilometres')
l2_km.grid(row=2,column=2)

b2=Button(root,text="Mi -> Km",command=mi_to_km)
b2.grid(row=3,column=0)

e2_value=StringVar()
e2=Entry(root,textvariable=e2_value)
e2.grid(row=3,column=1)

t2=Text(root,height=1,width=20)
t2.grid(row=3,column=2)

root.mainloop()