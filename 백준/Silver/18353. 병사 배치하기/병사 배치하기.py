n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n + 1)]
dp[0] = 1
for i in range(1, n):  # 본인 자리
  for j in range(i):  # 비교 대상
    if (arr[j] > arr[i] and dp[i] < dp[j] + 1):
      dp[i] = dp[j] + 1
print(n - max(dp))
