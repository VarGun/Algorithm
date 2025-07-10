n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []
def backT(ans):
  global m, nums
  if (len(ans) == m):
    print(*ans)
    return
  for i in range(n):
    if (len(ans) == 0 or (nums[i] not in ans and nums[i] > ans[- 1])):
      ans.append(nums[i])
      backT(ans)
      ans.pop()
backT(ans)