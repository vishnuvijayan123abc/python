#same method name with same number of arguments, it is used to chnge the behaviours of existing method,
#need two class ad need inheritence
# class A:
#     def display(self):
#         print("a")
# class B(A):
#     def display(self):
#         print("b")
# obj=A()
# obj.display()
# obj=B()
# obj.display()

#over riding with multiple inheritence
# class a:
#     def fun(self):
#         print("a")
# class b:
#     def fun1(self):
#         print("b")
# class c(a,b):
#     def fun(self):
#         print("c")
#     def fun1(self):
#         print("c")
# obj=c()
# obj.fun()
# obj.fun1()

#over riding using multilevel
class a:
    def fun1(self):
        print("a")
class b(a):
    def fun1(self):
        print("b")
class c(b):

    def fun1(self):
        print("c")

obj=c()

obj.fun1()
