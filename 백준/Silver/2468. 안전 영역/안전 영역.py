from collections import deque
n = int(input())
arr = []
_max = -1
_min = 101
for _ in range(n):
  line = list(map(int, input().split()))
  if (max(line) > _max):
    _max = max(line)
  if (min(line) < _min):
    _min = min(line)
  arr.append(line)
visited = [[False for _ in range(n)] for _ in range(n)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(y, x, height, visited, arr):
  q = deque()
  q.append([y, x])
  visited[y][x] = True
  while q:
    head = q.popleft()
    y = head[0]
    x = head[1]
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if (0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and arr[ny][nx] > height):
        q.append([ny, nx])
        visited[ny][nx] = True

max_cnt = 0
for height in range(0, _max + 1):
  cnt = 0
  visited = [[False for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if (not visited[i][j] and arr[i][j] > height):
        cnt += 1
        bfs(i, j,  height, visited, arr)
  if (max_cnt < cnt):
    max_cnt = cnt
print(max_cnt)