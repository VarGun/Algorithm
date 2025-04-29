import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
ques = []


def pald(s):
  n = len(s)
  dp = [[False] * n for _ in range(n)]

  for i in range(n):
    dp[i][i] = True

  for i in range(n - 1):
    if (s[i] == s[i + 1]):
      dp[i][i + 1] = True

  for i in range(3, n + 1):
    for j in range(n - i + 1):  # 시작점 => 길이가 3일 경우 0 부터 5까지 가능 => 7 - 3 + 1 = 5
      k = j + i - 1  # 끝 점 => 시작점으로부터 길이만큼 떨어진 점
      if (s[j] == s[k] and dp[j + 1][k - 1]):  # 1. 시작점과 끝 점이 같고 2. 그 안쪽 문자열이 pald 라면
        dp[j][k] = True

  return dp

dp = pald(nums)

for _ in range(m):
  s, e = map(int, input().split())
  if (dp[s - 1][e - 1]):
    print(1)
  else:
    print(0)
