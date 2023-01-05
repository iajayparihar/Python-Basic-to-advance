import pandas as pd
from sqlalchemy import create_engine
import pymysql
engine = create_engine("mysql+pymysql://root:Abhigyan786@localhost/employee")
mycon=engine.connect()
print('connection successfull')

dic={"empid":[13,14,15],"Name":["sajid","yatin","deepu"],"salary":[1000,222,3000]}
df=pd.DataFrame(dic)
print(df)
# .to_sql("table name",connection,if_exists="replace / append") 
df.to_sql("emp1",mycon,if_exists="append",index=False)
print("record inserted successfully")