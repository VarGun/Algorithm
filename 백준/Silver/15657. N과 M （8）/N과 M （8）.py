n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []

cnt = 0

def dfs(num):

  if(len(ans) == m):
    print(*ans)
    return
  
  for i in arr:
    if(i >= num):
      ans.append(i)
      dfs(i)
      ans.pop()

dfs(arr[0] - 1)