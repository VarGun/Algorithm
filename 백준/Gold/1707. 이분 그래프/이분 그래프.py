from collections import deque
import sys
input = sys.stdin.readline


def bfs(num, visited):
  q = deque()
  q.append(num)
  while q:
    head = q.popleft()  # head = 1
    for i in range(len(gun[head])):
      if (visited[gun[head][i]] == 0):  # 방문하지 않았을 경우
        if (visited[head] == 1):
          visited[gun[head][i]] = -1
        else:
          visited[gun[head][i]] = 1
        q.append(gun[head][i])
      elif (visited[head] == visited[gun[head][i]]):
        return False
  return True


K = int(input())
while K:
  K -= 1
  V, E = map(int, input().split())
  gun = [[] for _ in range(V + 1)]
  visited = [0 for _ in range(V + 1)]

  for _ in range(E):
    v1, v2 = map(int, input().split())
    gun[v1].append(v2)
    gun[v2].append(v1)
  flag = False
  for i in range(1, V + 1):
    if (visited[i] == 0):
      flag = bfs(i, visited)
      if (not flag):
        break
  print('YES' if flag else 'NO')
