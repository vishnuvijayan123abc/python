class a:
    def setval(self,name,salary):
        self.name=name
        self._sa=salary
        print("name:",self.name,"\n""salaey :",self._sa)
class b(a):
    def setval1(self):
        print(self.name)
        print(self._sa)
on=b()
on.setval("vishnu",55000)
on.setval1()
print("name=",on.name,"salasry=",on._sa)