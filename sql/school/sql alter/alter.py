# query to add new coloum to an existing table
import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycursor=mydb.cursor()
sql="alter table school add location varchar(200)"
mycursor.execute(sql)
mydb.commit() # used to save changes
print("table sucessfully created")