s=[]
len=int(input("enter the length "))
count=0
def enqueue():
    global count,s
    if count==len:
        print("full")
    else:
        element=input("enter the element")
        if element.isalpha():
            s.append(element)
            print(s)
            count+=1
        elif element.isdigit():
            s.append(int(element))
            print(s)
            count+=1
        elif "*" in element:
            s.append(float(element))
            print(s)
            count+=1
def dequeue():
    global count
    if count==0:
        print("empty")
    else:
        s.pop(0)
        print(s)
        count-=1
while True:
    option=int(input("(1) enqueue \t (2) dequeue \n enter your optiomn:"))
    if option==1:
        enqueue()
    elif option==2:
        dequeue()
    else:
        print("invalid")