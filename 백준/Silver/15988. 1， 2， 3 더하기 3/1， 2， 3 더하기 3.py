def solution(num):
  for _ in range(len(d), num + 1):
    d.append((d[-3] + d[-2] + d[-1])% 1000000009)
  print((d[num - 1]) )

d = [1,2,4,7]
n = int(input())
for _ in range(n):
  num = int(input())
  solution(num)