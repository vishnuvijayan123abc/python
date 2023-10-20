#it is same a list sequencial data type ,immutable
#iteration,count,len,element accessing tuple(),, is repersented using()
t=("a","b",1,1.2)
print(type(t))
# for i in t:
#     print(i)

# a=t.count("a")
# print(a)

# a=t[0]
# print(a)
#creat a turple input by the user
n=[]
a=int(input("enter the number"))
for i in range(a):
    e=input("enter the element")
    if e.isdigit():
        n.append(int(e))
    elif "." in e:
        n.append(float(e))
    else:
        n.append(e)

an=tuple(n)
print(an)
