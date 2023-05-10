numbers=[1,4,2,8,3,4,9,7,5,6]
for i in range(len(numbers)):
  for j in range(i+1,len(numbers)):
    if(numbers[i]>numbers[j]):
      numbers[i],numbers[j]=numbers[j],numbers[i]
print(numbers)
