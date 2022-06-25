from tkinter import *
win=Tk()
win.geometry("700x350")
def on_click(event):
    label["text"]="Hello,there!"

def on_release(event):
    label["text"]="Button ,Released!"

label=Label(win,text="Click anyWhare...",font=("calibari 18 bold"))
label.pack(pady=60)

win.bind("<ButtonPress-1>",on_click)
win.bind("<ButtonRelease-1>",on_release)
mainloop()