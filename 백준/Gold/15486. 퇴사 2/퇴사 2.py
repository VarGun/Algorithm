import sys
input = sys.stdin.readline
n = int(input())
table = []
dp = [0 for _ in range(n + 1)]

for _ in range(n):
  table.append(list(map(int, input().split())))
_max = 0
for i in range(n):
  _max = max(_max, dp[i])
  if (i + table[i][0] > n):
    continue
  dp[i + table[i][0]] = max(dp[i + table[i][0]], _max + table[i][1])

print(max(dp))
