#an if condition inside another if condition
#if condition:
#    if condition:
#         body of nested if
#      elif condition:
#         body of nested elif
#      else:
#          body of nested else
#elif condition:
      # body of elif

#write a pgrm to findlargest of three numbers using neted if
# a=int(input ("enter a"))
# b=int(input ("enter b"))
# c=int(input ("enter c"))
# if a>b:
#     if a>c:
#         print("%d is greater"%a)
# elif b>c:
#     print("%d is greater"%b)
# else:
#     print("%d is greater"%c)

#largest of 4 number using nested if
# a=int(input ("enter a"))
# b=int(input ("enter b"))
# c=int(input ("enter c"))
# d=int(input("enter d"))
# if a>b:
#     if a>c:
#         if a>d:
#             print("a is greater")
#         else:
#           print("c is greater")
#
# elif b>c:
#
#         if b>d:
#             print("b is greater")
#
# elif c>d:
#     print("c is greater")
# else:
#     print("d is greater")

#gender male or female
# if gender = male age<18 queue1
#if gender =female age<18 q1
# if gender femal age>=18 and age<=50 q2
#if gender female and age>50 q3

# if male age>=18 and age<=50 q4
# if male age>50 q5
#
g=input("enter your gender")
age=int(input("enter your age"))

if g=="male":
    if age<18:
        print("queue 1")
    elif age>=18:
       if age<=50:
         print("queue4")
       elif age>50:
         print("queue5")
elif g=="female":
    if age<18:
        print("queue 1")
    elif age>=18:
       if age<=50:
         print("queue2")
       elif age>50:
         print("queue3")









