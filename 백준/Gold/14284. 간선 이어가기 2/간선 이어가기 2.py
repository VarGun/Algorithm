import sys
import heapq
input = sys.stdin.readline
INF = 10e8
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dis = [INF for _ in range(N + 1)]
for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a].append((c, b))
  graph[b].append((c, a))

def dij(s):
  global dis
  dis[s] = 0
  q = []
  heapq.heappush(q, (0, s))
  while q:
    cur_w, cur_n = heapq.heappop(q)
    if (cur_w > dis[cur_n]):
      continue
    for weight, next_n in graph[cur_n]:
      next_w = cur_w + weight
      if (dis[next_n] > next_w):
        dis[next_n] = next_w
        heapq.heappush(q, (next_w, next_n))


S, T = map(int, input().split())
dij(S)
print(dis[T])