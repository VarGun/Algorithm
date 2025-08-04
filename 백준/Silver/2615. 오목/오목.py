board = [list(map(int, input().split())) for _ in range(19)]
flag = False
dy = [1, -1, 0, 1]
dx = [0, 1, 1, 1]

oy = [-1, 1, 0, -1]
ox = [0, -1, -1, -1]


def gun(y, x, tar):  # 찾으면 검사
  global board, flag
  dirs = []
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if (0 <= ny < 19 and 0 <= nx < 19 and board[ny][nx] == tar):
      dirs.append(i)  # 방향 저장
  if (not dirs):  # 주변에 같은 애가 없을 경우
    return

  for i in range(len(dirs)):
    dd = dirs[i]  # 해당 방향
    # 시작점 판단 필요 (반대편이 다른지 같은지)
    ooy = y + oy[dd]
    oox = x + ox[dd]
    # 범위 내 이고, 같을 경우 continue
    if (0 <= ooy < 19 and 0 <= oox < 19 and board[ooy][oox] == tar):
      continue

    cnt = 0
    tmp_y = y
    tmp_x = x
    for _ in range(19):
      tmp_y = tmp_y + dy[dd]  # (0, 1) -> (1, 1) -> (2, 1)
      tmp_x = tmp_x + dx[dd]
      if (0 <= tmp_y < 19 and 0 <= tmp_x < 19):
        if (board[tmp_y][tmp_x] == tar):
          cnt += 1
        else:
          break
      else:
        break

    if (cnt == 4):
      flag = True
      print(tar)
      print(y + 1, x + 1)
      return

for i in range(19):
  for j in range(19):
    if (flag):
      break
    if (board[i][j] != 0):
      gun(i, j, board[i][j])
  if (flag):
    break
if (not flag):
  print(0)
