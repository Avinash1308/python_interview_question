arr=[22097,89,46,876,3423,79,4556]
small=arr[0]
    
for i in range(len(arr)):
  if small>arr[i]:
    small=arr[i]
print(small)
