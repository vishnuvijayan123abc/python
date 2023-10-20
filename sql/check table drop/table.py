import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="project"

)
mycursor=mydb.cursor()

#id name phone email
sql="create table table_name(id int auto_increment,name varchar(50),primary key(id))"
mycursor.execute(sql)
mydb.commit() # used to save changes
print("table sucessfully created")