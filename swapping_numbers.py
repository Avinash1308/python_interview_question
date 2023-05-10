n1=10
n2=20
print(f"before swapping numbers are  n1 is : {n1} and n2 is  {n2} ")
temp=n1
n1=n2
n2=temp
print(f"after swapping numbers are  n1 is : {n1} and n2 is  {n2} ")





# another way                      it is also without using third variable
n1=10
n2=20
print(f"before swapping numbers are  n1 is : {n1} and n2 is  {n2} ")
n1,n2=n2,n1
print(f"after swapping numbers are  n1 is : {n1} and n2 is  {n2} ")



# without using third variable  
n1=10
n2=20
print(f"before swapping numbers are  n1 is : {n1} and n2 is  {n2} ")
n1=n1+n2
n2=n1-n2
n2=n1-n2
print(f"after swapping numbers are  n1 is : {n1} and n2 is  {n2} ")
