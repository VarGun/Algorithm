n = int(input())
dic = {}
arr = list(map(int, input().split()))

d = [0] * (n + 1)
for i in range(n):
  dic[i + 1] = arr[i]
d[1] = dic[1]
for i in range(2, n + 1):
  max = dic[i]
  for j in range(1, i // 2 + 1):
    if(max < d[j] + d[i - j]):
      max = d[j] + d[i - j]
  d[i] = max

print(d[n])