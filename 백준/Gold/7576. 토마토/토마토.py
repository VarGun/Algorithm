from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
tmt = deque()

for i in range(n):
  for j in range(m):
    if(arr[i][j] == 1):
      tmt.append([i, j])

while tmt:
  head = tmt.popleft()
  x, y = head[1], head[0]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if(0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 0):
      arr[ny][nx] = arr[y][x] + 1
      tmt.append([ny, nx])

z_flag = False
day = 0

for line in arr:
  for j in line:
    if(j == 0):
      z_flag = True
      print(-1)
      break
    day = max(day, j)
  if(z_flag):
    break
  
if(not z_flag):
  print(day - 1)