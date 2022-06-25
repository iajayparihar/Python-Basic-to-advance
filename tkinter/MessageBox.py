from tkinter import *
from tkinter import messagebox as msg
win =Tk()
win.geometry("500x60")
def hello():
                # " title  "," containt " 
    msg.showinfo("Show info","hello World")
    msg.showwarning("show warning","are you there?")
    msg.showerror("show Error","ERROR !!!")
    msg.askokcancel("ask ok cancel","you are good person.")
    msg.askquestion("ask queston","Are you a good persion")
    msg.askretrycancel("ask retry cancel","what do you want cancel or retry ???")
    msg.askyesno("ask yes no","did you know Abhigyan?")
    msg.askyesnocancel("ask yes no cancel ","toh fir plan cancel")

b1=Button(win,text="press this Button for MessageBox",command=hello)
b1.pack()
b2=Button(win,text="Exit",command=win.destroy)
b2.pack()
win.mainloop()