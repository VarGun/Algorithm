n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
ans_total = set()

def backT(depth):
  global ans
  if(len(ans) == m):
    ans_total.add(tuple(ans))
    return
  for i in range(0, n):
    ans.append(arr[i])
    backT(depth + 1)
    ans.pop()

backT(0)
ans_total = list(ans_total)
ans_total.sort()
for i in range(len(ans_total)):
  print(*list(ans_total[i]))