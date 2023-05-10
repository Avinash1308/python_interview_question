def palindrom_num(num):
  temp=num
  res=0
  while(temp>0):
    digit=temp%10
    res=res+digit**3
    temp//=10
  return res
num=153
result=palindrom_num(num)

if(num==result):
  print("it is armstrong")
else:
  print("not armstrong")
  
