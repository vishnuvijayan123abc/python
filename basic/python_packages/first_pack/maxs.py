def add(*a):
    sum=0
    for i in a:
         sum+=i
    return (sum)
def numrev(a):
    c=str(a)
    c=a[::-1]
    b=int(a)
    return b
def rev(a):
    a=a[::-1]
    return (a)
def amstrg(a):
    sum=0
    temp=a
    while a!=0:
        d=a%10
        sum+=d**3
        a//=10
    if temp==sum:
       return("yes %s is a armstrong number"%temp)
    else:
        return("no %s is not a armstrong number"%temp)

