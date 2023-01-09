import mysql.connector as mycnt
from mysql.connector import Error

try:
    con=mycnt.connect(host="localhost",database="mca",user="root",password="Abhigyan786")

    mySql_insert_query='''INSERT INTO admission(Rollno,First_Name,Last_Name,Mobile_no) VALUES (9,"choper","Deer",7777777777)'''

    cursor=con.cursor()
    cursor.execute(mySql_insert_query)
    con.commit()
    print(cursor.rowcount,"Record inserted successfully into student table")

except Error as e:
    print("Failed to insert record into student table{}".format(e))

finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("MySql connection is closed .")