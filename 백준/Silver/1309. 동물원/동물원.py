N = int(input())

d = [[1,2]]

for i in range(1, N + 1):
  a = [(sum(d[i-1])) % 9901, ((d[i-1][0]) * 2 + d[i-1][1]) % 9901]
  d.append(a)

print(sum(d[N - 1]) % 9901)
