import sys

input = sys.stdin.readline

n = int(input())
dp = [1 for _ in range(n + 1)]

arr = list(map(int, input().split()))

for i in range(1, n):
  for j in range(i):
    if(arr[i] < arr[j]):
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))