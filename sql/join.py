#used to combain row from two or more tables based on a related coloum between them
import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"

)
num=int(input("enter the number of data"))
for i in range(num):
    mycursor=mydb.cursor()
    name=input("enter your name")
    address=input("enter email")


#id name phone email
    sql="insert into  student_regg(name,address)values('%s','%s')"%(name,address)
    mycursor.execute(sql)
    mydb.commit() # used to save changes
print("table sucessfully created")