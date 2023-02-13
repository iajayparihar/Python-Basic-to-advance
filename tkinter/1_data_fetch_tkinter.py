from tkinter import * 

win=Tk()
win.geometry("500x500")
win.title("tkinter all method's")
name=Label(win,text="username")
name.grid(row=1,column=1)

btn1=Button(win,text='click me !',command=win.destroy)
btn1.grid(row=2,column=1)

entry1=Entry(win)
entry1.grid(row=3,column=1)

def txtvar():
    mytext.set('hello')

mytext=StringVar()


btn2=Button(win,text='show label',command=txtvar)
btn2.grid(row=5,column=1)

def add():
    res=int(first_entry.get())+int(second_entry.get())
    result.set(res) 

result=StringVar()
Label(win,text='first number').grid(row=6,column=1)
Label(win,text='second number').grid(row=7,column=1)
first_entry=Entry(win,border=3)
first_entry.grid(row=6,column=2)

second_entry=Entry(win,border=3)
second_entry.grid(row=7,column=2)

result_label=Label(win,textvariable=result)
result_label.grid(row=8,column=1)
btn3=Button(win,command=add,width=20,text='add')
btn3.grid(row=9,column=1)

win.mainloop()