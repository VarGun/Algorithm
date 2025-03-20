import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(1003)] for _ in range(1003)]

for i in range(1, n + 1):
  for j in range(1, m + 1):
    dp[i][j] = arr[i - 1][j - 1] + max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
    if(i == n and j == m):
      print(dp[i][j])