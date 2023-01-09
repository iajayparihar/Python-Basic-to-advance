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


delemp_col = input("Enter the column for delete :- ")

# drop that column in dataframe
# there is 3 ways for delete

df.drop(delemp_col,inplace=True,axis=1)  # with axis = 1  drop column and axis = 0 then rows

# del df[delemp_col]
# df.pop(delemp_col)

print("After deleted record %s"%(delemp_col))
print(df)

# write new dataframe to database (after deleted record)
# if_exists is use for overwrite or append the data in existing table if table is not present then create table and write data

# df.to_sql("emp1",mycon,if_exists="replace",index=False)
# print("column deleted successfully from database")

trv =Treeview(win,selectmode="browse")
trv.frid(row=1,column=1,padx=30,pady=20)
trv["height"]=10
trv["show"]="headlings"
trv["columns"]=11
for i in l_header:
    trv.column(i,width=10,ANCHOR="c")
    trv.heading(i,text=i)

for x in l_row:
    v=[r for r in dt]
    trv.insert("","end",iid=v[0],values=v)

win.mainloop()