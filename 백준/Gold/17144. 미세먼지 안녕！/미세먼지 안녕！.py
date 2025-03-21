import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

up = -1
down = -1
# 공기 청정기 위치 찾기
for i in range(r):
  if arr[i][0] == -1:
    up = i
    down = i + 1
    break

# 미세먼지 확산
def spread():
  dx = [-1, 0, 0, 1]
  dy = [0, -1, 1, 0]

  tmp_arr = [[0] * c for _ in range(r)]
  for i in range(r):
    for j in range(c):
      if arr[i][j] != 0 and arr[i][j] != -1:
        tmp = 0
        for k in range(4):
          nx = dx[k] + i
          ny = dy[k] + j
          if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
            tmp_arr[nx][ny] += arr[i][j] // 5
            tmp += arr[i][j] // 5
        arr[i][j] -= tmp

  for i in range(r):
    for j in range(c):
      arr[i][j] += tmp_arr[i][j]


# 작동
def operate_air(start, dx, dy):
  direct = 0
  before = 0
  x, y = start, 1
  while True:
    nx = x + dx[direct]
    ny = y + dy[direct]
    if x == start and y == 0:
      break
    if nx < 0 or nx >= r or ny < 0 or ny >= c:
      direct += 1
      continue
    arr[x][y], before = before, arr[x][y]
    x = nx
    y = ny
  

for _ in range(t):
  spread()
  operate_air(up, [0, -1, 0, 1], [1, 0, -1, 0]) # 작동 - 위
  operate_air(down, [0, 1, 0, -1], [1, 0, -1, 0]) # 작동 - 아래

answer = 0
for i in range(r):
  for j in range(c):
    if arr[i][j] > 0:
      answer += arr[i][j]

print(answer)