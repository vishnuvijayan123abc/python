import  re
# rule="[A-Za-z]+"
# word=input("enter your name")
# match=re.fullmatch(rule,word)
# if match:
#     print("valid name")
# else:
#     print("invalid name")

#name should starts with upper case then lower case ,space range should be in between 7-10
# rule="^[A-Z][a-z\s]{6,9}"
# word=input("enter your word")
# match=re.fullmatch(rule,word)
# if match:
#     print("valid name")
# else:
#     print("invalid name")


#the name should only starts with A,B OR C followd by lower cases number should be includd or not
# rule="^[ABC][a-z]+[0-9]*"
# word=input("enter your word")
# match=re.fullmatch(rule,word)
# if match:
#     print("valid name")
# else:
#     print("invalid name")
#phone number validation 10 numbers required it should stars with (9,8,7,6)
# rules="^[9876][0-9]{9}"
# number=input("enter your number")
# match=re.fullmatch(rules,number)
# if match:
#     print("valid")
# else:
#     print("invalid")

# rules="^[+][9][1][9876][0-9]{9}"
# number=input("enter your number")
# match=re.fullmatch(rules,number)
# if match:
#     print("valid")
# else:
#     print("invalid")

#
# rules="^[ABC][a-z]+([^0-9]|[0-9]{1,2})"
# word=input("enter your word")
# match=re.fullmatch(rules,word)
# if match:
#     print("valid name")
# else:
#     print("invalid name")

# rule="^[a-z]+[0-9]*[*_]?[a-z0-9]*[@][g][m][a][i][l][.][c][o][m]"
# word=input("enter your word")
# match=re.fullmatch(rule,word)
# if match:
#     print("valid name")
# else:
#     print("invalid name")

# rule=r"([0-9]{1,2}[-][0-9]{1,2}[-][0-9]{4}|[0-9]{1,2}[//][0-9]{1,2}[//][0-9]{4})"
# dob=input("enter your date of birth")
# match=re.fullmatch(rule,dob)
# if match:
#     print("valid")
# else:
#     print("invalid")
#registration nd login using regexlib
     #enter name
     #enter email
     #password
rule="[A-Za-z]+"
rule1="^[a-z]+[0-9]*[*_]?[a-z0-9]*[@][g][m][a][i][l][.][c][o][m]"
rule2="^[a-zA-Z]\w{3,14}$"
rule3="^[+][9][1][9876][0-9]{9}"
name=input("enter your name")
match=re.fullmatch(rule,name)
email=input("enter your email")
match1=re.fullmatch(rule1,email)
passw=input("enter your password")
match2=re.fullmatch(rule2,passw)
ph=input("enter your ph number")
match3=re.fullmatch(rule3,ph)
if match and match1 and match2 and match3:
    print("registration success")
    e = input("enter email")
    p = input("enter password")
    if e == email and p == passw:
        print("login success")
    else:
        print("login failed")
else:
    print("fail")









