from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = []
for _ in range(n):
  paper.append(list(map(int, input().split())))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(y, x):
  global dy, dx, ans_flag
  c_q = deque()
  visited = [[0 for _ in range(m)] for _ in range(n)]
  c_map = [[0 for _ in range(m)] for _ in range(n)]
  q = deque()
  q.append([y, x])
  visited[y][x] = 1
  while q:
    head = q.popleft()
    y = head[0]
    x = head[1]
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if (0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0):
        if (paper[ny][nx] == 0):
          q.append([ny, nx])
          visited[ny][nx] = 1
        elif (paper[ny][nx] == 1):
          ans_flag = True
          if (c_map[ny][nx] < 2):
            c_map[ny][nx] += 1
            if (c_map[ny][nx] >= 2):
              c_q.append([ny, nx])
  return c_q


ans_flag = False
ans = 0
while True:
  ans_flag = False

  for i in range(n):
    flag = False
    for j in range(m):
      if (paper[i][j] == 0):
        c_q = bfs(i, j)
        flag = True
        break
    if (flag):
      break

  if (not ans_flag):
    print(ans)
    break

  ans += 1
  while c_q:
    head = c_q.popleft()
    paper[head[0]][head[1]] = 0
