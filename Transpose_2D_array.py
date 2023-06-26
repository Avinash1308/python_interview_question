def arr_transpose(arr):
  transpose=[ list(row) for row in zip(*arr)]
  return transpose
arr=[[1,2,3],
    [4,5,6],
    [7,8,9]]
print(arr_transpose(arr))



# another way
def array_transpose(arr):
  row=len(arr)
  column=len(arr[0])
  transpose=[[0 for _ in range(row)] for _ in range(column)]
  for i in range(row):
    for j in range(column):
      transpose[j][i]=arr[i][j]
  return transpose

arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]
print(array_transpose(arr))
