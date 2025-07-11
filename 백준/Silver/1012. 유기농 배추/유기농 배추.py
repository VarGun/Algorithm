from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(y, x, visited, n, m, arr):
  global dy, dx
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
      if (0 <= ny < n and 0 <= nx < m and visited[ny][nx] == False and arr[ny][nx] == 1):
        q.append([ny, nx])
        visited[ny][nx] = True

t = int(input())
while t:
  t -= 1
  m, n, k = map(int, input().split())
  arr = [[0 for _ in range(m)] for _ in range(n)]
  visited = [[False for _ in range(m)] for _ in range(n)]
  for _ in range(k):
    x, y = map(int, input().split())
    arr[y][x] = 1
  cnt = 0
  for i in range(n):
    for j in range(m):
      if (arr[i][j] == 1 and visited[i][j] == False):
        cnt += 1
        bfs(i, j, visited, n, m, arr)
  print(cnt)