# 1) full match():it returns true if match found
# 2) search(): it returns match objects
# 3)findall():it returns list contain all match
# 4)split: it returns a string has been split
# 5)sub():it is used to replace the matches

# a regular expression is created using mix of characters special sequence and set
#[] : it repersent a set of characters
#\  : it repersenrt special sequence
# ^ : it repersent pattern present at the beginning of a string
# * : it repersent zero or more occurance
# +  : it repersent 1 or more occurance
#{}  : specified number of occrance of pattern
# | (or) : it repersent this or that characters is present


#rules o f regulare exprssion
# x="[abc]" : either a,b or c
# x="[^abc]": except abc
# x="[a-z]": lower case a-z
# x="[A_Z]": upper case A_Z
# x="[a-zA-Z]": both lower case and upper case
# x="[0-9]": it checks the digit
# x="[a-zA-Z0_9]": lower case upper case or digit


#special sequence:
# x="\s": check space
# x="\d": check digit
# x="\D": it returns string except number
# x="\w": it returns a string contains a word



#quantifiers:
# x="[a]+":it includes one or more
# x="[a]*": zero or more
# x="[a]?": a included or not included
# x="[a]{n}": n>number of times
# x=[a]{n,k}: n min number k max number

