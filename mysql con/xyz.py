# import mysql.connector as mysql
# def data_fetch():
#     # if request.method=='POST':
#     #     naam=request.POST['uname']
#     #     rno = request.POST['uroll']
#         rno=1
#         naam='Abhigyan'
#         con = mysql.connect(host='localhost',user='root',password='Abhigyan786',database='django_login')
#         cur=(con.cursor())
#         query="select * from mca_result where rollno='{}' and name='{}' ".format(rno,naam)
#         cur.execute(query)    
#         data=tuple(cur.fetchall())
#         print(data)
#         for i in data:
#             print(i[0])


# data_fetch()
total=100
pre=round(total/6,2)
print(pre)