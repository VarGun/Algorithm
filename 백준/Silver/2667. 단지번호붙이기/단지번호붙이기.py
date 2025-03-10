from collections import deque

n = int(input())
arr = [[] for _ in range(n)]

for i in range(n):
  line = input()
  for j in range(n):
    arr[i].append(int(line[j]))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * n for _ in range(n)]
cnt_list = []
num = 1
num_cnt = 0

def bfs(y, x):
  global num, num_cnt
  q = deque([[y, x]])
  visited[y][x] = num
  
  while q:
    head = q.popleft()
    y = head[0]
    x = head[1]
    num_cnt += 1

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if(0 <= nx < n and 0 <= ny < n and arr[ny][nx] == 1 and visited[ny][nx] == 0):
        q.append([ny, nx])
        visited[ny][nx] = num
  
  cnt_list.append([num, num_cnt])


for i in range(n):
  for j in range(n):
    if(arr[i][j] == 1 and visited[i][j] == 0):
      num_cnt = 0
      num += 1
      bfs(i, j)

print(num -  1)
cnt_list.sort(key=lambda x : x[1])
for i in range(num - 1):
  print(cnt_list[i][1])