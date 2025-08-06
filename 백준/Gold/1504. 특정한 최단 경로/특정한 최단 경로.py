import sys
import heapq
input = sys.stdin.readline

INF = 10e8
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append((c, b))
  graph[b].append((c, a))
v1, v2 = map(int, input().split())


def dij(s):
  dis = [INF for _ in range(N + 1)]
  dis[s] = 0
  q = []
  heapq.heappush(q, (0, s))
  while q:
    w, cur_n = heapq.heappop(q)
    if (dis[cur_n] < w):
      continue
    for ww, next_n in graph[cur_n]:
      next_w = w + ww
      if (dis[next_n] > next_w):
        dis[next_n] = next_w
        heapq.heappush(q, (next_w, next_n))
  return dis


ans_start = 0
ans_end = 0
dis_one = dij(1)
dis_v1 = dij(v1)
dis_v2 = dij(v2)

ans_start += dis_one[v1] + dis_v1[v2] + dis_v2[N]
ans_end += dis_one[v2] + dis_v2[v1] + dis_v1[N]

if (ans_start >= INF and ans_end >= INF):
  print(-1)
else:
  print(min(ans_start, ans_end))
