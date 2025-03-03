n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
visited = [False for _ in range(n)]

def dfs():
  num = 0
  if(len(ans) == m):
    print(*ans)
    return
  
  for i in range(len(arr)):
    if(not visited[i] and arr[i] != num):
      ans.append(arr[i])
      visited[i] = True
      num = arr[i]
      dfs()
      ans.pop()
      visited[i] = False

dfs()