import pandas as pd
from sqlalchemy import create_engine
import pymysql
engine = create_engine("mysql+pymysql://root:Abhigyan786@localhost/employee")
mycon=engine.connect()
print('connection successfull')
df = pd.read_sql("select * from emp1",mycon)
print("before delete table ",df)

delemp_id = int(input("Enter the empid for delete :- "))
# we need index for deleting the row 
# finding the row index

delemp_index = df[df["empid"]==delemp_id].index

# drop that row in dataframe
df.drop(delemp_index,inplace=True)
print("After deleted record %s"%(delemp_id))
print(df)

# write new dataframe to database (after deleted record)
# if_exists is use for overwrite or append the data in existing table if table is not present then create table and write data
df.to_sql("emp1",mycon,if_exists="replace",index=False)
print("record successfully from database")
