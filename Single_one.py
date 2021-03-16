len_list1 = int(input("Mention the range of list:"))
list1 =[]
for i in range(0,len_list1):
    list1.append(int(input("enter element")))
single = 0
for i in range(0,len_list1):
    single = single^list1[i]
print("single element: ",single)