from collections import deque
n, m = map(int, input().split())
_max = 10 ** 6

visited = [0 for _ in range(_max + 1)]
def bfs(num):
  global visited
  q = deque()
  q.append(num)
  visited[num] = 1

  while q:
    head = q.popleft()
    if(head == m):
      return
    for i in (head * 2, head - 1, head + 1):
      if(0 <= i < _max):
        if(visited[i] == 0):
          if(i == head * 2):
            visited[i] = visited[head]
          else:
            visited[i] = visited[head] + 1
          q.append(i)

bfs(n)
print(visited[m] - 1)