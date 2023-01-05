import pandas as pd
import mysql.connector as con

connection = con.connect(host="localhost",database="employee",user="root",password="Abhigyan@786")

if connection.is_connected():
    emp_id=int(input("Enter the Employee ID :- "))
    df=pd.read_sql("select * from employ where empid='%s' " %(emp_id),connection)
    print(df)
else:
    print("mysql connection problem")