# syntax
# class a:
#     def setval(self):
#         print("iam parent")
# class b(a):
#     def set1(self):
#         print("iam child")
# c=b()
# c.set1()
# c.setval()

# parent class company name loctaion,child class eployee name id salary phone
# class company:
#     def cp(self,name,loction):
#         self.nm=name
#         self.lc=loction
#         print("company name =",self.nm,"\n""location =",self.lc)
# class employee(company):
#     def ep(self,name,id,salery,phone):
#         self.na=name
#         self.id=id
#         self.sal=salery
#         self.ph=phone
#         print("name =",self.nm,"\n""id =",self.id,"\n""salary =",self.sal,"\n""phone =",self.ph)
# ob=employee()
# ob.cp("tcs","kochi")
# ob.ep("vishnu vijayan",5505,35000,9847481745)


#single inheritance using condtructor
     #supper:it is a function that used to call the constructor of a parent class
       #syntax
#
# class A:
#     def __init__(self):
#         print("parent class")
# class b:
#     def setval(self):
#         print("child")
#         super().__init__()
#
# ob=b()
# ob.setval()



class vechile:
    def __init__(self,name,number):
        self.nm=name
        self.nu=number
        print("vechile name =",self.nm,"\n""number =",self.nu)
class car(vechile):
    def __init__(self,name,number,color,price):
        super().__init__(name,number)
        self.cl=color
        self.pr=price
        print("colour =",self.cl,"\n""price  =",self.pr)
o=car("bmw","kl059876","black",268750)

