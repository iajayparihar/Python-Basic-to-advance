import mysql.connector as mycnt
from mysql.connector import Error

try:
    con=mycnt.connect(host="localhost",database="bca",user="root",password="Abhigyan@786")

    data_fetch_Query="select * from student;"
    cursor=con.cursor()
    cursor.execute(data_fetch_Query)
    # gel all the records
    result=cursor.fetchall()
    for record in result:
        print("Roll No is :",record[0])
        print("Name  is   :",record[1])
        print("Salary  is :",record[2])
        print()
except Error as e:
    print("Error in reading data from MySql table {}".format(e))
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("MySql connection is closed .")