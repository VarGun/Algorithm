from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
_max = -1

for _ in range(m):
  a, b = map(int, input().split())
  arr[b].append(a)

cnt_list = []

def bfs(num):
  q = deque()
  q.append(num)
  visited = [0 for _ in range(n + 1)]
  visited[num] = 1
  cnt = 1

  while q:
    head = q.popleft()

    next = arr[head]
    for i in next:
      if(visited[i] == 0):
        q.append(i)
        cnt += 1
        visited[i] = 1

  return cnt

tmp_q = []

_max = 0

for i in range(1, n + 1):
  gugu = bfs(i)
  if(_max == gugu):
    tmp_q.append(i)
  elif(_max < gugu):
    _max = gugu
    tmp_q = []
    tmp_q.append(i)

print(*tmp_q)