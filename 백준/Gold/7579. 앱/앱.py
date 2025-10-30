N, M = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

max_cost = 100 * 100
dp = [0 for _ in range(max_cost + 1)]
for ci in range(len(c)):
  for cost in range(max_cost, c[ci] - 1, -1):
    dp[cost] = max(dp[cost], dp[cost - c[ci]] + a[ci])

for di in range(len(dp)):
  if (dp[di] >= M):
    print(di)
    break
