import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"

)
mycursor=mydb.cursor()

#id name phone email
sql="create table school(id int auto_increment,name varchar(50),roll int,school_name varchar(50),primary key(id))"
mycursor.execute(sql)
mydb.commit() # used to save changes
print("table sucessfully created")