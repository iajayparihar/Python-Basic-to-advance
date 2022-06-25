from tkinter import *
win=Tk()
win.geometry("300x300")
btn=Button(win,text="click me !",bd="5",command=win.destroy)
btn.pack(side="bottom")
win.mainloop()
