#it is a data struture that follows fifio first in first out
#enqueu and dqueu
stack=[]
len=int(input("enter the length"))

t=0
def enqueu():
    global t
    if t==len:
        print("stack is full")
    else:
        e=int(input("enter the element"))
        stack.append(e)
        t+=1
        print(stack)
def dqueu():
    global t
    if t==0:
        print("stack is empty")
    else:
        stack.pop(0)
        t-=1
        print(stack)
while True:
    c=int(input("1 enqueu \t\t 2 dequeu"))
    if c==1:
        enqueu()
    elif c==2:
        dqueu()
    else:
        print("invalid")