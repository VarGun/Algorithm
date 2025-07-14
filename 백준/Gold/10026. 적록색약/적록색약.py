from collections import deque

n = int(input())
arr = [input() for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
visited_jm = [[0 for _ in range(n)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(y, x, char, visited, js):
  q = deque()
  q.append([y, x])

  while q:
    head = q.popleft()
    x = head[1]
    y = head[0]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0):
        if(js):
          if(arr[ny][nx] == char):
            q.append([ny, nx])
            visited[ny][nx] = 1
        else: 
          if(char == 'R' or char == 'G'):
            if(arr[ny][nx] == 'R' or arr[ny][nx] == 'G'):
              q.append([ny, nx])
              visited_jm[ny][nx] = 1
          elif(char == 'B'):
            if(arr[ny][nx] == 'B'):
              q.append([ny, nx])
              visited_jm[ny][nx] = 1

cnt = 0
cnt_jm = 0
for i in range(n):
  for j in range(n):
    if(visited[i][j] == 0):
      bfs(i, j, arr[i][j], visited, True) # 정상
      cnt += 1
    if(visited_jm[i][j] == 0):
      bfs(i, j, arr[i][j], visited_jm, False)
      cnt_jm += 1

print(cnt, cnt_jm)