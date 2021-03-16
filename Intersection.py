len_list1 = int(input("Range of first list:"))
list1 =[]
for i in range(0,len_list1):
    list1.append(int(input("enter element")))

len_list2 = int(input("Range of second list:"))
list2 =[]
for i in range(0,len_list2):
    list2.append(int(input("enter element")))
list3 = [i for i in list1 if i in list2]

print("Intersection of two lists",set(list3))