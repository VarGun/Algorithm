import sys

n = int(input())
ans = 0
col_list = [-1 for _ in range(n)]

def check(r):
  for i in range(r):
    if(col_list[i] == col_list[r] or r - i == abs(col_list[r] - col_list[i])): # 같은 행에 있는지 or 대각선 상에 있는지 (이전에 놓은 퀸들을 검사해서 위치 잡기)
      return False
  return True

def dfs(r):
  global n, ans

  if(r == n):
    ans += 1
    return
  
  for i in range(n):
    col_list[r] = i
    if(check(r)):
      dfs(r + 1)

dfs(0)
print(ans)