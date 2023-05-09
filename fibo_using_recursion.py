def fabo(num):
  if num<0:
    return -1
  elif (num==0 or  num==1):
    return num
  else:
    return fabo(num-1)+fabo(num-2)
num=5
for i in range(num):
  print(fabo(i))
