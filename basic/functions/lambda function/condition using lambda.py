#find the square of a number if the number which is greater thn zero
# x=lambda a:a**2 if a>0 else None
# print(x(5))
#find a number is negative or positive
# x=lambda a:"posstive" if a>0 else "negative"
# print(x(5))
#find the largest of two numbers using lambda
# x=lambda a,b:a if a>b else b
# print(x(1,2))
#conver a postive number to a negative and negative to postive
# x=lambda a:a*-1 if a>0  else -a*1
# a=int(input("enter nymber"))
# print(x(a))
#find a number is odd or even
# x=lambda a:"even" if a%2==0 else "odd"
# print(x(5))



#elif

#write a pgrm to find largest of three numbers
# x=lambda a,b,c:a if a>b and a>c else(b if b>c else c)
# print(x(1,2,3))

#find the smallest of 3 number input ny the user
# x=lambda a,b,c:a if a<b and a<c else(b if b<c else c)
# a=int(input("enter a"))
# b=int(input("enter b"))
# c=int(input("enter c"))
# print(x(a,b,c))

#find a nuber is possitive negative zero
# x=lambda a:"possitive" if a>0 else("zero" if a==0 else "negative" )
# print(x(0))

# la=lambda a,b,c,d:a if a>b and a>c and a>d else(b if b>c and b>d else(c if c>d else d) )
# print(la(1,2,3,4))


#accept the age of 4 people and display the youngest one
# x=lambda a,b,c,d:"%d is youngest"%a if a<b and a<c and a<d else("%d is youngest"%b if b<c and b<d else("%d is youngest"%c if c<d else "%d is youngest"%d) )
# a=int(input("enter age of a"))
# b=int(input("enter age of b"))
# c=int(input("enter age of c"))
# d=int(input("enter age of d"))
# print(x(a,b,c,d))
