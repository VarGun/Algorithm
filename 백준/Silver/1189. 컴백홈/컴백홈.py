import sys
input = sys.stdin.readline

def dfs(x, y, dist):
  if dist == k and x == 0 and y == c - 1:
    return 1
  
  g[x][y] = 'T'
  paths = 0
  
  for dx, dy in d:
    nx, ny = x + dx, y + dy
    
    if 0 <= nx < r and 0 <= ny < c and g[nx][ny] == '.':
      paths += dfs(nx, ny, dist + 1)
  
  g[x][y] = '.'
  
  return paths

if __name__ == "__main__":
  r, c, k = map(int, input().split())
  g = [list(input().strip()) for _ in range(r)]

  d = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 아래, 위, 오른쪽, 왼쪽

  result = dfs(r - 1, 0, 1)

  print(result)