# using longblob for image in mysql create table image datatype.
import mysql.connector as mycnt
from mysql.connector import Error
def converToBinaryData(filename):
    #Converting digital data to binary format
    with open (filename,"rb")as file:
        binaryData=file.read()
    return binaryData

def insertBLOB(empid,name,photo,biodataFile):
    print("Inserting BLOB into empinfodetail table.")
    try:
        con=mycnt.connect(host="localhost",database="tkinter1",user="root",password="Abhigyan@786")

        cursor=con.cursor()
        insert_blob_query=''' INSERT INTO empinfodetail(id,name,photo,biodata)VALUES(%s,%s,%s,%s)'''
        empPic=converToBinaryData(photo)
        file1=converToBinaryData(biodataFile)

        #conver data into tuple format
        insert_blob_tuple=(empid,name,empPic,file1)
        result=cursor.execute(insert_blob_query,insert_blob_tuple)

        con.commit()

        print("Image and file inserted successfully as a BLOB into empinfodetail table {} .".format(result))

    except Error as e:
        print("Failed inserting BLOB data into mysql table{}".format(e))

    finally:
        if con.is_connected():
            cursor.close()
            con.close()
            print("Connection is closed .")
insertBLOB(2,"Venom" , "E:\zzzzz\w3c.jpg", "E:\zzzzz\dapython1.py")

