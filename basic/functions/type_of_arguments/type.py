#arguments are calssifed in to 5 types
#positional arguments
#default arguments(it is values which are used to assign a default value to the argument)
#keyword arguments (durring a function call values pass through the arguments need not be in the order of parameters in the function
# definition this can be achived by key word arguments)

#arbittery argumets(for these aregument a star is placed brfore a parameter in function defiition which can hold any number of values )
# def add(*a):
#     b=0
#     for i in a:
#         b+=i
#     print(b)
# add(10,10,10)

# def mul(*a):
#     c=1
#     for i in a:
#         c*=i
#     print(c)
# mul(2,2,2)



# def larg(*a):
#     b=0
#     for i in a:
#
#         if i>b:
#             b=i
#     print(b)
# larg(-1,0,5,0)







# def add(a,b=5):
#     print(a+b)
# add(5,2)

# def mul(a,b,c=1,d=1):
#     print(a*b*c*d)
# mul(1,2,10,10)

# def larg(a,b,c=0,d=0):
#     if a>b and a>c and a>d:
#         print("a is greater")
#     elif b>c and b>d:
#         print("b is greater")
#     elif c>d:
#         print("c is grater")
#     else:
#         print("d is greater")
#
# larg(6,60,30,40)

#key word arguments
#
# def name(first_name,middel_name,second_name):
#     print(first_name,middel_name,second_name)
# name(middel_name="anu",first_name="ann",second_name="k")


#keywoard arbittary
#
# def name(**kwargs):
#     print(kwargs)
#     for i, j in kwargs.items():
#         print(i,j)
# name(name="john",name1="arun",name2="john wick")


#function with argument and return type
#the return is a special statement that u can only use inside a function to send the function results back to the colum

