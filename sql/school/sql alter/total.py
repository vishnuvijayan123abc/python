import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycursor=mydb.cursor()
sql="alter table mark add total int as (maths+che+english)"
mycursor.execute(sql)
mydb.commit() # used to save changes
print("table sucessfully created")