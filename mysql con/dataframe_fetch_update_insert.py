import pandas as pd
from mysql.connector import Error
import mysql.connector as mycon   # con connection
from sqlalchemy import create_engine # myconn engine connection
import pymysql

try: 
    engine = create_engine("mysql+pymysql://root:Abhigyan786@localhost/employee")
    myconn=engine.connect()
    
    con = mycon.connect(host="localhost",database="employee",user="root",password="Abhigyan786")

    data_fetch_Query= "select * from employ;"
    cursor= con.cursor(dictionary=True) # dictionary = True is append for column name 
    cursor.execute(data_fetch_Query)
    feched_result=cursor.fetchall()
    print("data fetch done successfully.")
    df1= pd.DataFrame(feched_result)
    # print(df1)

    # if only add one row then no need to making a dataframe 
    single_row = {'empid':16,"Name":"gunwant_Sir_jii","salary":999999}
    new_org_df = df1.append(single_row, ignore_index = True)
    print("after append 1 row.")
    # print(new_org_df)

    # if we add more then one row at a time then we need to make that a dataframe
    new_row1 = {'empid':[17,18],
                "Name":["narayna","kushwant"],
                "salary":[60000,30000]}
    # print()# for new line

    milti_row_df = pd.DataFrame(new_row1)
    # print(milti_row_df)
#
    # print()# for new line
    
    new_org_df3= pd.concat([new_org_df, milti_row_df],ignore_index= True)
    new_org_df3.reset_index()
    print(new_org_df3)

    new_org_df3.to_sql("emp1",myconn,if_exists="append",index=False)
    print("data inserted succesfully into the sql databases.")

    
except Error as e:
    print("Error in reading data from Mysql table{}".format(e))



