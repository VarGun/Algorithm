from collections import deque
R, C = map(int, input().split())
s = 0  # 양
w = 0  # 늑대
board = []
visited = [[False for _ in range(C)] for _ in range(R)]

for _ in range(R):
  line = list(input())
  for i in line:
    if (i == 'o'):
      s += 1
    elif (i == 'v'):
      w += 1
  board.append(line)
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def bfs(y, x):
  global visited, board, s, w

  tmp_s = tmp_w = 0
  q = deque()
  q.append((y, x))
  visited[y][x] = True

  while q:
    y, x = q.popleft()
    if (board[y][x] == 'o'):
      tmp_s += 1
    elif (board[y][x] == 'v'):
      tmp_w += 1
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if (0 <= ny < R and 0 <= nx < C and not visited[ny][nx] and board[ny][nx] != '#'):
        q.append([ny, nx])
        visited[ny][nx] = True
  if (tmp_s > tmp_w):
    w -= tmp_w
  else:
    s -= tmp_s


for i in range(R):
  for j in range(C):
    if ((board[i][j] == 'o' or board[i][j] == 'v') and not visited[i][j]):
      bfs(i, j)
print(s, w)
