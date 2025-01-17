from collections import deque
import sys
input = sys.stdin.readline

def bfs(arr, start, visited):
  deq = deque([start])
  visited[start] = True

  while deq:
    v = deq.popleft()
    for i in (arr[v]):
      if(not visited[i]):
        deq.append(i)
        visited[i] = True

  return


if __name__ == "__main__":
  n, m = map(int, input().split())
  visited = [False for _ in range(n + 1)]
  # arr = [[] for _ in range(n + 1)]
  arr = [[] for _ in range(n + 1)]

  for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

  cnt = 0
  
  for i in range(1, len(arr)):
    if(not visited[i]):
      bfs(arr, i, visited)
      cnt += 1
  print(cnt)