#sql="update table_nam set email='%s',phone=%d where id=%d
#update stud name and ph number using id
import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycursor=mydb.cursor()
id=int(input("enter id"))
email=input("enter name")
phone_number=int(input("enter phone"))
sql="update student_reg set email='%s',phone_number=%d where id=%d"%(email,phone_number,id)
mycursor.execute(sql)
mydb.commit()
print("success")