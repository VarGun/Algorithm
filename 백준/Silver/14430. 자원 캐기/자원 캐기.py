r, c = map(int, input().split())
arr = []
for _ in range(r):
  arr.append(list(map(int, input().split())))
dp = [[0 for _ in range(c)] for _ in range(r)]
dp[0][0] = arr[0][0]
for i in range(r):
  for j in range(c):
    if (i == 0):  # 맨 윗줄
      if (j == 0):
        continue
      dp[i][j] = arr[i][j] + max(dp[i][j], dp[i][j - 1])
    elif (j == 0):  # 맨 왼쪽 줄
      dp[i][j] = arr[i][j] + max(dp[i][j], dp[i - 1][j])
    else:
      dp[i][j] = arr[i][j] + max(dp[i][j], dp[i][j - 1], dp[i - 1][j])

print(dp[r - 1][c - 1])
