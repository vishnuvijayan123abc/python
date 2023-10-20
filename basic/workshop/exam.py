#append
# li=[1,2,3,4]
# li.append("hello")
# print(li)
#insert function
# li.insert(2,"bye")
# print(li)
# li=[1,2,3,4,5]
# p=int(input("enter the position"))
# data=input("enter the data")
# if data.isdigit():
#     li.insert(p,int(data))
# elif data.isalpha():
#     li.insert(p,data)
# elif "." in data:
#     li.insert(p,float(data))
# print(li)
#extend
#li=[1,2,3]
# li.extend(["abc","c",11])
# print(li)
#pop
# li=[1,2,3,4,5,6]
# li.pop(2)
# print(li)
#remove
# li=["hello",1,2,3,5]
# li.remove("hello")
# print(li)
#reverse
# li=[1,2,3,4,5,6]
# li.reverse()
# print(li)
#count
# li=[1,2,3,4,5,5,6,6,6,6,6]
# a=li.count(5)
# print(a)
# c=0
# for i in li:
#     if i==6:
#         c+=1
# print(c)
#sort
# li=["a","b","z","d"]
# li.sort()
# print(li)
# li.sort(reverse=True)
# print(li)

#length
# li=[1,2,3,4,5,6,7,8,9]
# print(len(li))
# c=0
# for i in li:
#     c+=1
# print(c)


#element accessing
# li=[1,2,3,4,5,6,7,8,9]
# a=li[2]
# print(a)

#slicing
# a=li[2:5:2]
# print(a)


# class student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#         print(self.id)
# std=student("simon",1)
# std.id=2
# print(std.id)

# class people():
#     def __init__(self,name):
#         self.name=name
#     def nameprint(self):
#         print(self.name)
# p1=people("sally")
# p2=people("louise")
# p1.nameprint()
print(1,": kochi",2,"aluva",3,"angamaly")
a=int(input("select your location"))
if a==1:
    print("kochi")
    print(1,"pvr lulu",2,"cenipol")
    b=int(input("select your theater"))
    if b==1:
        print("pvr lulu kochi")
        print(1,"2018",2,"jhon wick")
        c=int(input("select film"))
        if c==1:
            print(1,"to confirm",2,"cancel")
            e=int(input("enter your choise"))
            if e==1:
                print("ticket confirm")
            else:
                print("canceled")


