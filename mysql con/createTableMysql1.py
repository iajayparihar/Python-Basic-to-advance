import mysql.connector as mycnt
from mysql.connector import Error
try:
    con=mycnt.connect(host="localhost",database="bca", user="root",password="Abhigyan@786")
    
    mysql_Create_table_Query="""CREATE TABLE student(rollno varchar(3) , Name varchar(250), salary int(6),  PRIMARY KEY(rollno) )"""

    cursor=con.cursor()
    result=cursor.execute(mysql_Create_table_Query)
    print(result)
    print("Employee Table created successfully ")

except Error as e:
    print("Failed to create table in sql :", e)
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("MySql connection is closed ")
