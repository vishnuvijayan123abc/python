import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="project"

)
num=int(input("enter the number of data"))
for i in range(num):
    mycursor=mydb.cursor()
    name=input("enter your name")
    sql="insert into  table_name(name)values('%s')"%(name)
    mycursor.execute(sql)
    mydb.commit() # used to save changes
print("table sucessfully created")