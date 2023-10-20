#the calander module allows output clander like the program and provide additional function related to calander
import calendar
# year=int(input("enter the year"))
# # month=int(input("enter the month"))
# # a=calendar.month(year,month)
# # print(a)
# b=calendar.calendar(year,2,0,6,5)
#
# print(b)


#leep year
# year=int(input("enter your year"))
# a=calendar.isleap(year)
# print(a)

#text calander function
year=int(input("enter your year"))
a=calendar.TextCalendar(calendar.SUNDAY)
print(a.formatmonth(year,5))