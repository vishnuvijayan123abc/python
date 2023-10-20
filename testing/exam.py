marks=0
print("who won highest run in ipl \n (1) sachin \t (2) virat \t (3) cris gale")
a1=int(input("enter your choise"))
if a1==2:
    print("correct answer")
    marks+=10
else:
    print("wrong answer")
    marks-=2
print("which state is the capital of india \n (1) kerala \t (2) goa \t (3) delhi")
a2=int(input("enter your choise"))
if a2==3:
    print("correct answer")
    marks+=10
else:
    print("wrong answer")
    marks-=2

print("your mark is",marks)