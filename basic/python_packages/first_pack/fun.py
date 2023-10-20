def chrlen(a):
    count=0
    for i in a:
        if " " not in i:
            count+=1
    return(count)

def upper(a):
    count=0
    for i in a:
        if i.isupper():
            count+=1
    return(count)
def lower(a):
    count=0
    for i in a:
        if i.islower():
            count+=1
    return(count)
def rev(a):
    a=a[::-1]
    return (a)






