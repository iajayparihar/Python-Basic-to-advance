from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

win=Tk()
win.geometry("300x200")
win.resizable(FALSE,FALSE)
win.title("Combowidget")

lab=ttk.Label(text="Please ,select a month :- ")
lab.pack(fill=X,padx=5,pady=5)

select_month=StringVar()
month_cb=ttk.Combobox(win,textvariable=select_month)

month_cb["values"]=[month_name[m][0:3] for m in range (1,13)]
month_cb["state"]="readonly"
month_cb.pack(fill=X,padx=5,pady=5)

def month_change(event):
    '''handle the month change event'''
    showinfo(title='Result',message=f'you selected {select_month.get()}!')

month_cb.bind("<<ComboboxSelected>>",month_change)
win.mainloop()