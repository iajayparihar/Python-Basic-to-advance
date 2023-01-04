import pandas as pd 
import mysql.connector as connector

con = connector.connect(host="localhost",database="employee",user="root",password="Abhigyan@786")

if con.is_connected():
    Fletter = input("Enter the first letter of Name :- ")
    df=pd.read_sql("select * from employ where Name like '%s%%' "%(Fletter) , con)
    # df=pd.read_sql("select * from employ where Name like '_%s%%' "%(Fletter) , con) 
    # for second letter find use '_%s%%'
    # for third letter find use '__%s%%'
    print(df)
else:
    print("mysql connection problem")