import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycursor=mydb.cursor()
#sql="drop table student"
mycursor.execute(sql)
mydb.commit() # used to save changes
print("removed")


sql="truncate table table name" #removes all the row from a table but the table structure remains


#delete databade
sql="drop database database_name"