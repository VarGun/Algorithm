from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

tmt = deque()

for i in range(h):
  for j in range(n):
    for k in range(m):
      if(arr[i][j][k] == 1):
        tmt.append([i, j, k])


def bfs():
  global tmt

  while tmt:
    head = tmt.popleft()
    x = head[2]
    y = head[1]
    z = head[0]
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      if(0 <= nx < m and 0 <= ny < n and 0 <= nz < h and arr[nz][ny][nx] == 0):
        arr[nz][ny][nx] = arr[z][y][x] + 1
        tmt.append([nz, ny, nx])

bfs()

ans = 0
z_flag = False
for i in range(h):
  for j in range(n):
    for k in range(m):
      if(arr[i][j][k] == 0):
        print(-1)
        z_flag = True
        break
      if(arr[i][j][k] > ans):
        ans = arr[i][j][k]
    if(z_flag):
      break
  if(z_flag):
    break

if(not z_flag):
  print(ans - 1)
