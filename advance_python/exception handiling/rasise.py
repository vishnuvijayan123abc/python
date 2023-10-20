#exception rasie keyword: it is used to raise exception or errors,it raise an error and stop the control flow of pgrm

#negative exception rasing
# try:
#     v=int(input('enter the number'))
#     if v>0:
#         print("positive")
#     elif v<0:
#         raise Exception  #exception block that catch any type of error
# except ValueError as z:
#     print(z)
# except Exception :
#     print("negative error occur")
#votting eligiblity
# try:
#     name=input("enter your name")
#     age=int(input("enter your age"))
#     if age>=18:
#         print(name,"is eligible for votting")
#     else:
#         raise Exception
# except ValueError as z:
#     print(z)
# except Exception:
#     print(name,"age is below 18")

#name exception
try:
    name=input("enter your name")
    if name.isalpha():

          print("sucessfull")
    else:
        raise Exception
except Exception:
    print("please input a valid name")
