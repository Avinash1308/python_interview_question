list1=[9,5,8,6,7,1,2,3,5]
print(sorted(list1[::-1]))


# another
list1=[9,5,8,6,7,1,2,3,5]
list1.reverse()
print(list1)

# another one approach
list1=[9,5,8,6,7,1,2,3,5]
reverse_list=[]
for i in range(len(list1)-1,-1,-1):
  reverse_list.append(list1[i])
print(reverse_list)



