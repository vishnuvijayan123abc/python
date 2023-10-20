import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"

)
num=int(input("enter the number of data"))
for i in range(num+1):
    mycursor=mydb.cursor()
    name=input("enter your name")
    email=input("enter email")
    phone_number=int(input("enter phone number"))

#id name phone email
    sql="insert into  student_reg(name,email,phone_number)values('%s','%s',%d)"%(name,email,phone_number)
    mycursor.execute(sql)
    mydb.commit() # used to save changes
print("table sucessfully created")