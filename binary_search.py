def binary_search(numbers,ele):
  start=0
  end=len(numbers)-1
  while(start<=end):
    mid=(start+end)//2
    if(numbers[mid]==ele):
      return mid
    if(numbers[mid]>ele):
      end=mid-1
    if(numbers[mid]<ele):
      start=mid+1
numbers=[1,2,3,4,5,8,9]
ele=8
print(binary_search(numbers,ele))
