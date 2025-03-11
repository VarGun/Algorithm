from collections import deque

n, m = map(int, input().split())
flag = False
ans = -1
def bfs(num):
  global m, ans
  q = deque()
  q.append([num, 1])
  while q:
    head = q.popleft()
    num = head[0]
    cnt = head[1]
    if(num == m):
      ans = cnt
      return
    pos = [num * 10 + 1, num * 2]
    
    for i in pos:
      if(i <= m):
        q.append([i, cnt + 1])

bfs(n)
print(ans)