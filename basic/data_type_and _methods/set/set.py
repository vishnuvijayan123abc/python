#unodered data type,iteratable,set unindexed,duplication not allows ,{},mutable
# s={"a","b","c"}
# print(s)
# print(len(s))
# print(type(s))

#find the len of a set
# c=0
# for i in s:
#     c+=1
# print(c)
#add method
# s.add("k")
# print(s)
#creat a empty set and elements into the set
# s=set({})
# a=int(input("enter number"))
# for i in range(a):
#     h=input("enter your data")
#     s.add(h)
# print(s)

# li=["a","a","b","c","c"]
# s=set(li)
# a=list(s)
# a.sort()
# print(a)

#update method
# li={"a","b","c"}
# l2=["j","s",1]
# li.update(l2)
# print(li)


#remove method
# li={"a","b","c"}
# li.remove("a")
# print(li)
# li.discard("c")
# print(li)
# li.pop()
# print(li)

#do u want to remove element from the set

# s={"a","b","c"}
# k=len(s)
# for i in range(k):
#     d=input("do u want to remove element from the set")
#     if d=="yes":
#         f=input("enter the element to remove")
#         s.remove(f)
#
#     elif d=="no":
#         break
#
#     print(s)

#break is a keyword that is used to stop the excution of your pgrm
#continue



#intersection update method
#the method that is used to keep the elements same in the sets
# x={"a","b","c"}
# y={"c","b","k"}


# s={"a","b","c"}
# for i in range(len(s)):
#     a=input("do u want to remove element")
#     if a=="yes":
#         j=input("enter the element to remove")
#         s.remove(j)
#         print(s)
#     elif a=="no":
#         break

# a=["a","a","a","b","c","c"]
# b=set(a)
# h=(list(b))
# h.sort()
# print(h)

#intersection
# x={"a","b","c"}
# y={"d","e","a"}
# x.intersection_update(y)
# print(x)
#symentric intersection update
# x.symmetric_difference_update(y)
# print(x)