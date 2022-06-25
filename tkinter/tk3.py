from tkinter import *
win=Tk()
win.geometry("500x300")
user_name=Label(win,text="User Name").place(x=40,y=60)
user_password=Label(win,text="Password").place(x=40,y=100)
submit_btn=Button(win,text="Submit").place(x=40,y=130)
user_name_input=Entry(win,width="30").place(x=110,y=60)
user_password_input=Entry(win,width="30").place(x=110,y=100)
win.mainloop()