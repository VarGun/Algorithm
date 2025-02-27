import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []


for _ in range(n):
  arr.append(list(map(int, input().split())))


d = [[1, 0], [-1, 0], [0, -1], [0, 1]]


q = deque()

def bfs(x, y):
  global visited
  q.append([x, y])

  while len(q) != 0:
    head = q.popleft()
    x = head[0]
    y = head[1]
    visited[x][y] = True
    for i in range(4):
      dx = x + d[i][0]
      dy = y + d[i][1]
      if(tmp[dx][dy] <= 0):
        arr[x][y] -= 1
      else:
        if(visited[dx][dy] == False):
          visited[dx][dy] = True
          q.append([dx, dy])

year = 0


while True:

  tmp = [[0 for _ in range(m)]for _ in range(n)]

  for i in range(n):
    for j in range(m):
      tmp[i][j] = arr[i][j]
  
  cnt = 0
  visited = [[False for _ in range(m)] for _ in range(n)]
  flag = False

  for i in range(1, n - 1):
    for j in range(1, m - 1):      
      if(tmp[i][j] > 0 and visited[i][j] == False):
        cnt += 1
        if(cnt >= 2):
          flag = True
          break
        bfs(i, j)

  
  if(flag):
    print(year)
    break
  
  if(cnt == 0):
    print(0)
    break

  elif(cnt >= 2):
    print(year)
    break
  
  else:
    year += 1