import sys

n = int(input())
arr = list(input())
dp = [sys.maxsize for _ in range(n)]
dp[0] = 0
for i in range(n):
  for j in range(i + 1, n):
    if (arr[i] == 'B' and arr[j] == 'O'):
      dp[j] = min(dp[j], (j - i) ** 2 + dp[i])
    elif (arr[i] == 'O' and arr[j] == 'J'):
      dp[j] = min(dp[j], (j - i) ** 2 + dp[i])
    elif (arr[i] == 'J' and arr[j] == 'B'):
      dp[j] = min(dp[j], (j - i) ** 2 + dp[i])


if (dp[-1] == sys.maxsize):
  print(-1)
else:
  print(dp[-1])
