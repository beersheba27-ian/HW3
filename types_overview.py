# sequence[start:stop:step]
# start - index "from" inclusive
# stop - index "to" exclusive
# step - step for sequence
# built-in Python sequence types: range, list, string
str = "Hello"
print(str[1]) #e
print(str[1:3]) #el
print(str[1:3:-1]) #empty
print(str[-1]) #o
print(str[-1:3]) #empty
print(str[0:5:1]) #sequence copy
print (str[::-1]) #sequence reversed copy
print (list(range(20)[::-1]))