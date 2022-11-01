import mysql.connector as mycnt
from mysql.connector import Error

try:
    con=mycnt.connect(host="localhost",database="bca",user="root", password="Abhigyan@786")

    print("Before updating Query ..")
    get_query=""" select * from student where rollno=6"""
    cursor=con.cursor()
    cursor.execute(get_query)
    res=cursor.fetchone()
    print(res,"\n")
    # update query in single record Know
    print("After updating Query ..")
    update_Query= """ Update student set Name="Bangu" where rollno=6 """
    cursor.execute(update_Query)
    con.commit()
    print("Row is updated successfully .")
except Error as e:
    print(e)
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("Connection is closed .")