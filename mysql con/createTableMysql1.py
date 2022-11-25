import mysql.connector as mycnt
from mysql.connector import Error
try:
    con=mycnt.connect(host="localhost",database="tkinter1", user="root",password="Abhigyan@786")
    
    mysql_Create_table_Query="""CREATE TABLE empinfodetail(id int(4),name varchar(250), photo  VARCHAR(320) ,biodata VARCHAR(320) )"""

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
