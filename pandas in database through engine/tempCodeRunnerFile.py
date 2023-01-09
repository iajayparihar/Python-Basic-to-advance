import pandas as pd
from sqlalchemy import create_engine
import pymysql
from tkinter import *
win=Tk()
win.geometry("500x500")
win.title("Delete column ")

engine = create_engine("mysql+pymysql://root:Abhigyan786@localhost/employee")
mycon=engine.connect()
print('connection successfull')
df= mycon.execute("select * from emp1")
# df = pd.read_sql("select * from emp1",mycon)
print("before delete table ")
print(df)

l_header = [i for i in df.keys()] # column headers
l_row = [ i for i in df.values()] # rows
print(l_header)
print("------------")
print(l_row)
