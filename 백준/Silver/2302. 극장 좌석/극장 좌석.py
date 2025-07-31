N = int(input())
M = int(input())
vip = []
for _ in range(M):
  vip.append(int(input()))
dp = [1] * 41
dp[2] = 2


for i in range(3, 41):
  dp[i] = dp[i - 1] + dp[i - 2]

if (len(vip) != 0):
  start = 0
  ans = 1
  for i in range(len(vip)):
    div = vip[i]  # 가르기
    gun = div - start - 1
    ans *= dp[gun]
    start = div
  if (N != start):
    ans *= dp[N - start]
  print(ans)
else:
  print(dp[N])
