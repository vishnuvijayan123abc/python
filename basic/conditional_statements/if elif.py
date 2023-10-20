#the elif statement allows you to check multiples condition  for true and excute a block of code as soon as one of the conditions evaluvate to true
#if condition1:
     #body of if
#elif  condition2:
    #body 0f elif
#elif conditio3
      #body of elif
#else:
    #body of else#

# write a pgrm to check a number is positive zero or negative
# n=int(input("enter your number"))
# if n>0:
#     print("positive")
# elif n==0:
#     print("the given nuber is zero")
# else:
#     print("negative")

#write a pgrm to find the largest of 3 number
# a=int(input("enter a"))
# b=int(input("enter b"))
# c=int(input("enter c"))
# if a>b and a>c:
#     print("%d a is greater"%a)
# elif  b>c:
#     print("%d b is greater"%b)
# else:
#     print("%d is greater"%c)

# accept the agee of 4 people and display the youngest one
# age1=int(input("enter age 1"))
# age2=int(input("enter age 2"))
# age3=int(input("enter age 3"))
# age4=int(input("enter age 4"))
#
# if age1<age2 and age1<age3 and age1<age4:
#     print("age1 is younger")
# elif age2<age3 and  age3<age4:
#     print("age 2 is younger")
# elif age3<age4:
#     print("age 3 is younger")
# else:
#     print("age 4 is younger")

#write a pgrm to accept two numbers and mathamatical operators and perform operations  accordingly
# n1=int(input("enter number 1"))
# n2=int(input("enter number2"))
# op=input("enter your operator")
# if op=="+":
#     print(n1,op,n2,"=",n1+n2)
# elif op=="-":
#     print(n1,op,n2,"=",n1-n2)
# elif op=="*":
#     print(n1,op,n2,"=",n1*n2)
# elif op=="/":
#     print(n1,op,n2,"=",n1/n2)
# else:
#     print("invalid user input")


#accept the mark from user and display the grade according to the following criteria:
# 81 to 100 a+
# 71 to 80 a
# 61 t0 70 b+
#51 to 60 b
#41 to 50 c
#31 to 40 d
# 30 and below fail
#
# m=int(input("enter your mark"))
# if m>=81 and m<=100:
#     print("a+")
# elif m>=71 and m<=80:
#     print("a")
# elif m>=61 and m<=70:
#     print("b+")
# elif m >= 51 and m <= 60:
#     print("b")
# elif m >= 41 and m <= 50:
#     print("c")
# elif m >= 31 and m <= 40:
#     print("d")
# elif m<=30:
#     print("fail")
# else:
#     print("enter vaild input")

# write a pgrm to accept the cost price of bike and display the road tax to paid according to the following criteria

#>100000    15% tax
#>50000 and <=100000 10%tax
#<=50000 5% tax

# cost=int(input("enter the cost of bike"))
# if cost>100000:
#     tax=cost*15/100
#     print(tax)
# elif cost>=50000 and cost<=100000:
#     tax=cost*10/100
#     print(tax)
# else:
#     tax=cost*5/100
#     print(tax)
#

# the company decided to give bonus to the employee according to the criteria
# more than 10 years  10%
#>=6 and <=10 8%
#less than6 years 5%
s=int(input("enter your salary"))
y=int(input("enter your year"))
if y>10:
    print(s*10/100)
elif y>=6 and y<=10:
    print(s*8/100)
else:
    print(s*5/100)



