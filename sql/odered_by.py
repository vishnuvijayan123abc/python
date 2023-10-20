#ordered by in my sql is a key word thbat is used to sortrecordsin assenting oder or in decending oder
import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"

)
mycursor=mydb.cursor()
sql="select id from student_reg order by id desc"
mycursor.execute(sql)
data=mycursor.fetchall()
for i in data:
    id=i[0]
    name=i[1]
    email=i[2]
    phone_number=i[3]
    print("sucess")