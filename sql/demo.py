import pymysql
mydbb=pymysql.connect(
    host="localhost",
    user="root",
    password=""

)

mycursor=mydbb.cursor()

sql="create database student"
mycursor.execute(sql)
print("data base created")
