from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
T = input()
if (len(T) == 1):
  print(M)
  exit(0)
pers = list(map(int, T.split()))[1:]  # 진실 아는 사람들
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
party = []
for i in range(1, M + 1):
  line = list(map(int, input().split()))[1:]
  party.append(line)
  for j in range(len(line)):
    for k in range(len(line)):
      if (j != k):
        graph[line[k]].append(line[j])

def bfs(num):
  global graph, visited
  q = deque([num])
  while q:
    head = q.popleft()  # 사람의 숫자
    for i in graph[head]:
      if (visited[i] == 0):
        visited[i] = 1
        q.append(i)


for i in range(len(pers)):
  visited[pers[i]] = 1
  bfs(pers[i])

ans = 0
for i in range(len(party)):
  tar = party[i]
  flag = False
  for j in tar:
    if (visited[j] == 1):
      flag = True
      break
  if (not flag):
    ans += 1
print(ans)
