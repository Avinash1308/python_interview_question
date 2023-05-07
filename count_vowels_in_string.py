arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
s="program to find number of vowels present in string"
count=0
for i in range(len(arr)):
  for j in range(len(s)):
    if arr[i]==s[j]:
      count+=1
print("number of vowels present in string : ",count)
