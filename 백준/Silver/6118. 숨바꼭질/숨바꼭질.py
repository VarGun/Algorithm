from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  arr[a].append(b)
  arr[b].append(a)


def bfs(num):
  global arr
  visited = [0 for _ in range(n + 1)]
  visited[num] = 1
  q = deque()
  q.append(num)
  cnt = 0
  while q:
    head = q.popleft()
    next = arr[head]
    for i in next:
      if(visited[i] == 0):
        q.append(i)
        visited[i] = visited[head] + 1
  
  _max = 0
  ans = []
  for i in range(1, len(visited)):
    if(visited[i] > _max):
      ans = []
      ans.append(i)
      _max = visited[i]
    elif(visited[i] == _max):
      ans.append(i)
  
  print(ans[0], _max - 1, len(ans))

bfs(1)