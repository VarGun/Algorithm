from collections import deque
n = int(input())
arr = []
for _ in range(n):
  arr.append(list(input()))

cnt = 0  # 단지 수
sizes = []  # 단지 크기들
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
visited = [[False for _ in range(n)] for _ in range(n)]

def bfs(y, x, cnt):
  global visited, sizes
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
      if (0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and arr[ny][nx] == '1'):
        q.append([ny, nx])
        visited[ny][nx] = True
        cnt += 1
  sizes.append(cnt)

for i in range(n):
  for j in range(n):
    if (arr[i][j] == '1' and visited[i][j] == False):
      cnt = 1
      bfs(i, j, cnt)
print(len(sizes))
sizes.sort()
for i in range(len(sizes)):
  print(sizes[i])
