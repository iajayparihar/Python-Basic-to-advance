from tkinter import *
win=Tk()
#win.geometry("500x300")
def motion(event):
    print("moved position: (%s,%s)"%(event.x,event.y))
    return
what="What do you Want hsdbxcuasdxwu uwcwuc ksacn akscjhbnsayuncwjc jbvcwjuhebcwuxbwjheb"
msg=Message(win,text=what)
msg.pack()
msg.config(background="lightgreen",font=("times",24,'italic'))
msg.bind("<Motion>",motion)
mainloop()