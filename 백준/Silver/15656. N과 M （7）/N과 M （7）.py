n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
ans = []
def backT():
  global ans
  if(len(ans) == m):
    print(*ans)
    return
  for i in range(n):
    ans.append(arr[i])
    backT()
    ans.pop()

backT()
