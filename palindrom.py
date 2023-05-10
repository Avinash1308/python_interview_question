def palindrom_num(num):
  temp=num
  rev=0
  while(temp>0):
    digit=temp%10
    rev=(rev*10)+digit
    temp//=10
  return rev
num=121
result=palindrom_num(num)
if(num==result):
  print("it is palindrom")
else:
  print("not palindrom")
  
