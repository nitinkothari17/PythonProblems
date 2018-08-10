a = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]

d1 = 0
d2 = 0 
length = len(a)

for i in range(length):
  d1 +=  a[i][i]
  d2 +=  a[i][length-i-1]
  
print (diagonal_sum_1,diagonal_sum_2)
