import mysql.connector as mycnt
from mysql.connector import Error

try:
    con=mycnt.connect(host="localhost",database="employee",user="root",password="Abhigyan@786")
    cursor=con.cursor(prepared=True)
    # parameterized query
    update_query=''' UPDATE employ set salary=%s where empid=%s '''
    #tuplr ti insert at placeholder
    tuple1=(9000,2)
    cursor.execute(update_query,tuple1)
    con.commit()
    print("Data updated successfully into employ table using prepared statement.")

except Error as e:
    print("parameterized query failed {}".format(e))
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("mysQl connection is closed")