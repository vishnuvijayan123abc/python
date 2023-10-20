import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"

)
mycursor=mydb.cursor()

#id name phone email
sql="create table student_reg(id int auto_increment,name varchar(50),email varchar(50),phone_number bigint(10),primary key(id))"
mycursor.execute(sql)
mydb.commit() # used to save changes
print("table sucessfully created")
#

