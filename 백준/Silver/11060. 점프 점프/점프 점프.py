n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]

for i in range(n - 1):
  if(arr[i] != 0):
    if(i != 0 and dp[i] == 0):
      break
    tmp = dp[i]
    for j in range(i + 1, i + arr[i] + 1):
      if(j < n):
        if(dp[j] == 0):
          dp[j] = tmp + 1
        else:
          dp[j] = min(dp[j], tmp + 1)

if(n == 1):
  print(0)
else:
  if(dp[n - 1] == 0):
    print(-1)
  else:
    print(dp[n - 1])