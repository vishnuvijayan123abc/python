#encapusulation is one of the fundamental consept in oops
#it describes the ide of wrping data and method
#this put restriction on accesing varible and data
#it can prevent the accidentl modification data

#access modifiers
#it is used to modifie the limts of accessing the varible function of class
#public acess:can use anywher in function
#private access:access with in the class
#protected:whith in the class and its sub class

class employee:
    def __init__(self,name,project,salary):
        self.nm=name
        self._pr=project #protrcted
        self.__sl=salary #private