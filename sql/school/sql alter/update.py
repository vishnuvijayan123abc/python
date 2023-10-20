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
sql="update school set location='%s' where id=%d"%(name,id)
mycursor.execute(sql)
mydb.commit()
print("success")