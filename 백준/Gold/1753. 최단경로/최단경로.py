import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = 10e8
graph = [[] for _ in range(V + 1)]
dis = [INF for _ in range(V + 1)]
for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((w, v))
heap = []


def dij(s):
  dis[s] = 0
  heapq.heappush(heap, (0, s))
  while heap:
    weight, cur = heapq.heappop(heap)
    if (dis[cur] < weight):
      continue
    for w, next_n in graph[cur]:
      next_w = w + weight
      if (next_w < dis[next_n]):
        dis[next_n] = next_w
        heapq.heappush(heap, (next_w, next_n))


dij(K)
for i in range(1, V + 1):
  print(dis[i] if dis[i] != INF else "INF")
