brackets = input("enter the string of brackets: ")
dict1 = {'}':'{',']':'[',')':'('}
set1 = '({['
set2 = ')]}'
temp =[]
for char in brackets:
    if char in set1:
        temp.append(char)
    elif char in set2:
        if temp[-1]==dict1[char]:
            temp.pop()
if len(temp)==0:
    print("Valid")
else:
    print("Invalid")