#date time module supplies class to work with dtae and time
import datetime
# y=int(input("enter the year"))
# m=int(input("enter the month"))
# d=int(input("enter the day"))
# date=datetime.date(y,m,d)
# print(date)

#datetime.date.today
# today=datetime.date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)

#datetime.datetime.now
# a=datetime.datetime.now()
# print(a)

#diference between 2 dates
# d=datetime.datetime(2023,12,11)
# d1=datetime.datetime(1998,8,7)
# a=d-d1
# print(a)

#timedelta
from datetime import timedelta
# d=datetime.date.today()
# d+=timedelta(days=15)
# print(d)

#find the date before 20 days
d=datetime.date.today()
d-=timedelta(days=20)
print(d)