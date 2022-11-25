import mysql.connector as mycnt
from mysql.connector import Error

try:
    con=mycnt.connect(host="localhost",database="employee",user="root",password="Abhigyan@786")
    cursor=con.cursor(prepared=True)
    # parameterized query
    delete_query=''' Delete from employ where empid=%s'''
    #tuplr ti insert at placeholder
    empid=(5,)
    cursor.execute(delete_query,empid)
    con.commit()
    print("Data deleted successfully into employ table using prepared statement.")

except Error as e:
    print("parameterized query failed {}".format(e))
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("mysQl connection is closed")