arr=[1,2,3,4,5,9,6,7,8,]
ele=9
pos=-1
for i in range(len(arr)):
  if arr[i]==ele:
    pos=i
    break
if(pos==-1):
  print("element not found")
else:
  print("element found at position :  ",pos)
  
