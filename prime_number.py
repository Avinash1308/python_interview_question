num=37
if num>0:
  for i in range(2 ,int(num/2)+1):
    if(num%i==0):
      print("not prime")
      break
  else:
    print('prime')
else:
    print( 'not prime')
    
    
    
    
 // another aproach
num=18
prime=True
for i in range(2,int(num/2)+1):
  if(num%i==0):
    prime=False
    break
if(prime):
  print('it is prime number')
else:
  print('not prime number')
