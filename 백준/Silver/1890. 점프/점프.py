import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dp = [[0 for _ in range(101)] for _ in range(101)]

dp[0][0] = 1

for i in range(n):
  for j in range(n):
    if(arr[i][j] == 0 or dp[i][j] == 0):
      continue
    if(i + arr[i][j] < n):
      dp[i + arr[i][j]][j] += dp[i][j]
    if(j + arr[i][j] < n):
      dp[i][j + arr[i][j]] += dp[i][j]

print(dp[n - 1][n - 1])