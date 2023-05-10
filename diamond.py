n=5
spaces=n-1
star=1
for i in range(n):
  for j in range(spaces):
    print(' ',end="")
  for j in range(star):
    print('*',end="")
  print()
  spaces-=1
  star+=2
spaces=1
star=n*2-3
for i in range(n):
  for j in range(spaces):
    print(' ',end="")
  for j in range(star):
    print('*',end="")
  print()
  spaces+=1
  star-=2

  
