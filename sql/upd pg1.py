#update ph using id and name
import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycursor=mydb.cursor()
id=int(input("enter id"))
name=input("enter name")
phone_number=int(input("enter phone"))
sql="update student_reg set phone_number=%d where id=%d and name='%s'"%(phone_number,id,name)
mycursor.execute(sql)
mydb.commit()
print("success")