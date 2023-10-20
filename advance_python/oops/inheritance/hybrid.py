#it is a combination of different types of inheritance
# class parent:
#     def fun(self):
#         print("parent")
# class child(parent):
#     def fun1(self):
#         print("child")
# class child1(parent):
#     def fun2(self):
#         print("child1")
# class child2(child,child1):
#     def fun3(self):
#         print("child2")
#
# ob=child2()
# ob.fun()
# ob.fun1()
# ob.fun2()
# ob.fun3()

#university(univ_name,location)
#collage(collage name)
#course(course_nme)
#student(roll_no,name)

# class universtity:
#     def fun(self,uni_name,location):
#         self.unam=uni_name
#         self.lc=location
#         print("university name =",self.unam,"\n""location =",self.lc)
# class college(universtity):
#     def cl_fun(self,collagenm):
#         self.cnam=collagenm
#         print("college name =",self.cnam)
# class course(universtity):
#     def curs(self,course_name):
#         self.crnam=course_name
#         print("course name =",self.crnam)
# class student(college,course):
#     def stud(self,roll,studname):
#         self.roll=roll
#         self.stud=studname
#         print("roll no =",self.roll,"\n""student name =",self.stud)
# ob=student()
# ob.fun("mg","kottyam")
# ob.cl_fun("skcms")
# ob.curs("bcom")
# ob.stud(12,"vishnu")
class univers:
    def __init__(self,uni_name,location):
        self.uninam=uni_name
        self.lc=location
        print("university name =", self.uninam, "\n""location =", self.lc)
class college(univers):
    def __init__(self,uni_name,location,college_name):
        univers.__init__(self,uni_name,location)
        self.clgnam=college_name
        print("college name =",self.clgnam)
class course(univers):
    def __init__(self,uni_name,location,course_name):
        univers.__init__(self,uni_name,location)
        self.crnam=course_name
        print("course =",self.crnam)
class student(college,course):
    def __init__(self,uni_name,location,college_name,course_name,roll,name):

        college.__init__(self,uni_name,location,college_name)
        course.__init__(self,uni_name,location,course_name)
        self.ro=roll
        self.stunam=name
        print("roll number=",self.ro,"\n""name =",self.stunam)
ob=student("mg","kottyam","skcms","bcom",24,"vishnu")

