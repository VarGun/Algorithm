import sys

input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
_sum = 0
for i in range(1, N + 1):
  gun = abs(i - arr[i - 1])
  _sum += gun
print(_sum)
