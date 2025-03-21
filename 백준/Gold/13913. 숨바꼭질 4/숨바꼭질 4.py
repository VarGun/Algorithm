from collections import deque
n, k = map(int, input().split())

_max = 10 ** 6

def bfs(num):
  global k
  q = deque()
  q.append(num)
  visited = [0 for _ in range(_max + 1)]
  parent = [0 for _ in range(_max + 1)]
  parent[num] = num
  while q:
    head = q.popleft()
    if(head == k):
      print(visited[head])
      ans = []
      for i in range(visited[head] + 1):
        ans.append(head)
        head = parent[head]
      ans.reverse()
      print(*ans)
      return
    next = [head - 1, head + 1, head * 2]
    for i in next:
      if(0 <= i <= _max and visited[i] == 0):
        q.append(i)
        visited[i] = visited[head] + 1
        parent[i] = head

bfs(n)