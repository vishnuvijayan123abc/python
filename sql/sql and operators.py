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
sql="select * from student_reg where id=%d and name=%s"%(id,name)
mycursor.execute(sql)
a=mycursor.fetchone()
id=a[0]
name=a[1]
email=a[2]
phone_number=a[3]
print(id,name,email,phone_number)