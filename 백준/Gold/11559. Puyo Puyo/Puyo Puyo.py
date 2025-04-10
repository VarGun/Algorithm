from collections import deque

arr = [list(input()) for _ in range(12)]
visited = []
flag = False
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(y, x, char): # 탐색 + 4개 이상인지 검사
  global visited, arr, flag, ans
  q = deque()
  same = deque()
  q.append([y, x])
  same.append([y, x])

  visited[y][x] = 1
  size = 1
  while q:
    head = q.popleft()
    y = head[0]
    x = head[1]
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if(0 <= ny < 12 and 0 <= nx < 6 and visited[ny][nx] == 0 and arr[ny][nx] == char):
        q.append([ny, nx])
        same.append([ny, nx])
        visited[ny][nx] = 1
        size += 1

  if(size >= 4):
    flag = True
    while(same): # 없애기
      head = same.popleft()
      arr[head[0]][head[1]] = '.'


def renewal_map(same = deque()): # 맵 갱신
  global arr

  for i in range(6):
    for j in range(10, -1, -1):
      if(arr[j][i] != '.'):
        for k in range(j + 1, 12):
          if(arr[k][i] != '.'): # 끝으로 가기 전에 만남
            tmp = arr[j][i]
            arr[j][i] = '.'
            arr[k - 1][i] = tmp
            
            break
          elif(k == 11 and arr[k][i] == '.'):
            tmp = arr[j][i]
            arr[j][i] = '.'
            arr[k][i] = tmp
  

while(True):
  visited = [[0] * 6 for _ in range(12)]
  flag = False
  for i in range(12):
    for j in range(6):
      if(arr[i][j] != '.' and visited[i][j] == 0):
        bfs(i, j, arr[i][j])

  ans += 1
  renewal_map()
  if(not flag):
    
    break

print(ans - 1)