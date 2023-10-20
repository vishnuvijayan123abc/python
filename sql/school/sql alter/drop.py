#query to drop a coloum

import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycursor=mydb.cursor()
sql="alter table school drop location"
mycursor.execute(sql)
mydb.commit() # used to save changes
print("removed")