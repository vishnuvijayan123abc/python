# overloading is the method or operators that can do diffrent function with the same name and different parameters/arguments
# class A:
#     def product(self,a,b):
#         print(a*b)
#     def product(self,a,b,c):
#         print(a*b*c)

#obj=A()
#obj.product(1,2)
#obj.product(1,2,3)
#in the above code we use two method but we can use only the second method because python does not support overloading

#method to achive method overloading
     #1)multiple dispatch method:it is the method that used for achiving overloading

#pip:python installer package
#pip install(package name)

from multipledispatch import dispatch
# class A:
#     @dispatch(int,int)
#     def product(self,a,b):
#         print(a*b)
#     @dispatch(int,int,int)
#     def product(self,a,b,c):
#         print(a*b*c)
# obj=A
# obj.product(1,3)
# obj.product(1,2,3)
# class A:
#     @dispatch(str,str)
#     def stri(self,a,b):
#         print(a+b)
#     @dispatch(str,int,float)
#     def stri(self,a,b,c):
#         print("name",a,"\n""id",b,"\n""marks:",c)
# obj=A()
# obj.stri("hello","bye")
# obj.stri("vishnu",5,55.5)


