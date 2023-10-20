import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="project"

)
mycursor=mydb.cursor()

#id name phone email
sql="drop table table_name"
mycursor.execute(sql)
mydb.commit() # used to save changes
print("table sucessfully created")