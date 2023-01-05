import pandas as pd
from sqlalchemy import create_engine
import pymysql
engine = create_engine("mysql+pymysql://root:Abhigyan786@localhost/employee")
mycon=engine.connect()
print('connection successfull')
df = pd.read_sql("select * from emp1",mycon)
print("before delete table ",df)

delemp_col = input("Enter the column for delete :- ")

# drop that column in dataframe
df.drop(delemp_col,inplace=True,axis=1)
print("After deleted record %s"%(delemp_col))
print(df)

# write new dataframe to database (after deleted record)
# if_exists is use for overwrite or append the data in existing table if table is not present then create table and write data

df.to_sql("emp1",mycon,if_exists="replace",index=False)
print("record successfully from database")
