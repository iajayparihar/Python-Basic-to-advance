import mysql.connector as mycnt
from mysql.connector import Error

try:
    con=mycnt.connect(host="localhost",database="mca",user="root",password="Abhigyan786")
    select_Query=''' select * from admission where rollno=4 '''
    cursor=con.cursor()
    cursor.execute(select_Query)
    res=cursor.fetchone()
    print(res)

    # delete record
    delete_Query=''' delete from admission where rollno=4 '''
    cursor.execute(delete_Query)
    con.commit()
    print(cursor.rowcount,"Number of rows deleted .")

    #verify
    cursor.execute(select_Query)
    result=cursor.fetchall()
    if len(result)==0:
        print("Query deleted Successfully . ")
    
except Error as e:
    print(e)

finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("Connection is closed .")