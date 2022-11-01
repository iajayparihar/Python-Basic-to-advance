import mysql.connector as mycnt
from mysql.connector import Error
try:
    con=mycnt.connect(host="localhost",database="bca", user="root",password="Abhigyan@786")
    delete_Query=''' Delete from student where rollno =%s'''
    records_tobe_delete=[(1,),(3,)]
    cursor=con.cursor()
    cursor.executemany(delete_Query,records_tobe_delete)
    con.commit()
    print(cursor.rowcount,"Record deleted Successfully")

except Error as e:
    print("Failed to deleted :", e)
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("MySql connection is closed ")