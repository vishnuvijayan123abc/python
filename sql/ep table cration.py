import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)
mycursor=mydb.cursor()

sql="create table emp_details(emp_id int auto_increment,name varchar(50),salary int,company_name varchar(50),phone bigint(10),primary key(emp_id))"
mycursor.execute(sql)
mydb.commit()
print("created")