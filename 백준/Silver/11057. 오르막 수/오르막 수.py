N = int(input())

d = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]

for i in range(1, N):
  a = []
  for j in range(0, 10):
    gun = 0
    for k in range(j, 10):
      gun += d[i - 1][k]
    a.append(gun)
  d.append(a)
print((d[N - 1][0]) % 10007)