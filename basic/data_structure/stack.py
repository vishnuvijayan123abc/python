# stk=[]
# size=int(input("enter the number of elements : "))
# top=0
# def push():
#     global top  #it is a key woard that is used to chang the global value
#     if top==size:
#         print("stack is full")
#     else:
#         el=int(input("enter the element"))
#         stk.append(el)
#         top+=1
#         print(stk)
# def pop():
#     global top
#     if top==0:
#         print("stack is empty")
#     else:
#         stk.pop()
#         top-=1
#         print(stk)
#
# while True:
#     choise=int(input("1 push function \t\t 2 pop"))
#     if choise==1:
#         push()
#     elif choise==2:
#         pop()
#     else:
#         print("invalid")



s=[]
l=int(input("enter th length "))
c=0
def push():
    global c
    if c==l:
        print("stack is full")
    else:
        e=int(input("enter the element"))
        s.append(e)
        c+=1
        print(s)
def pop():
    global c
    if c==0:
        print("stack is empty")
    else:
        s.pop()
        c-=1
        print(s)
while True:
    choise=int(input("1 push \t\t 2 pop"))
    if choise==1:
        push()
    elif choise==2:
        pop()
    else:
        print("invaliid")