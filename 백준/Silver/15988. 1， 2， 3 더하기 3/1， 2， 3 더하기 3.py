from collections import deque
import sys
input = sys.stdin.readline

d = [1,2,4,7]
n = int(input())
for _ in range(n):
  num = int(input())
  for i in range(len(d), num + 1):
    d.append((d[-3] + d[-2] + d[-1])% 1000000009)
  # print('d[i] : ', d[i])
  print((d[num - 1]) )