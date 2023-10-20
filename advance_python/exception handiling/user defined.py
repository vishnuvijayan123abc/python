#in python usr can define coustom exception by creating a class,this exception class has not be defined  either directly or idirectly
#from the build in exception class most # of build in exception are also derived from this class
# class Zeroerror(Exception):
#     pass
# class Nagerror(Exception):
#     pass
#
# try:
#     num=int(input("enter number"))
#     if num==0:
#         raise Zeroerror
#     elif num<0:
#         raise Nagerror
# except Zeroerror:
#     print("zero errror")
# except Nagerror:
#     print("neg")
#


class old(Exception):
    pass
class young(Exception):
    pass
try:
    age=int(input("enter your age"))
    if age>50:
        raise old
    elif age<21:
        raise young
    else:
        print("you are registered")
except old:
    print("you are too old")
except young:
    print("you are too young")