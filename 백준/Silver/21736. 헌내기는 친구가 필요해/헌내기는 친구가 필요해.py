import sys

sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
init = []  # 도연 위치
arr = []
for i in range(n):
  tar = list(input())
  for j in range(m):
    if (tar[j] == 'I'):
      init = [i, j]
  arr.append(tar)
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
visited = [[False for _ in range(m)] for _ in range(n)]

# dfs
visited[init[0]][init[1]] = True
cnt = 0
def dfs(y, x):
  global cnt
  visited[y][x] = True
  if (arr[y][x] == 'P'):
    cnt += 1
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if (0 <= ny < n and 0 <= nx < m and arr[ny][nx] != 'X' and not visited[ny][nx]):
      dfs(ny, nx)

dfs(init[0], init[1])
print(cnt if cnt != 0 else 'TT')