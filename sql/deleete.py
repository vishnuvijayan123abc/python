import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycursor=mydb.cursor()
id=int(input("enter the id to delete"))
sql="delete from student_reg where id=%d"%id
mycursor.execute(sql)
mydb.commit()
print("id deleted")