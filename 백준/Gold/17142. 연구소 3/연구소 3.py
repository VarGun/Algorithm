from collections import deque
import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
board = []
vr = []
vr_cnt = 0
wall_cnt = 0
for i in range(n):
  line = list(map(int, input().split()))
  for j in range(n):
    if (line[j] == 2):
      vr.append([i, j])
      vr_cnt += 1
    elif (line[j] == 1):
      wall_cnt += 1
  board.append(line)

all_cnt = n * n - wall_cnt
if (wall_cnt + vr_cnt == n * n):
  print(0)
  exit(0)
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(q=deque()):
  global all_cnt
  tmp_board = [[0 for _ in range(n)] for _ in range(n)]
  visited = [[0 for _ in range(n)] for _ in range(n)]
  check_cnt = 0
  for i in range(len(q)):
    visited[q[i][0]][q[i][1]] = 1
    check_cnt += 1
  while q:
    head = q.popleft()
    y = head[0]
    x = head[1]
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if (0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0 and (board[ny][nx] == 0 or board[ny][nx] == 2)):
        q.append([ny, nx])
        tmp_board[ny][nx] = tmp_board[y][x] + 1
        visited[ny][nx] = 1
        check_cnt += 1
  if (all_cnt != check_cnt):
    return -1
  _max = -1
  for i in range(n):
    for j in range(n):
      if (board[i][j] == 0):  # 바이러스가 아닐 경우
        _max = max(_max, tmp_board[i][j])

  return _max

_min = 50 * 50
flag = False
for comb in combinations(vr, m):
  gun = deque(comb)
  res = bfs(gun)
  if (res != -1):
    flag = True
    _min = min(_min, res)

if (flag):
  print(_min)
else:
  print(-1)
