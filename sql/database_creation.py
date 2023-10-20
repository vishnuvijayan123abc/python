import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password=""

)

#create a curssor object
mycurssor = mydb.cursor()

#cursor object which is used to select retrive data from a set of row and aslo it is used to excte an sql command

#create database databasename
sql="create database employee"
mycurssor.execute(sql)
print("database created sucessfully")