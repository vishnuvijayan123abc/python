import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password=""

)
mycurssor = mydb.cursor()
sql="create database project"
mycurssor.execute(sql)
print("database created sucessfully")