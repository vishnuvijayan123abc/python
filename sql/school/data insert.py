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
    roll = int(input("enter roll number"))
    school_name=input("enter") 


#id name phone email
    sql="insert into  school(name,roll,school_name)values('%s',%d,'%s')"%(name,roll,school_name)
    mycursor.execute(sql)
    mydb.commit() # used to save changes
print("table sucessfully created")