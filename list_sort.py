list1=[1,4,3,5,2]
list1.sort()
print(list1)




# using for loop
list1=[1,4,3,5,2]
def sort(list1):
  n=len(list1)
  for i in range(n):
    for j in range(i+1,n):
      if list1[i]>list1[j]:
        list1[i],list1[j]=list1[j],list1[i]
sort(list1)
print(list1)
