numbers=[19,53,61,28,30,9]
print(max(numbers))                   #output 61



#another approach
numbers=[19,53,61,28,30,9]
max=numbers[0]
for i in range(len(numbers)):
  if max<numbers[i]:
    max=numbers[i]
    
print(max)                     #output 61




# another way
def max_in_arr(numbers):
  return max(numbers)
  
  

numbers=[19,53,61,28,30,9]
print(max_in_arr(numbers))
