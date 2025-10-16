from collections import deque
R, C = map(int, input().split())
board = []
JHs = deque()
FRs = deque()

for i in range(R):
  line = input()
  board_line = []
  for j in range(len(line)):
    if (line[j] == 'J'):
      JHs.append((i, j))
    elif (line[j] == 'F'):
      FRs.append((i, j))
    board_line.append(line[j])
  board.append(board_line)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
y, x = JHs.popleft()
if (y == 0 or y == R - 1 or x == 0 or x == C - 1):
  print(1)
  exit(0)
else:
  JHs.append((y, x))

cnt = 0
while (True):
  # 지훈 이동
  cnt += 1
  next_JHs = set()
  next_FRs = set()
  while JHs:
    y, x = JHs.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if (0 <= ny < R and 0 <= nx < C and board[ny][nx] == '.'):
        board[ny][nx] = 'J'
        next_JHs.add((ny, nx))
  # 불 이동
  while FRs:
    y, x = FRs.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if (0 <= ny < R and 0 <= nx < C and board[ny][nx] != '#' and board[ny][nx] != 'F'):
        if ((ny, nx) in next_JHs):
          next_JHs.remove((ny, nx))
        board[ny][nx] = 'F'
        next_FRs.add((ny, nx))

  if (len(next_JHs) == 0):  # 지훈이 위치 다 탐
    print('IMPOSSIBLE')
    break
  end_flag = False
  for j in next_JHs:
    y, x = j
    if (y == 0 or y == R - 1 or x == 0 or x == C - 1):
      end_flag = True
      break
    JHs.append(j)
  if (end_flag):
    print(cnt + 1)
    break

  for f in next_FRs:
    FRs.append(f)