import sys
input = sys.stdin.readline
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

# 0 : 가로, 1 : 세로, 2 : 대각선
dp[0][0][1] = 1
for i in range(2, n):
  if (arr[0][i] == 0):
    dp[0][0][i] = dp[0][0][i - 1]  # 맨 윗 줄 가로 처리

for i in range(1, n):
  for j in range(1, n):
    if (arr[i][j] == 0):
      # 가로
      if (arr[i][j - 1] == 0):
        dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
      # 세로
      if (arr[i - 1][j] == 0):
        dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]
      # 대각선
      if (arr[i - 1][j] == 0 and arr[i][j - 1] == 0):
        dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]

sum = 0
for i in range(3):
  sum += dp[i][n - 1][n - 1]
print(sum)