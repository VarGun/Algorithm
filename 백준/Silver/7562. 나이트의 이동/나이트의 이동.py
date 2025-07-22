from collections import deque

def bfs(y, x, visited, l, oy, ox):
  dy = [2, 1, -1, -2, -2, -1, 1, 2]
  dx = [1, 2, 2, 1, -1, -2, -2, -1]
  visited[y][x] = 0
  q = deque()
  q.append([y, x])
  while q:
    head = q.popleft()
    y = head[0]
    x = head[1]
    if (y == oy and x == ox):
      return
    for i in range(8):
      ny = y + dy[i]
      nx = x + dx[i]
      if (0 <= ny < l and 0 <= nx < l and visited[ny][nx] == -1):
        visited[ny][nx] = visited[y][x] + 1
        q.append([ny, nx])

t = int(input())
while t:
  t -= 1
  l = int(input())
  visited = [[-1 for _ in range(l)] for _ in range(l)]
  ky, kx = map(int, input().split())
  oy, ox = map(int, input().split())
  bfs(ky, kx, visited, l, oy, ox)
  print(visited[oy][ox])
