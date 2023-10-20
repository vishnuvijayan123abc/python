#class is a collection of objects (class is a blue print of a object)\
# clsss laptop object hp assus accer ,,ram, ic, mother board propprty and behaviour
#car is a class object is bmw,benz, and tyre engine propery and behaviour
# class class_name:
#     def function_name(self):
#         print("hello")
# obj=class_name()
# obj.function_name()

#member function : a function that define isid a class called member function or method

# class summ:
#     def add(self,a,b):
#         c=a+b
#         print(c)
# a=int(input("enter"))
# b=int(input("enter"))
# ob=summ()
# ob.add(a,b)

#object creation:(a real world entities or in other word it is an instance of class
# self is a self varible of a member function,thre varible that delcraded self that can access anywhere inside the class


# class laptop:
#     def setval(self,name,os,ram,price):
#         self.nm=name
#         self.os=os
#         self.rm=ram
#         self.pr=price
#         print("barnd =",self.nm)
#         print("os =",self.os)
#         print("ram =",self.rm)
#         print("peice=",self.pr)
# obj=laptop()
# obj.setval("dell","windows","16gb",28500)
# obj1=laptop()
# obj.setval("hp","windows 11","32gb",55000)

#creat a class person with  arguments name age gender height weight
# class person:
#     def prs(self,name,age,gender,height,weight):
#         self.nm=name
#         self.age=age
#         self.gn=gender
#         self.hg=height
#         self.we=weight
#         print("name =",self.nm ,"\n""age =",self.age,"\n""gender=",self.gn,"\n""height=",self.hg,"\n""weight =",self.we)
# ob=person()
# ob.prs("arun",25,"male",168,55)
# ob1=person()
# ob1.prs("anu",24,"female",155,45)
# ob2=person()
# ob2.prs("arjun",26,"male",165,85)


#static varibles: a varible that defines inside a class but outside function called static varible we cannot change the
                #value of static varible during object creation

# class class_name:
#     #static varible=value
#     def function_name(self):
#         #body
# ob=class_name()
# ob.function_name()

# class employee:
#     cm="tcs"
#     def setv(self,id,name,salary):
#         self.id=id
#         self.nm=name
#         self.sl=salary
#         print("company name =",employee.cm)
#         print("id =",self.id,"\n""name =",self.nm,"\n""salary =",self.sl)
# ob=employee()
# ob.setv(2014,"arun",27500)
# print()
# b1=employee()
# ob.setv(2055,"varun",29500)


#cerate a class student with atleast 2 static varible and dinamic varibles name,roll number,total marks
# class students:
#     sn="rajagiri"
#     cla=10
#     def stud(self,name,roll,total):
#         self.nm=name
#         self.rol=roll
#         self.to=total
#         print("school name =",students.sn,"\n" "class =",students.cla)
#         print("name =",self.nm,"\n""roll number =",self.rol,"\n""total =",self.to)
# ob=students()
# ob.stud("vishnu",25,555)


