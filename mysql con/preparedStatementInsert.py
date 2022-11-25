import mysql.connector as mycnt
from mysql.connector import Error

try:
    con=mycnt.connect(host="localhost",database="employee",user="root",password="Abhigyan@786")
    cursor=con.cursor(prepared=True)
    # parameterized query
    insert_query=''' INSERT INTO employ(empid,Name,salary) VALUES(%s,%s,%s)'''
    #tuplr ti insert at placeholder
    tuple1=(4,"mmta",9000)
    tuple2=(5,"snu",2000)
    
    cursor.execute(insert_query,tuple1)
    cursor.execute(insert_query,tuple2)
    con.commit()
    print("Data inserted successfully into employ table using prepared statement.")

except Error as e:
    print("parameterized query failed {}".format(e))
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("mysQl connection is closed")