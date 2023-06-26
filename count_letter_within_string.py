str="hello      model where are you    "
words=(str.split())
count=0;
for ele in words:
 for letter in ele:
   count+=1
print(count) 
#output
#21
