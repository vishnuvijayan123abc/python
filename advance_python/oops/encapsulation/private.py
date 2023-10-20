class employee:
    def __init__(self,name,salary):
        self.na=name
        self.__sa=salary
    def prinval(self):
        print("name:",self.na,"\n""salary:",self.__sa)
ob=employee("vishnu",55000)
ob.prinval()
print("name:",ob.na,"\n""salary:",ob._employee__sa)



#method to access private data and method outside the class

#name mangling:using public method
# _classname__datamember