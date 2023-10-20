#syntax:
# try :
    #code to be excuted
# except:
    # catch the exception

# zero division error
# try:
#    a=int(input("enter number"))
#    b=int(input("enter your number"))
#    c=a/b
#    print(c)
# except:
#     print("cannot divide by zero")

#solve qutracti equation using exception handelling
# try:
#     a=int(input("enter a"))
#     b=int(input("enter b"))
#     c=int(input("enter c"))
#
#     x=-b+(b**2)-(4*a*c)**.5/(2*a)
#     x1=-b-(b**2)-(4*a*c)**.5/(2*a)
#     print(x)
#     print(x1)
# except:
#     print("not divide by zero")

#value error:
# try :
#     a=int(input("enter a"))
#     print(a)
# except :
#     print("invalid input")


# try:
#    a=int(input("enter number"))
#    b=int(input("enter your number"))
#    c=a/b
#    print(c)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("value error")

#index error
# s = [1, 2, 3, 5]
# try:
#     a=int(input("enter position"))
#     print(s[a])
# except ValueError:
#     print("value error")
# except IndexError :
#     print("index out of range")

#file not found error
# import os
# try:
#     file_name=input("enter the file name")
#     os.remove(rf"C:\Users\VISHNU\Desktop\python\{file_name}")
#     print("file removed")
# except FileNotFoundError:
#     print("file not found")
# except ValueError:
#     print("value error")
a=int(input("enter"))
print(b)

