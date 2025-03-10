from collections import deque

n = int(input())
arr = []
_max = 0
for i in range(n):
  line = list(map(int, input().split()))
  for j in line:
    if(j > _max):
      _max = j
  arr.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(arr, h, y, x, visited):
  q = deque()
  q.append([y, x])

  while q:
    head = q.popleft()
    x = head[1]
    y = head[0]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if(0 <= nx < n and 0 <= ny < n and arr[ny][nx] > h and visited[ny][nx] == 0):
        q.append([ny, nx])
        visited[ny][nx] = 1
      
  return

max_cnt = -1

for height in range(0, _max + 1): # 1 부터 최대값까지 돌기
  cnt = 0
  visited = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if(arr[i][j] > height and visited[i][j] == 0):
        cnt += 1
        bfs(arr, height, i, j, visited)
  if(max_cnt < cnt):
    max_cnt = cnt
print(max_cnt)