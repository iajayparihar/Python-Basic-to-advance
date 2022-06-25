from tkinter import *
win=Tk()
win.geometry("180x180")
v=StringVar(win,"1")
values={"RadioButton 1" : "1","Radiobutton 2" :"2","Radiobutton 3":"3","Radiobutton 4":"4","Radiobutton 5" : "5" }

for(t,val)in values.items():
    Radiobutton(win,text=t,variable=v,value=val,indicator=0,bg="light yellow",fg="blue").pack(fill=X,ipady=5)
mainloop()