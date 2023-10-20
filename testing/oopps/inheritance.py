# class car:
#     def br(self,name):
#         self.nm=name
#         print("brand =",self.nm)
# class cars(car):
#     def md(self,name):
#         self.nm=name
#         print("modle=",self.nm)
# ob=cars()
# ob.br("bmw")
# ob.md("x1")

#constructor
# class car:
#     def __init__(self,name):
#         self.nm=name
#         print("brand =",self.nm)
# class cars(car):
#
#     def __init__(self,name,modle):
#         super().__init__(name)
#         self.m=modle
#         print("modle =",self.m)
# ob=cars("bmw","5 series")

class phone:
    brand="iphone"
    def __init__(self,made):
        self.md=made
        print("brand =",phone.brand)
        print("made =",self.md)
class phones(phone):
    def __init__(self,made,model,storage):
        super().__init__(made)
        self.mo=model
        self.st=storage
        print("brand =",phone.brand)
        print("made =",self.md,"\n""model =",self.md,"\n""storage =",self.st)

ob=phones("us","12pro","128")
