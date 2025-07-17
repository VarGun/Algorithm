n = int(input())

dp = [0 for _ in range(n + 5)]
dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 0

for i in range(5, n + 1):
  if (dp[i - 1] == 0 and dp[i - 3] == 0 and dp[i - 4] == 0):
    dp[i] = 1
  else:
    dp[i] = 0
if (dp[n]):
  print('CY')
else:
  print('SK')
