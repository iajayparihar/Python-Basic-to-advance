import mysql.connector as mycnt
from mysql.connector import Error
# Convert binary data to proper format and write it on hardDisk
def write_file(data,filename):
    with open(filename,"wb") as file:
        file.write(data)

def read_BLOB(empid,photo,biodata):
    print("reading BLOB data from ___ table.")
    try:
        con=mycnt.connect(host="localhost",database="tkinter1",user="root",password="Abhigyan@786")

        cursor=con.cursor()
        fetch_blob_quert="""SELECT * from empinfodetail where id=%s"""

        cursor.execute(fetch_blob_quert,(empid,))
        result=cursor.fetchall()
        for row in result:
            print("ID =",row[0],)
            print("Name =",row[1])
            image=row[2]
            file1=row[3]
            print("Storing employee image and bio-data on disk \n")
            write_file(image,photo)
            write_file(file1,biodata)

    except Error as e:
        print("Failed to read BLOB data from mysql table {}".format(e))

    finally:
        if con.is_connected():
            cursor.close()                               
            con.close()
            print("Connection is closed .")

read_BLOB(2,"E:\zzzzz\w2c.jpg", "E:\zzzzz\dapython2.py")