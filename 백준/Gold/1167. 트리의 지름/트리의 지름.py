import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
n = int(input())
arr = [[] for _ in range(n + 1)]

for _ in range(n):
  line = list(map(int, input().split()))
  tar = line[0]  # 대상 노드
  line = line[1:]
  for i in range(0, len(line), 2):
    if (line[i] == -1):
      break
    arr[tar].append([line[i], line[i + 1]])

visited = [-1 for _ in range(n + 1)]

_max = 0
max_i = 1

def dfs(tar):
  global visited, arr, _max, max_i
  tar_list = arr[tar]  # [[1, 2], [4, 3]]
  for i in tar_list:
    if (visited[i[0]] == -1):
      visited[i[0]] = visited[tar] + i[1]
      if (_max < visited[i[0]]):
        _max = visited[i[0]]
        max_i = i[0]
      dfs(i[0])

visited[1] = 0
dfs(1)

visited = [-1 for _ in range(n + 1)]
visited[max_i] = 0
_max = 0
dfs(max_i)

print(_max)
