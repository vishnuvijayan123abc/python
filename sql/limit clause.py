import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycursor=mydb.cursor()
limit=int(input("enter limit"))
sql="select * from student_reg  limit %d"%(limit)
mycursor.execute(sql)
data=mycursor.fetchall()
for i in data:
    id=i[0]
    name=i[1]
    print("id =",id,"name=",name)