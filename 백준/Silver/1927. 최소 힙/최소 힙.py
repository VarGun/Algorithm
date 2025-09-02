import heapq
import sys
input = sys.stdin.readline
N = int(input())
gun = []
length = 0

for _ in range(N):
  n = int(input())
  if (n == 0):
    if (len(gun) == 0):
      print(0)
    else:
      print(heapq.heappop(gun))
  else:
    heapq.heappush(gun, n)
