from threading import *
import time

class hello(Thread):
    def __init__(self,a,b):
        Thread.__init__(self)
        self.a=a
        self.b=b
    def run(self):
        print(self.a+self.b,current_thread().name)
class mup(Thread):
    def __init__(self,a,b,c):
       Thread.__init__(self)
       self.a=a
       self.b=b
       self.c=c
    def run(self):
        for i in range(3):

            print(self.a*self.b*self.c,current_thread().name)

#run mthod is the entry point for a thread

t1=hello(1,2)
t2=mup(2,3,4)
t1.start()
t2.start()
t1.join()
t2.join()
print(current_thread().name),