# def hello():
#     return "hello"
# print(hello())

#write a pgrm to multi two number with function and arguments
# def mup(a,b):
#     return(a*b)
#
# print(mup(8,2))

#find a number odd or even
# def oe(a):
#     if a%2==0:
#         return "%d,is even"%a
#     else:
#         return("%d,is odd"%a)
# print(oe(5))



def add(a,b):
   return a+b
def sub(a,b):
    return a-b
def mup(a,b):
    return a*b
def div(a,b):
    return a/b
print("simple calaculator \n option \n 1 addition \n 2 sub \n 3 mup \n 4 div")
a=int(input("enter your choise"))
if a>4:
    exit()
b = int(input("enter your number"))
c = int(input("enter your number"))
if a==1:
    print(b,"+",c,"=", add(b,c))
elif a==2:
   print(b, "-", c, "=", sub(b, c))
elif a==3:
    print(b, "*", c, "=", mup(b, c))
elif a==4:
    print(b, "/", c, "=", div(b, c))
else:
    exit()













