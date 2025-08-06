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
    if (dis[cur_node] < weight):
      continue
    for w, next_n in graph[cur_node]:
      next_w = w + weight
      if (next_w < dis[next_n]):
        dis[next_n] = next_w
        path[next_n] = cur_node
        heapq.heappush(heap, (next_w, next_n))
  return dis

while T:
  T -= 1
  n, m, t = map(int, input().split())  # 노드 수, 간선 수, 목적지 후보 수
  s, g, h = map(int, input().split())  # 시작점, 경로 양쪽 노드 둘
  tar_list = [[g, h], [h, g]]
  graph = [[] for _ in range(n + 1)]  # 교차로 = 노드

  # 경로 [시작, 도착] 을 사용했는지
  path = [-1 for _ in range(n + 1)]
  path[s] = s
  for i in range(m):
    a, b, d = map(int, input().split())  # 양방향 + 가중치 추가
    graph[a].append([d, b])
    graph[b].append([d, a])
  cands = [int(input()) for _ in range(t)]
  dis_s = dij(s, graph)
  ans = []
  dis_g = dij(g, graph)
  dis_h = dij(h, graph)

  for i in range(len(cands)):
    if (dis_s[g] + dis_g[h] + dis_h[cands[i]] == dis_s[cands[i]] or dis_s[h] + dis_h[g] + dis_g[cands[i]] == dis_s[cands[i]]):
      ans.append(cands[i])
  tmp = sorted(ans)
  print(*tmp)
