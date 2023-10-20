# class a:
#     def fun_a(self):
#         print("hello")
# class b(a):
#     def fun_b(self):
#         print("hai")
# class c(b):
#     def fun_c(self):
#         print("bye")
# ob=c()
# ob.fun_c()
# ob.fun_b()
# ob.fun_a()


#mobile(storage and colour)
#samsung(ram)
#samsung s2(speed)

# class mobile:
#     def fun_mobile(self,storage,colour):
#         self.stor=storage
#         self.col=colour
#         print("storage =",self.stor)
#         print("colour =",self.col)
# class samsung(mobile):
#     def fun_s(self,ram):
#         self.r=ram
#         print("ram=",self.r)
# class s23(samsung):
#     def fun_s23(self,made):
#         self.mad=made
#         print("made =",self.mad)
# ob=s23()
# ob.fun_mobile(128,"black")
# ob.fun_s(8)
# ob.fun_s23("us")

class car:
    def __init__(self,wheel,color):
        self.wh=wheel
        self.cl=color
        print("wheel size =",self.wh,"\n""color =",self.cl)
class maruthi(car):
    def __init__(self,wheel,color,model):
        car.__init__(self,wheel,color)
        self.mod=model
        print("model =",self.mod)
class maruthi800(maruthi):
    def __init__(self,wheel,color,model,price):
        maruthi.__init__(self,wheel,color,model)
        self.pr=price
        print("price =",self.pr)

ob=maruthi800(13,"black",2015,250000)