import sys
import heapq
sys.setrecursionlimit(10**6)
T = int(input())
INF = int(1e9)
ans = []


def dij(s, graph):
  dis = [INF for _ in range(n + 1)]  # 거리
  dis[s] = 0
  heap = []
  heapq.heappush(heap, (0, s))
  while heap:
    weight, cur_node = heapq.heappop(heap)
    if dis[cur_node] < weight:
      continue
    for w, next_n in graph[cur_node]:
      next_w = w + weight
      if next_w < dis[next_n]:
        dis[next_n] = next_w
        path[next_n] = cur_node
        heapq.heappush(heap, (next_w, next_n))
  return dis


while T:
  T -= 1
  n, m, t = map(int, input().split())
  s, g, h = map(int, input().split())

  graph = [[] for _ in range(n + 1)]
  gh_w = None


  path = [-1 for _ in range(n + 1)]
  path[s] = s

  for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((d, b))
    graph[b].append((d, a))

    if (a == g and b == h) or (a == h and b == g):
      gh_w = d


  cands = [int(input()) for _ in range(t)]

  dis_s = dij(s, graph)
  dis_g = dij(g, graph)
  dis_h = dij(h, graph)

  ans = []
  for e in cands:
    if (dis_s[g] + gh_w + dis_h[e] == dis_s[e]) or (dis_s[h] + gh_w + dis_g[e] == dis_s[e]):
      ans.append(e)

  print(*sorted(ans))
