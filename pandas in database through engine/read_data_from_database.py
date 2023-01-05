import pandas as pd
import mysql.connector as con

connection=con.connect(host="localhost",database="tkinter1",user="root",password="Abhigyan@786")

if connection.is_connected():
    df=pd.read_sql("select * from employee_data",connection)
    df.to_csv("employee_data.csv",index=False)
    print(df)
else:
    print("mysql connection problem")