import mysql.connector
from mysql.connector import Error
try:
    con=mysql.connector.connect(host="localhost",database="mca",user="root",password="Abhigyan786")
    if con.is_connected():
        db_info=con.get_server_info()
        print(db_info)
        cursor=con.cursor()
        cursor.execute("select database();")
        record=cursor.fetchone()
        print("You are connected to database :", record)
except Error as e:
    print("Error while connection to MYSQL", e)
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("MYSql connection is closed .")