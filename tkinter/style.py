from tkinter import *
from tkinter.ttk import *
win=Tk()
win.geometry("180x180")
v=StringVar(win,"1")

st=Style(win)
st.configure("TRadiobutton",background="light green",foreground
="red",font=("arial",10,"bold"))

values={"RadioButton 1" : "1","Radiobutton 2" :"2","Radiobutton 3":"3","Radiobutton 4":"4","Radiobutton 5" : "5" }

for(t,val)in values.items():
    Radiobutton(win,text=t,variable=v,value=val).pack(fill=X,ipady=8)
mainloop()