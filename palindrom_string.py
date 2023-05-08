s="nitin nitin aw"
if (s==s[::-1]):
  print("palindrom")
else:
  print("not palindrom")


  
  
  
  
// another approach
s="nitin liil liil nitin "
rev=""
for i in s:
  rev=i+rev

if(s==rev):
  print("palindrom")
else:
  print("not palindrom")
  
