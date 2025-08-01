N = int(input())
hp = [0] + list(map(int, input().split()))
good = [0] + list(map(int, input().split()))


dp = [[0 for _ in range(101)] for _ in range(N + 1)]

for i in range(1, N + 1):
  for j in range(1, 101):
    if (hp[i] <= j):
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - hp[i]] + good[i])
    else:
      dp[i][j] = dp[i - 1][j]

print(dp[N][99])
