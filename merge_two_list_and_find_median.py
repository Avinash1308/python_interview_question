list1=[1,3,5,7]
list2=[2,4,6,8]
combined_list=(list1+list2)
print(combined_list)
sorted_list=sorted(combined_list)
print(sorted_list)
length=len(sorted_list)
print(length)
print(length//2)
if(length%2==0):
  median=(sorted_list[length//2-1]+sorted_list[length//2])/2
else:
  median=sorted_list[length//2]
print(median)
# output
# 4.5
