import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student"

)
mycursor=mydb.cursor()
sql="select school.name,mark.maths,mark.che,mark.english from school inner join mark on school.roll=mark.roll"
mycursor.execute(sql)
c=mycursor.fetchall()
for i in c:
    name=i[0]
    maths=i[1]
    che=i[2]
    english=i[3]
    print("name=",name ,"maths mark=",maths ,"che mark=",che,"english mark=",english)

