li="welcome hai bye"
longest=max(li.split(),key=len)
print("longest word is",longest,"\n""length is ",len(longest))

print()
s="hai"
print(s)
for i in s:
    if s.index(i)%2==0:

        print(i,end="")

print()
print()
li=["hai","bai","hello"]
dic={}
for i in li:
    h=i
    j=li.index(i)
    dic.update({h:j})
print(li)
print(dic)


print()



s="hello"
ns=s[-1]+s[1:-1]+s[0]
print(s)
print(ns)
