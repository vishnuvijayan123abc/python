from threading import *

#current _thread.name  : this function is used to get the name current working thread of a process
#main thread :its called a single thread in which a process that excute in a single thread durring the runnig of a program
def cube(a):
    print("calculate cube")
    for i in a:
        print("cube =",i**3,current_thread().name)
def sqr(a):
    print("calculate square")
    for i in a:
        print("sqr =",i**2,current_thread().name)

li=[1,2,3,5,6,4]
cube(li)
sqr(li)