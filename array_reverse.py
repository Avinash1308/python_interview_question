for(int j=1;j<=n-i;j++){
        System.out.print(' ');
      }



# using for loop
arr=[1,2,3,4,5,6,7]
for i in range(len(arr)):
  for j in range(i,len(arr)):
    arr[i],arr[j]=arr[j],arr[i]
print(arr) 

// using slicing
arr=[1,2,3,4,5,6,7]
print(arr[::-1])
