#delete using product name and coustmer name
import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
name=input("enter name")
email=input("enter the email")
mycursor=mydb.cursor()
sql="select name,email from student_reg"
mycursor.execute(sql)

a=mycursor.fetchall()
for i in a:
    if name==i[0] and email==i[1]:
        sql1 = "delete from student_reg where name='%s' and email='%s'" % (name, email)
        mycursor.execute(sql1)
        mydb.commit()
        print("deleted")
        break
else:
    print("data not found")





