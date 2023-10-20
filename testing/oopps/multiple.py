class father:
    def fun_f(self,fname,faddress):
        self.fname=fname
        self.fadd=faddress
        print("father name =",self.fname)
        print("address =",self.fadd)
class mother:
    def fun_m(self,mname):
        self.m=mname
        print("mother name =",self.m)
class son(father,mother):
    def s_fun(self,son_name):
        self.sname=son_name
        print("son name =",self.sname)
ob=son()
ob.fun_f("arjun","aluva")
ob.fun_m("anju")
ob.s_fun("arun")