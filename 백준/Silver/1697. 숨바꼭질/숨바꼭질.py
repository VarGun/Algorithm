from collections import deque

n, m = map(int, input().split())

visited = [-1] * (10 ** 5 + 1)

def bfs(n):
  q = deque()
  q.append(n)
  visited[n] = 0
  while q:
    head = q.popleft()
    if(head == m):
      print(visited[head])
      return

    pos = [head * 2, head + 1, head - 1]
    for i in pos:
      if(0 <= i <= (10 ** 5) and visited[i] == -1):
        q.append(i)
        visited[i] = visited[head] + 1

bfs(n)