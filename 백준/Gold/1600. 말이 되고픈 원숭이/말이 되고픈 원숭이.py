from collections import deque
import sys
input = sys.stdin.readline
K = int(input())
W, H = map(int, input().split())
arr = []
for _ in range(H):
  arr.append(list(map(int, input().split())))
visited = [[[0] * W for _ in range(H)] for _ in range(K + 1)]

mon = [(0, 1), (0, -1), (1, 0), (-1, 0)]

hor = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1
flag = False

while q:
  k, y, x = q.popleft()

  if (y == H - 1 and x == W - 1):
    flag = True
    print(visited[k][y][x] - 1)
    break

  for yy, xx in mon:
    ny, nx = y + yy, x + xx
    if (0 <= ny < H and 0 <= nx < W and arr[ny][nx] == 0 and visited[k][ny][nx] == 0):
      visited[k][ny][nx] = visited[k][y][x] + 1
      q.append((k, ny, nx))

  if (k < K):
    for yy, xx in hor:
      ny, nx = y + yy, x + xx
      if (0 <= ny < H and 0 <= nx < W and arr[ny][nx] == 0 and visited[k + 1][ny][nx] == 0):
        visited[k + 1][ny][nx] = visited[k][y][x] + 1
        q.append((k + 1, ny, nx))

if not flag:
  print(-1)
