from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
vir = [[] for _ in range(k + 1)]
board = []
for i in range(n):
  line = list(map(int, input().split()))
  for j in range(n):
    if (line[j] != 0):
      vir[line[j]].append([i, j])
  board.append(line)
s, tar_x, tar_y = map(int, input().split())

if (s == 0):
  print(board[tar_x - 1][tar_y - 1])
  exit()

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

q = deque()
for i in range(k + 1):
  if (len(vir[i]) != 0):
    for j in range(len(vir[i])):
      q.append(vir[i][j])

while s:
  flag = False
  tmp_q = deque()
  gun = len(q)
  while gun:
    gun -= 1
    head = q.popleft()
    for i in range(4):
      ny = head[0] + dy[i]
      nx = head[1] + dx[i]
      if (0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0):
        q.append([ny, nx])
        if (ny == tar_x - 1 and nx == tar_y - 1):
          print(board[head[0]][head[1]])
          exit()
        board[ny][nx] = board[head[0]][head[1]]
  s -= 1
print(board[tar_x - 1][tar_y - 1])
