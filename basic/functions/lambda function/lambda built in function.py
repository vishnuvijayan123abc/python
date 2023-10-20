#filter thta take a sequence as an arguments that will filter out all the elements in a sequence
#varible_name=list(filter(lambda arguments:expression,list_varible))
#write a lambda function to filter out even numbers from the given list
#li=[1,2,3,4,5,6,7,8,9,10]
# x=list(filter(lambda i:i%2==0,li))
# print(x)
# x=list(filter(lambda i:i%2!=0,li))
# print(x)
#from the given list find the numbers divisible by 13 but not by lambda
# li=[1,123,100,200,220,101,33,39,13]
# x=list(filter(lambda i:i%13==0 and i%3!=0,li))
# print(x)

#filter age between 18 and 50
# age=[12,34,28,2,50,22,1]
# x=list(filter(lambda i:i>18 and i<50,age ))
# print(x)

#mapping
#mapp function in python take a sequence as an argument and a new sequence is return ,it is a build in fuction allows you to
# #prosess and transforms all the items in an itertable list without a for loop

#varible_name=list(map(lambda argument:expression,list name))
#l=[1,2,3,4]
# x=list(map(lambda i:i**2,l ))
# print(x)

#find the square root of each elemnts in listx=list
# x=list(map(lambda i:i**0.5,l))
# print(x)
#creat a list from 1 to 10 enter user input
# li=[1,2,3,4,5,6,7,8,9,10]
# a=int(input("enter your value"))
# x=list(map(lambda i:i*a,li))
# print(x)

#map function using two list
# l=[1,2,3,4]
# l1=[5,6,7,8]
# x=list(map(lambda a,b:a+b,l,l1))
# print(x)

#creat the name of students and convert the first lettr to capital
# name=["vishnu vijayan","jhon wick"]
# x=list(map(lambda i:i.capitalize(),name))
# print(x)

#reduce
#a reduce function in python take a sequence as an argument and a new reduce result is return
#it is a function which belong to  funcction tool module,it is a python file with.py extentions

#how to import
from functools import reduce
#find the largest  element from the list using reduce
# l=[100,200,500,300,400]
# x=reduce(lambda a,b:a if a>b else b ,l)
# print(x)
#find the samllest element from the given list
# l=[2,1,3,5,7]
# x=reduce(lambda a,b:a if a<b else b,l)
# print(x)

#find the sum of elements using reduce
# li=[1,2,3,4,5,6]

# x=reduce(lambda a,b:a+b,li)
# print("sum of elements in list is", x)



#find the product of a number
# li=[5,7,9,11,13]
#
#
# x=reduce(lambda a,b:a*b,li)
# print("product is", x)