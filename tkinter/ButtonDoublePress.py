from tkinter import *
import sys;
def hello(a):
    print("single Click,Button-1")
def quit(z):
    print("Double Click, so let's stop please!")
    sys.exit()

widget=Button(None,text="mouse click")
widget.pack()
widget.bind("<Button-1>",hello)
widget.bind("<Double-1>",quit)
mainloop()