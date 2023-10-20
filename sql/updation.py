import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycursor=mydb.cursor()
id=int(input("enter id"))
name=input("enter your name")
sql="update student_reg set name='%s' where id=%d"%(name,id)
mycursor.execute(sql)
mydb.commit()
print("success")