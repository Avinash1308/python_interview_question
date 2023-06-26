list1=[1,"Apple",2,"banana",3,"cat"]
result=[item for item in list1 if not isinstance(item,int)]
print(result)
