import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

gun = deque()
for i in range(N - 1, -1, -1):
  if (A[i] == 0):
    gun.append(B[i])

for i in range(M):
  tar = nums[i]
  gun.append(tar)
  print(gun.popleft(), end=' ')