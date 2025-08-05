import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N, M, R = map(int, input().split())
visited = [0 for _ in range(N + 1)]
arr = [[] for _ in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().split())
  arr[a].append(b)
  arr[b].append(a)

cnt = 1

def dfs(n):  # n : node, 정점
  global visited, arr, cnt
  visited[n] = cnt
  sorted_tmp = sorted(arr[n])
  for i in range(len(sorted_tmp)):
    if (visited[sorted_tmp[i]] == 0):
      cnt += 1
      dfs(sorted_tmp[i])

dfs(R)
for i in range(1, N + 1):
  print(visited[i])
