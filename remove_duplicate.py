list1=[1,2,3,4,5,3,2,6,7,5,8,9]
result=set(list1)
print(list(result))


# another approach
list1=[1,2,3,4,5,3,2,6,7,5,8,9]
list2=[]
for i in list1: 
  if i not in list2:
    list2.append(i )
print(list2)
