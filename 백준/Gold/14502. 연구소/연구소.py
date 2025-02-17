from collections import deque

n, m = map(int, input().split())
g = []
for i in range(n):
  g.append(list(map(int, input().split())))

ans = 0
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs():
  q = deque()
  tmp_g = []
  for i in range(n):
    tmp_g.append([])
    for j in range(m):
      tmp_g[i].append(g[i][j])
      if(tmp_g[i][j] == 2):
        q.append([i, j])
  
  while q:
    h = q.popleft()
    x, y = h[0], h[1]

    for i in range(4):
      nx, ny = x + d[i][0], y + d[i][1]

      if(0 <= nx < n and 0 <= ny < m):
        if(tmp_g[nx][ny] == 0):
          tmp_g[nx][ny] = 2
          q.append([nx, ny])
  
  global ans
  safe = 0

  for i in tmp_g:
    for j in i:
      if(j == 0):
        safe += 1
  
  ans = max(ans, safe)


def wall(cnt):
  if(cnt == 3):
    bfs()
    return
  
  for i in range(n):
    for j in range(m):
      if(g[i][j] == 0):
        g[i][j] = 1
        wall(cnt + 1)
        g[i][j] = 0

wall(0)
print(ans)