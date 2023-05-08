s="reverse words in string"
s1=s.split()
for words in s1:
  for j in range(len(words)-1,-1,-1):
    print(words[j],end="")
  print(" ",end=" ")
