from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())

arr = [[] for _ in range(n + 1)]

visited = [9999999 for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  arr[a].append(b)

flag = False
ans = []
def bfs(num):
  global k, visited, flag
  q = deque()
  q.append(num)
  visited[num] = 0
  while q:
    head = q.popleft()
    c = arr[head] # [2, 3]
    if(visited[head] == k):
      flag = True
      ans.append(head)
    for i in c:
      if(visited[i] > visited[head] + 1):
        q.append(i)
        visited[i] = visited[head] + 1

bfs(x)
ans.sort()
if(flag):
  for i in range(len(ans)):
    print(ans[i])
else:
  print(-1)
