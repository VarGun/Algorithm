N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2)]
ans = 0


def rec(score, before_x, day):
  global N, M, ans
  if (day == N):
    if (score >= M):
      ans += 1
    return
  else:
    for i in range(2):
      for j in range(3):
        if (j == before_x):
          rec(score + (arr[i][j] // 2), j, day + 1)
        else:
          rec(score + arr[i][j], j, day + 1)


rec(0, -1, 0)
print(ans)
