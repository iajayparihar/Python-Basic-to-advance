import pandas as pd 
# import mysql.connector as connector
from sqlalchemy import create_engine
import pymysql

engine = create_engine("mysql+pymysql://root:Abhigyan786@localhost/employee")
mycon=engine.connect()

# con = connector.connect(host="localhost",database="employee",user="root",password="Abhigyan786")
try:
    df=pd.read_sql("select * from employ ",mycon)
    # print(df)
    # if only add one row then no need to making a dataframe 
    single_row = {'empid':20,"Name":"abc","salary":00000}
    new_org_df = df.append(single_row, ignore_index = True)
    print("after append 1 row.")
    # print(new_org_df)

    new_row1 = {'empid':[17,18],
                "Name":["narayna","kushwant"],
                "salary":[60000,30000]}
    # print()
    milti_row_df = pd.DataFrame(new_row1)
    print(milti_row_df)
    # print()
    org_df1= pd.concat([new_org_df, milti_row_df],ignore_index= True)
    org_df1.reset_index()
    print(org_df1)
    org_df1.to_sql("emp1", mycon,if_exists="append",index=False)
    print("record inserted successfully")

finally:
    pass