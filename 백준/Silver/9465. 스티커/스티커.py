import sys

input = sys.stdin.readline
t = int(input())

while t:
  t -= 1
  n = int(input())
  arr = [list(map(int, input().split())) for _ in range(2)]
  dp = [[0 for _ in range(n)] for _ in range(2)]
  
  if(n == 1):
    print(max(arr[0][0], arr[1][0]))
    continue

  dp[0][0], dp[1][0] = arr[0][0], arr[1][0]

  dp[0][1], dp[1][1] = arr[0][1] + arr[1][0], arr[1][1] + arr[0][0]
  for i in range(2, n):
    for j in range(2):
      dp[j][i] = arr[j][i] + max(dp[abs(j - 1)][i - 1], dp[abs(j - 1)][i - 2])

  print(max(dp[0][n - 1], dp[1][n - 1]))