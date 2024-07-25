import sys
input = sys.stdin.readline
from collections import deque

def dfs(n):
  print(n, end=" ")
  arr = g[n]
  for i in arr:
    if(not d_visit[i - 1]):
      d_visit[i - 1] = True
      dfs(i)

def bfs(n):
  while bfs_queue:
    tar = bfs_queue.popleft()
    print(tar, end=" ")
    for i in g[tar]:
      if(not b_visit[i - 1]):
        b_visit[i - 1] = True
        bfs_queue.append(i)
  
  
  


if __name__ == "__main__":
  N, M, V = map(int, input().split())

  d_visit  = [False for _ in range(N)]
  b_visit = [False for _ in range(N)]
  dfs_list = [V]
  g = [[] for _ in range(N + 1)]
  bfs_queue = deque([V])
    
  for _ in range(M):
    n, m = map(int, input().split())
    g[n].append(m)
    g[m].append(n)
  
  for i in g:
    i.sort()
  
  # print(*g)
  d_visit[V - 1] = True
  b_visit[V - 1] = True
  dfs(V)
  print()
  bfs(V)

# print(dict)
# print(bfs_queue)