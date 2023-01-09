import pandas as pd
import pymysql
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:Abhigyan786@localhost/employee")
mycon = engine.connect()
print("connection successful")
df = pd.read_sql("select * from emp1",mycon)
print(df)

update_name = input("Enter the name which you want to update :- ")
update_which_col = input("Enter the column which you want to update :- ")
update_col_value=input("Enter the column value :- ")
#find index for selecting the row

indx = df[df['Name'] == update_name].index
df.loc[indx,update_which_col]= update_col_value
print(df)
df.to_sql('emp1', mycon,if_exists="replace",index=False)
print("record updated successfully from database")