from tkinter import *

win = Tk()
win.geometry('500x500')
win.title("Frames")
# make multipule frames
frame1 = Frame(win,background="black",border=5,highlightbackground="red",highlightthickness=5,width=0)
frame1.grid(row=0,column=0,padx=20,pady=20,ipadx=200,ipady=100)

# frame2 = Frame(win,background="red",border=5,borderwidth=50)
# frame2.pack()


btn1= Button(frame1,text="click me!",command=win.destroy,bd="10")
btn1.pack(side="bottom")
btn1.pack(side="left")
btn1.pack(side="right")
user_name = Label(frame1,text="User Name ").place(x=20,y=50)
password = Label(frame1,text="password ").place(x=20,y=80)
user_entry = Entry(frame1,width='40').place(x=100,y=50)
pass_entry = Entry(frame1,width="40").place(x=100,y=80)

# second frame

# btn1= Button(frame2,text="click me!",command=win.destroy,bd="10")
# btn1.pack(side="bottom")
# # btn1.pack(side="left")
# # btn1.pack(side="right")
# user_name = Label(frame2,text="User Name ").place(x=20,y=50)
# password = Label(frame2,text="password ").place(x=20,y=80)
# user_entry = Entry(frame2,width='40').place(x=100,y=50)
# pass_entry = Entry(frame2,width="40").place(x=100,y=80)


win.mainloop()