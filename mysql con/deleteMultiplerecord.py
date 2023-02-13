import mysql.connector as mycnt
from mysql.connector import Error
try:
    con=mycnt.connect(host="localhost",database="mca", user="root",password="Abhigyan786")
    delete_Query=''' Delete from admission where Rollno =%s'''
    records_table_delete=[(1,),(3,)]
    cursor=con.cursor()
    cursor.executemany(delete_Query,records_table_delete)
    # con.commit()
    t=cursor.rowcount
    print(t,"Record deleted Successfully")

except Error as e:
    print("Failed to deleted :", e)
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("MySql connection is closed ")