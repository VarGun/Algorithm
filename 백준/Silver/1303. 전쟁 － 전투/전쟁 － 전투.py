def dfs(x, y, visited):
  global cnt_w, cnt_b, sum_w, sum_b, stack

  if(visited[x][y]):
    return
  if(arr[x][y] == "W"):
    cnt_w += 1
  else:
    cnt_b += 1
  stack.append([x, y])
  visited[x][y] = True

  for d in direction:
    if(x + d[0] >= 0 and x + d[0] < m and y + d[1] >= 0 and y + d[1] < n):
      if(arr[x][y] == arr[x + d[0]][y + d[1]]):
        dfs(x + d[0], y + d[1], visited)
  stack.pop()
  if(len(stack) == 0):
    if(arr[x][y] == "W"):
      sum_w += cnt_w * cnt_w
      cnt_w = 0
    else:
      sum_b += cnt_b * cnt_b
      cnt_b = 0

  return


if __name__ == "__main__":
  n, m = map(int, input().split())
  stack = []
  sum_w = 0
  sum_b = 0
  arr = []
  for _ in range(m):
    arr.append(list(input()))
  visited = [[False for _ in range(n)] for _ in range(m)]
  cnt_w = 0
  cnt_b = 0
  direction = [[0, -1], [0, 1], [-1, 0], [1, 0]] # 상 하 좌 우
  for i in range(m):
    for j in range(n):
      dfs(i, j, visited)
  
  print(sum_w)
  print(sum_b)