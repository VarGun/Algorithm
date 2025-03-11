n = int(input())
a, b = map(int, input().split())

m = int(input())

arr = [[] for _ in range(n + 1)]

for i in range(m):
  x, y = map(int, input().split())
  arr[x].append(y)
  arr[y].append(x)

visited = [0 for _ in range(n + 1)]

depth = 0
flag = False

def dfs(num):
  global depth, flag

  if(visited[num] or flag):
    return

  if(num == b):
    flag = True
    return

  visited[num] = True
  for i in range(len(arr[num])):
    depth += 1
    dfs(arr[num][i])
    if(flag):
      return
    depth -= 1
  return

dfs(a)
if(flag):
  print(depth)
else:
  print(-1)
