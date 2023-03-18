import mysql.connector as mycon
from mysql.connector import Error
import pprint
try:
    con = mycon.connect(host='localhost', user='root',
                        password='Abhigyan786', database='student')
    cur = con.cursor()
    select_all=''' select * from info1 '''
    cur.execute(select_all)
    result=cur.fetchmany(5)
    pprint.pprint(result)

except Error:
    print(Error)
