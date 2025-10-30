N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# (0, 1) 부터 (n - 3, n - 2) 까지 점을 맨 윗 모서리로
tops = []  # 위쪽 모서리 후보들
for i in range(0, N - 2):
  for j in range(1, N - 1):
    tops.append([i, j])

def get_rac(top):
  res = []
  y, x = top[0], top[1]  # top 좌표
  for ld in range(1, N):  # left down
    for rd in range(1, N):  # right down
      if (y + ld + rd >= N):
        continue
      if (x - ld < 0 or x + rd >= N):
        continue
      left = [y + ld, x - ld]
      right = [y + rd, x + rd]
      bottom = [y + ld + rd, x - ld + rd]
      res.append((top, left, right, bottom))

  return res

def cal_rac(top, left, right, bottom):
  area = [[0 for _ in range(N)] for _ in range(N)]
  part = 5
  y, x = top
  ld = left[0] - y  # left down
  rd = right[0] - y  # right down

  score = [0, 0, 0, 0, 0]

  # 경계선 긋고
  for i in range(ld + 1):
    if (area[y + i][x - i] != part):
      score[4] += board[y + i][x - i]
    area[y + i][x - i] = part
    if (area[y + rd + i][x + rd - i] != part):
      score[4] += board[y + rd + i][x + rd - i]
    area[y + rd + i][x + rd - i] = part

  for i in range(rd + 1):
    if (area[y + i][x + i] != part):
      score[4] += board[y + i][x + i]
    area[y + i][x + i] = part
    if (area[y + ld + i][x - ld + i] != part):
      score[4] += board[y + ld + i][x - ld + i]
    area[y + ld + i][x - ld + i] = part

  for yy in range(N):  # 한 줄씩 검사
    start, end = -1, -1
    for xx in range(N):
      if (area[yy][xx] == part):  # 처음 발견
        if (start == -1):
          start = xx
        else:
          end = xx
    if (start == -1 or end == -1):
      continue
    for i in range(start, end + 1):
      if (area[yy][i] != part):
        score[4] += board[yy][i]
      area[yy][i] = part

  # 1
  for yy in range(left[0]):
    for xx in range(top[1] + 1):
      if (area[yy][xx] == part):
        break
      score[0] += board[yy][xx]
      area[yy][xx] = 1

  # 2
  for yy in range(right[0] + 1):
    for xx in range(N - 1, top[1], -1):
      if (area[yy][xx] == part):
        break
      score[1] += board[yy][xx]
      area[yy][xx] = 2

  # 3
  for yy in range(left[0], N):
    for xx in range(bottom[1]):
      if (area[yy][xx] == part):
        break
      score[2] += board[yy][xx]
      area[yy][xx] = 3

  # 4
  for yy in range(right[0] + 1, N):
    for xx in range(N - 1, bottom[1] - 1, -1):
      if (area[yy][xx] == part):
        break
      score[3] += board[yy][xx]
      area[yy][xx] = 4
  return (max(score) - min(score), area, ld, rd)


res = float('inf')

for top in tops:
  racs = get_rac(top)
  for r in racs:
    diff, area, ld, rd = cal_rac(*r)
    res = min(res, diff)
print(res)
