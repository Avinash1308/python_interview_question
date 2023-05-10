n=5
spaces=n-1
star=1
for i in range(1,n+1):
  for j in range(spaces):
    print(' ',end="")
  for j in range(star):
    print('*',end="")
  print()
  spaces-=1
  star+=2
   
