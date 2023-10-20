#it is aa collecton of key value pairs,it is unindexing,mutable,{} duplication is not possible

#syntax
#dic={"key":"value","key1":"value1","key2":"value2"}

# person={"name":"vishnu",
#         100:200,
#         "address":"kochi",
#         "phone":98478455
#         }
# print(person)
# print(type(person))

#access key from dict
# print(person.keys())
# print(person.values())

#get function

# a=person.get("name")
# print(a)
# b=person["phone"]
# print(b)
#
#
# z=input("enter the key")
# print(person.get(z))
# print(len(person))

#update method
# person.update({"pin":556})
# print(person)
# person.update({"name":"jhon"})
# print(person)
# h=input("enter the key")
# j=input("enter the value")
# person.update({h:j})
# print(person)

# person["name"]="jhon wick"
# person["place"]="ekm"
# print(person)


#pop method
# person.pop(100)
# print(person)
#
# person.popitem()
# print(person)

#dictionary itteration
# for i in person.values():
#          print(i)
# for i,j in person.items():
#         print(i,j)


#creat a dict using user input
# h={}
# n=int(input("enter number of keys"))
# for i in range(n):
#         key=input("enter the key")
#
#         value=input("enter the value")
#         if value.isdigit():
#           h.update({key:int(value)})
#         elif "." in value:
#             h.update({key:float(value)})
#         else:
#             h.update({key:value})
# print(h)




# j={}
# h=int(input("enter the value"))
# for i in range(h):
#         k=input("enter the key value")
#         v=input("enter the value")
#         if v.isdigit():
#                 j.update({k:int(v)})
#         elif "." in v:
#                 j.update({k:float(v)})
#         else:
#                 j.update({k:v})
# print(j)