import sys

input = sys.stdin.readline
r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
_max = 1
path = set()

def dfs(y, x, depth):
  global arr, _max, dy, dx

  _max = max(_max, depth)

  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if (0 <= ny < r and 0 <= nx < c and not arr[ny][nx] in path):
      path.add(arr[ny][nx])
      dfs(ny, nx, depth + 1)
      path.remove(arr[ny][nx])

path.add(arr[0][0])
dfs(0, 0, 1)
print(_max)
