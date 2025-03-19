n = int(input())
while n:
  n -= 1
  
  t = int(input())
  dp = [0 for _ in range(10001)]
  dp[1] = 1
  dp[2] = 1
  dp[3] = 1
  dp[4] = 2
  dp[5] = 2
  for i in range(6, t + 1):
    dp[i] = dp[i - 1] + dp[i - 5]

  print(dp[t])