list1=[1,2,4,57,3]
min=min(list1)
max=max(list1)
all_numbers=set(range(min,max))
missing=all_numbers-set(list1)
print(missing)
