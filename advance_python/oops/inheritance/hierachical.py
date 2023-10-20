# class a:
#     def fun_a(self):
#         print("hai")
# class b(a):
#     def fun_b(self):
#         print("hello")
# class c(a):
#     def fun(self):
#         print("bye")
# ob=b()
# ob.fun_b()
# ob.fun_a()
# ob=c()
# ob.fun()
# ob.fun_a()

# class details:
#     def fun_det(self,id,name,gender):
#         self.id=id
#         self.nm=name
#         self.g=gender
#         print("id =",self.id,"\n""name =",self.nm,"\n""gender =",self.g)
# class developer(details):
#     def fun_dev(self,designation,company):
#         self.des=designation
#         self.com=company
#         print("designation =",self.des,"\n""company name =",self.com)
# class doctor(details):
#     def fun_doc(self,hospital,specialization):
#         self.ho=hospital
#         self.sp=specialization
#         print("hospital name =",self.ho,"\n""specialization =",self.sp)
# ob=developer()
# ob.fun_det(555,"vishnu","male")
# ob.fun_dev("developer","tcs")
# print()
# ob=doctor()
# ob.fun_det(555,"vishnu","male")
# ob.fun_doc("applo","skin")

class details:
    def __init__(self,id,name,gender):
        self.id=id
        self.nm=name
        self.g=gender
        print("id =",self.id,"\n""name =",self.nm,"\n""gender =",self.g)
class developer(details):
    def __init__(self,id,name,gender,designation,company):
        details.__init__(self,id,name,gender)
        self.des=designation
        self.com=company
        print("designation =",self.des,"\n""company name =",self.com)
class doctor(details):
    def __init__(self,id,name,gender,hospital,specialization):
        details.__init__(self, id, name, gender)
        self.ho=hospital
        self.sp=specialization
        print("hospital name =",self.ho,"\n""specialization =",self.sp)
ob=developer(55,"vishnu","male","developer","tcs")
print()
ob1=doctor(55,"vishnu","male","appllo","skin")