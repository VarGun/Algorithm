n = int(input())
tar = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]
i_p = [n // 2, n // 2]
cnt = 1  # 총 횟수
cur = 0  # (간 횟수 == 가야하는 횟수) 의 횟수
go_cnt = 0  # 간 횟수
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dir_cnt = 1  # 가야하는 횟수
d = 0  # 방향
ans_y, ans_x = 0, 0
while cnt <= n ** 2:

  board[i_p[0]][i_p[1]] = cnt
  if (cnt == tar):
    ans_y, ans_x = i_p[0] + 1, i_p[1] + 1
  i_p[0] += dy[d]
  i_p[1] += dx[d]
  go_cnt += 1
  if (go_cnt == dir_cnt):
    go_cnt = 0
    cur += 1
    d = (d + 1) % 4

  if (cur == 2):
    cur = 0
    dir_cnt += 1

  cnt += 1

for i in range(n):
  for j in range(n):
    print(board[i][j], end=' ')
  print()
print(ans_y, ans_x)
