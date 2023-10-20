s=[]
len=int(input("enter the length of a list"))
count=0

def push():
    global count,s
    if count==len:
        print("stack is full")
    else:
        el=input("enter the element")
        if el.isdigit():
            s.append(int(el))
            print(s)
            count+=1
        elif el.isalpha():
            s.append(el)
            print(s)
            count+=1
        elif "." in el:
            s.append(float(el))
            print(s)
            count+=1
def pop():
    global count
    if count==0:
        print("stack is empty")
    else:
        s.pop()
        count-=1
        print(s)
while True:
    op=int(input("(1) push \t\t (2) pop \n enter your option:"))
    if op==1:
        push()
    elif op==2:
        pop()
    else:
        print("invalid")



