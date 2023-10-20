#it is a function that is used to check a thread is alive or not if alive it return true otherwise false
#it is a function that is used to customize thread name
from threading import *
import time
def cube(a):
    print("calculate cube")
    for i in a:
        time.sleep(3)
        print("cube =",i**3,current_thread().name,t1.is_alive())
def sqr(a):
    print("calculate square")
    for i in a:
        time.sleep(1)
        print("sqr =",i**2,current_thread().name,t2.is_alive())
li=[1,2,3,5,6,4]
t1=Thread(target=cube,args=(li,))
t1.setName("first_thread")
t2=Thread(target=sqr,args=(li,))
t2.setName("second_thread")
t1.start() #function that is used to star each thread in a process
t2.start()
t1.join()
t2.join()
print(t1.is_alive(),t2.is_alive())
print("this is a multi thread ",current_thread().name)
#join : this function is used to wait the child thread to complete its excution