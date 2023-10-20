import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"

)
mycursor=mydb.cursor()

#id name phone email
sql="create table mark(id int auto_increment,roll int,maths int,che int, english int, primary key(id))"
mycursor.execute(sql)
mydb.commit() # used to save changes
print("table sucessfully created")
#

