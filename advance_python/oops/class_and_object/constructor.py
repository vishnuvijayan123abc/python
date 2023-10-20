#__init__(),this method in python is a constructor in an object oreinted programming,it is called every time an object is creted
    #from a class,the method lets class to initilise the object attributes directly while creating a reffernce object

# class class_name:
#     def __init__(self,a,b):
#         print(a,b)
# ob=class_name(1,2)

#creat a class car with dinamic varibles name colour modele type engine
class car:
    def __init__(self,name,colour,modele,type):

             self.nm=name
             self.col=colour
             self.m=modele
             self.ty=type
             print("name =",self.nm,"\n""colour =",self.col,"\n""model =",self.m,"\n""type =",self.ty)
ob=car("volvo s90","black",2023,"sedan")
