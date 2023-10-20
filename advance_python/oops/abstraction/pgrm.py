#the process of handling complexity by handling unnecessary information from user
#this is one of the core concept of oops
from abc import ABC,abstractmethod
# class vechile(ABC):
#     @abstractmethod
#     def wheel(self):
#         pass
#     @abstractmethod
#     def door(self):
#         pass
# class car(vechile):
#     def wheel(self):
#         print("4 wheels")
#     def airbag(self):
#         print("have airbag")
#     def door(self):
#          print("4 doors")
#
#
# ob=car()
# ob.wheel()
# ob.airbag()
# ob.door()


class animal:
    @abstractmethod
    def eye(self):
        pass
    @abstractmethod
    def skin(self):
        pass
class elephant(animal):
    def eye(self):
        print("elephant have black eye")
    def skin(self):
        print("black colour skin")
    def teeth(self):
        print("have 26 teeth")
class lion (animal):
    def eye(self):
        print("lion have brown eyes")
    def skin(self):
        print("light brown skin colour")
    def teeth(self):
        print("30 teeth")
ob=elephant()
ob.skin()
ob.eye()
ob.teeth()
print()
ob1=lion()
ob1.eye()
ob1.teeth()
ob1.skin()