def dfs(d, idx):
  if (d == 6):
    print(*ans)
    return
  
  for i in range(idx, k):
    ans.append(nums[i])
    dfs(d + 1, i + 1)
    ans.pop()


while(True):
  arr = list(map(int, input().split()))
  k = arr[0]
  nums = arr[1:]
  ans = []
  dfs(0, 0)
  if(k == 0):
    exit()
  print()