import pandas as pd 
import mysql.connector as connector

con = connector.connect(host="localhost",database="employee",user="root",password="Abhigyan@786")

if con.is_connected():
    Lemp_id=int(input("Enter the lower employee id :-"))
    Uemp_id=int(input("Enter the upper employee id :-"))

    df=pd.read_sql("select * from employ where empid between %s and %s"%(Lemp_id,Uemp_id),con)
    print(df)

else:
    print("mysql connection problem")