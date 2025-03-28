from collections import deque
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
wall = list(map(int, input().split()))

arr = [[0 for _ in range(w)] for _ in range(h)]

for i in range(w):
  for j in range(h - wall[i], h):
    arr[j][i] = 1

visited = [[0 for _ in range(w)] for _ in range(h)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0

def find_right(i, j):
  global visited
  origin_j = j
  while True:
    j += 1
    if(j >= w):
      for k in range(origin_j, w):
        visited[i][k] = 1
      return False
    
    if(arr[i][j] == 1):
      return [i, j]

def find_left(i, j):
  global visited
  origin_j = j
  while True:
    j -= 1
    if(j < 0):
      for k in range(origin_j, -1, -1):
        visited[i][k] = 1
      return False
    
    if(arr[i][j] == 1):
      return [i, j]

def bfs(y, x):
  global visited, ans
  if(visited[y][x] == 1):
    return
  q = deque()
  q.append([y, x])
  visited[y][x] = 1
  while q:
    head = q.popleft()
    ans += 1
    y = head[0]
    x = head[1]
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
    if(0 <= ny < h and 0 <= nx < w and visited[ny][nx] == 0 and arr[ny][nx] == 0):
      q.append([ny, nx])
      visited[ny][nx] = 1

for i in range(h):
  for j in range(w):
    if(arr[i][j] == 0 and visited[i][j] == 0):
      right = find_right(i, j)
      left = find_left(i, j)
      if(right and left):
        bfs(i, j)

print(ans)