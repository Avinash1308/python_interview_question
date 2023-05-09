def prime_recursion(num,divisor=2):
  if num<2:
    return False
  if num==2 or num==3:
    return True
  if num%divisor==0:
    return False
  if divisor*divisor>num:
    return True
  return prime_recursion(num,divisor+1)
a=prime_recursion(23)
print(a)
                 
