N = int(input())
arr = list(map(int, input().split()))

dp = [[-1] * N for _ in range(2)]

dp[0][0] = dp[1][0] = arr[0]

for i in range(1, N):
  dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
  dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])

print(max(max(dp[0]), max(dp[1])))
