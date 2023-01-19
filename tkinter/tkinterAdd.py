from tkinter import *
window=Tk()
def addNumber():
    result=int(box1.get()) + int(box2.get())
    myText.set(result)

myText=StringVar()
Label(window,text="First").grid(row=0, sticky=W)
Label(window,text="Second").grid(row=1, sticky=W)
Label(window,text="Result").grid(row=2, sticky=W)
res=Label(window,text="hello ",textvariable=myText).grid(row=2,column=1,sticky=W)
# label check ----------------->
box1=Entry(window,bd=5)
box1.grid(row=0,column=1)
box2=Entry(window,bd=5)
box2.grid(row=1,column=1)

b=Button(window,text="Calculate",command=addNumber)
b.grid(row=0,column=2,columnspan=2,rowspan=2,sticky=E+W+N+S,padx=5,pady=5)
window.mainloop()
