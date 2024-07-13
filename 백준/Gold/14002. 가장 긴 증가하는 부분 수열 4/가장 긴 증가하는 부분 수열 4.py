import copy

n = int(input())
arr = list(map(int, input().split()))
p_i = [-1 for _ in range(n)]


d = [1] * n
for i in range(1, n):
  for j in range(i):
    if(arr[i] > arr[j]):
      if(d[i] < d[j] + 1):
        d[i] = d[j] + 1
        p_i[i] = j

max_l = max(d)
max_i = d.index(max_l)

arr_lis = []

for _ in range(max_l):
  arr_lis.append(arr[max_i])
  max_i = p_i[max_i]

arr_lis.reverse()
print(max_l)
print(*arr_lis)