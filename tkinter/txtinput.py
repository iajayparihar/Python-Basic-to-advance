from tkinter import *
win=Tk()
win.geometry("300x400")
win.title('Q&A')
def take():
    Input=inputtxt.get("1.0","end-1c")
    if (Input=="120"):
        Output.insert(END,"Correct")
    else:
        Output.insert(END,"Wrong.Correct Ans is 120")
l=Label(win,text="what is  24*5 = ?")
inputtxt=Text(win,height=10,width=25,bg="lightyellow")
Output=Text(win,height=5,width=25,bg="light cyan")
Display=Button(win,height=4,width=25,text="SHOW ANSWER",command=take)
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
win.mainloop()
