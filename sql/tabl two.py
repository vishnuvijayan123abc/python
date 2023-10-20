import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"

)
mycursor=mydb.cursor()
sql="create table student_regg(id int auto_increment,name varchar(50),address varchar(50),primary key(id))"
mycursor.execute(sql)
mydb.commit() # used to save changes