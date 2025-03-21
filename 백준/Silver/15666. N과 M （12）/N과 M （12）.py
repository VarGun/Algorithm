n, m = map(int, input().split())
arr = sorted(set(list(map(int, input().split()))))
ans = []

def backT(depth, idx):
  global ans

  if(len(ans) == m):
    print(*ans)
    return

  for i in range(idx, len(arr)):
    ans.append(arr[i])
    backT(depth + 1, i)
    ans.pop()

backT(0, 0)