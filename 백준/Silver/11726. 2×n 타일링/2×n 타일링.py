n = int(input())
dp = [0, 1, 2]
for i in range(2, n):
  cur = dp[-1] + dp[-2]
  dp.append(cur)
print(dp[n] % 10007)