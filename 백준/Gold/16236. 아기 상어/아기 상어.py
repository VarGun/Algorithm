from collections import deque

n = int(input())
start = []
arr = []
for i in range(n):
  line = list(map(int, input().split()))
  for j in range(n):
    if(line[j] == 9):
      start = [i, j]
  arr.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

time = 0 # 시간
lv = 2 # 상어 크기
eat = 0 # 먹은 물고기 수

def bfs(y, x, spot):
  global lv, arr
  visited = [[0 for _ in range(n)] for _ in range(n)]
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
      if( 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0 and arr[ny][nx] <= lv): # 지나갈 수는 있게
        visited[ny][nx] = visited[head[0]][head[1]] + 1 # 길은 표시
        if(arr[ny][nx] != 0 and arr[ny][nx] < lv): # 먹을 수 있는지
          spot.append([visited[ny][nx], ny, nx])
        q.append([ny, nx])
  
cnt = 0
while True:
  spot = [] # 물고기의 위치 : [거리, y 좌표, x 좌표]

  bfs(start[0], start[1], spot)
  if(len(spot) == 0): # 갈 수 있는 곳이 없을 때
    break
  next = sorted(spot, key=lambda x: (x[0], x[1], x[2]))[0]
  time += next[0] - 1
  arr[start[0]][start[1]] = 0
  start = [next[1], next[2]]
  if(lv > arr[next[1]][next[2]]): # 먹을 수 있는 경우
    eat += 1
  if(eat == lv):
    eat = 0
    lv += 1
  
print(time)