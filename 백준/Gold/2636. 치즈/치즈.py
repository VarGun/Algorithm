from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(y, x, tmp, visited):
  global arr
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
      if(0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0): # 탐색할 대상
        if(arr[ny][nx] == 1):
          tmp[ny][nx] = 0
        elif(arr[ny][nx] == 0):
          q.append([ny, nx])
          visited[ny][nx] = 1


def bfs_cheese(y, x, visited):
  global arr
  q = deque()
  q.append([y, x])
  visited[y][x] = 1
  cnt_cheese = 0
  while q:
    head = q.popleft()
    cnt_cheese += 1
    y = head[0]
    x = head[1]
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if(0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and arr[ny][nx] == 1): # 탐색할 대상
        q.append([ny, nx])
        visited[ny][nx] = 1
  return cnt_cheese

time = 0
before_cheese = 0
while True:
  visited = [[0 for _ in range(m)] for _ in range(n)]
  visited_cheese = [[0 for _ in range(m)] for _ in range(n)]
  cnt = 0
  cnt_cheese = 0

  for i in range(n): # 먼저 세
    for j in range(m):
      if(arr[i][j] == 1 and visited_cheese[i][j] == 0):
        cnt += 1
        cnt_cheese += bfs_cheese(i, j, visited_cheese)
  if(cnt == 0):
    print(time)
    print(before_cheese)
    break

  tmp = copy.deepcopy(arr)

  bfs(0, 0, tmp, visited)

  arr = copy.deepcopy(tmp)
  
  time += 1

  before_cheese = cnt_cheese