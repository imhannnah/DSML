list1=[10,34,4,5,34,4,4,68]
print("old list:",list1)
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print("elements in newlist:",list2)
