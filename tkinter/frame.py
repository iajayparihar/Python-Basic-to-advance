from tkinter import*
window=Tk()
window.state('zoomed')
left_frame=Frame(window,bg='black',borderwidth=3)
left_frame.pack(side=LEFT,anchor='ne',fill='y')


label1=Label(left_frame,text='click here for new window')
label1.pack(fill='x')
label2=Label(left_frame,text='click me')
label2.pack(fill='x')
label3=Label(left_frame,text='the end')
label3.pack(fill='x')

window.mainloop()


