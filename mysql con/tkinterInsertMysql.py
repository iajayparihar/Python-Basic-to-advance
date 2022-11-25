import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector as mycnt
from mysql.connector import Error

def insertdb():
    try:
        con=mycnt.connect(host="localhost",database="tkinter1",user="root",password="Abhigyan@786")

        cursor=con.cursor(prepared=True)

        insert_query=''' INSERT INTO employee_data(fname,lname,email,age) VALUES (%s,%s,%s,%s) '''

        # tuple to insert placeholder
        tuple1=(entry_fname.get(),entry_lname.get(),entry_email.get(),entry_age.get())

        cursor.execute(insert_query,tuple1)
        con.commit()
        print("Data Inserted successfully into employee_data table using prepared statement .")
    except Error as e:
        print("Parameterized quert failed {}".format(e))
    finally:
        if con.is_connected():
            cursor.close()
            con.close()
            print("Connection is closed .")


win=Tk()
win.title("insert data")
bkg="#636e72"
frame=tk.Frame(win,bg=bkg)
frame.grid(row=0,column=0)

first_name=tk.Label(frame,text="First Name :",bg=bkg)
entry_fname=tk.Entry(frame)
first_name.grid(row=0,column=0)
entry_fname.grid(row=0,column=1,padx=10,pady=10)

second_name=tk.Label(frame,text="Last Name :",bg=bkg)
entry_lname=tk.Entry(frame)
second_name.grid(row=1,column=0)
entry_lname.grid(row=1,column=1,padx=10,pady=10)

label_email=tk.Label(frame,text="Email id :",bg=bkg)
entry_email=tk.Entry(frame)
label_email.grid(row=2,column=0)
entry_email.grid(row=2,column=1,padx=10,pady=10)

lable_age=tk.Label(frame,text="Age :",bg=bkg)
entry_age=tk.Entry(frame)
lable_age.grid(row=3,column=0)
entry_age.grid(row=3,column=1,padx=10,pady=10)

button_insert=tk.Button(frame,text="Insert Data",bg="orange",command=insertdb)
button_insert.grid(row=4,column=0,columnspan=2,sticky=EW)
win.mainloop()