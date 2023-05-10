def selection_sort(num):
  for i in range(len(num)):
    minindex = i
    for j in range(i + 1, len(num)):
      if (num[minindex] > num[j]):
        minindex = j

    temp = num[minindex]
    num[minindex] = num[i]
    num[i] = temp


num = [1, 9, 6, 2, 7, 4, 8, 3, 5]
selection_sort(num)
print(num)
