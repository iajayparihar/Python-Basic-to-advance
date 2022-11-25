import mysql.connector as mycnt
from mysql.connector import Error

try:
    con=mycnt.connect(host="localhost",database="employee",user="root",password="Abhigyan@786")
    cursor=con.cursor()
    con.autocommit=False
    #widraw from Venom account
    update_query=''' Update employ set salary=salary-1000 where empid=2'''
    cursor.execute(update_query)
    
    # Deposit to account bangu
    update1_query=''' Update employ set salary=salary+1000 where empid=1'''
    cursor.execute(update1_query)
    
    con.commit()
    print("Data updated successfully into employ table using prepared statement.")

except Error as e:
    print("parameterized query failed {}".format(e))
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("mysQl connection is closed")