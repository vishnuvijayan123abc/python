# def function_name():  #function declaration
#     print("hello")    #function definision
# function_name()


#write a pgrm to add two number using function add
# def add():
#     a=int(input("enter the number"))
#     b=int(input("enter the number"))
#     print(a+b)
# add()

#write a pgrm to find factorial using
# def fact():
#     a=int(input("enter your number"))
#     c=1
#     for i in range(1,a+1):
#         c*=i
#     print(c)
# fact()

#function with arguments
#they are values that are pass into a fuction during function calll ,they are also known as parameters
# def fun_add(k,n):
#     print(k+n)
# fun_add(1,2)

#varibles classification
# global varible and local varible

#global
#a varible that can access inside a fanction and same time outside function

#local varible
# access only inside function

# def add(a,b):
#     print(a+b)
# n1=int(input("enter the number"))
# n2=int(input("enter the number"))
# add(n1,n2)

# def fact(a):
#     c=1
#     for i in range(1,a+1):
#         c*=i
#     print(c)
# fact(5)

#find the largest off 3 numbers

# def lag(a,b,c):
#     if a>b and a>c:
#         print(a)
#     elif b>c:
#         print(b)
#     else:
#         print(c)
# lag(1,5,3)

# def rev(a):
#     print(a[::-1])
# rev("hello")


#find a number is amstrong
# def am(a):
#     g=a
#     sum=0
#     for i in range(a+1):
#         m = a % 10
#         sum+=m**3
#         a//=10
#
#     print(g)
#     if sum==g:
#         print("yes")
#     else:
#         print("no")
# am(153)


#reverse of a number with function
#area of a circle
#slove quadratic equation
# def rev(a):
#     r=0
#     while a!=0:
#         m=a%10
#         r=r*10+m
#         a//=10
#     print(r)
#
# rev(125)

# def circle(a):
#     a=3.14*a**2
#     print(a)
# a=int(input("enter your radius"))
# circle(a)


# def qu(a,b,c):
#     x=(b**2)-(4*a*c)
#     s1=(-b-(x**0.5))/(2*a)
#     s2 = (-b +(x ** 0.5)) / (2 * a)
#     print(s1)
#     print(s2)
# a=float(input("enter the a"))
# b=float(input("enter the b"))
# c=float(input("enter the c"))
#
# qu(a,b,c)
# a=int(input("enter a"))
# b=int(input("enter b"))
# c=int(input("enter c"))
# d=(b**2)-(4*a*c)**0.5
# x1=(-b+d)/(2*a)
# x2=(-b-d)/(2*a)
# print(x1)
# print(x2)


# def q (a,b,c):
#     d=(b**2)-(4*a*c)**0.5
#     x1=(-b+d)/(2*a)
#     x2=(-b+d)/(2*a)
#     print(x1)
#     print(x2)
# a=int(input("enter a"))
# b=int(input("enter b"))
# c=int(input("enter c"))
# q(a,b,c)


# def tax(a):
#     if a>=100000:
#         print("tax is",a*15/100)
#     elif a>50000 and a<=100000:
#         print("tax is",a*10/100)
#     else:
#         print("tax is ",a*5/100)
# a=int(input("enter the cost of bike"))
#
# tax(a)



# def check(a):
#     if a%2==0 and a%3==0:
#         print("its is divisible by 2 and 3")
#     else:
#         print("not")
# a=int(input("enter your number"))
# check(a)



# def bonus(s,e):
#     if e>10:
#         print("bonous is",s*10/100)
#     elif e>=6 and e<=10:
#         print("bonous is",s*8/100)
#     else:
#         print("bonous is",s*5/100)
# a=float(input("enter your salary"))
# b=int(input("enter your experience"))
# bonus(a,b)
#
