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
    roll = int(input("enter roll number"))
    maths=int(input("enter mark"))
    che = int(input("enter mark"))
    english = int(input("enter mark"))



#id name phone email
    sql="insert into mark  (roll,maths,che,english)values(%d,%d,%d,%d)"%(roll,maths,che,english)
    mycursor.execute(sql)
    mydb.commit() # used to save changes
print("table sucessfully created")