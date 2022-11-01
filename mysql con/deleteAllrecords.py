import mysql.connector as mycnt
from mysql.connector import Error
try:
    con=mycnt.connect(host="localhost",database="bca", user="root",password="Abhigyan@786")
    # deleteAll_Row_Query=''' drop table student'''
    # alter_column='''ALTER TABLE student DROP COLUMN salary'''
    delete_database_query='''DROP DATABASE bca'''

    cursor=con.cursor()
    cursor.execute(delete_database_query)
    con.commit()
    print(cursor.rowcount,"Record deleted Successfully")

except Error as e:
    print("Failed to deleted :", e)
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("MySql connection is closed ")