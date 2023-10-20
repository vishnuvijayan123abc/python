#an expection is an error which occur during the exceution of a pgrm and xpection handelling is a method that are used to catch and handdle
#exception in python
# they are classifies into two types
   #logic errors : these are error that are created by the programer (syntax error,intentation error,name error)
   #run time errors: these are error that are created by the end users during the pgrm execution
                              #(zero divison error,index error,value error,file not found error)



# expection handelling wiht arguments: it can have an argument which is a value that gives additional information about
                                    # the proble the content of the argument changes by the type of expetion
#
# try :
#     #code to be executed
# except Exceptiontype as argument:
#     exception body
# s=[1,2,3]
# try:
#     g=int(input("enter position"))
#     print(s[g])
#     a=int(input("enter a"))
#     b=int(input("enter b"))
#     c=a/b
#     print(c)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as w:
#     print(w)
# except IndexError as z:
# #     print(z)
# import os
# try:
#     a=int(input("enter"))
#     print(b)
#     os.remove(r"C:\Users\VISHNU\Desktop\python\deo.py")
#     print("removed")
# except FileNotFoundError as j:
#     print(j)
# except NameError as l:
#     print(l)
