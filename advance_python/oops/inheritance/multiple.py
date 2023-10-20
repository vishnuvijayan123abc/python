# class a:
#     def fun1(self):
#         print("class a")
# class b:
#     def fun2(self):
#         print("class b")
# class c(a,b):
#     def fun3(self):
#         print("class c")
# ob=c()

# ob.fun3()
# ob.fun1()
# ob.fun2()
#
#
#
# class father:
#     def fun_f(self,fname,faddress):
#         self.fname=fname
#         self.fadd=faddress
#         print("father name =",self.fname)
#         print("address =",self.fadd)
# class mother:
#     def fun_m(self,mname):
#         self.m=mname
#         print("mother name =",self.m)
# class son(father,mother):
#     def s_fun(self,son_name):
#         self.sname=son_name
#         print("son name =",self.sname)
# ob=son()
# ob.fun_f("arjun","aluva")
# ob.fun_m("anju")
# ob.s_fun("arun")
#
#
# class father:
#     def __init__(self,fname):
#         self.f=fname
# class mother:
#     def __init__(self,mname):
#         self.mname=mname
# class son(father,mother):
#     def __init__(self,fname,mname,sname):
#         father.__init__(self,fname)
#         mother.__init__(self,mname)
#         self.s=sname
#         print("father name=",self.f)
#         print("mother name =",self.mname)
#         print("son name =",self.s)
# ob=son("aru","anu","aju")

# class company:
#     def __init__(self,company_name,location):
#         self.cmname=company_name
#         self.lc=location
# class team:
#     def __init__(self,leadername,department):
#         self.tname=leadername
#         self.dep=department
# class employee(company,team):
#     def __init__(self,company_name,location,leadername,department,empname,desig,salary):
#         company.__init__(self,company_name,location)
#         team.__init__(self,leadername,department)
#         self.enmae=empname
#         self.d=desig
#         self.sa=salary
#         print("company name =",self.cmname,"\n""location =",self.lc)
#         print("leader name =",self.tname,"\n""department =",self.dep)
#         print("employee name =",self.enmae,"\n""desigination =",self.d,"\n""salary =",self.sa)
# ob=employee("tcs","kochi","rahul","r and d","vishnu","dep",55000)