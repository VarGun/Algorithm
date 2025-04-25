import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
n = int(input())
if (n == 1):
  print(0)
  exit(0)

tree = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]
for _ in range(n - 1):
  p, c, d = map(int, input().split())
  tree[p].append([c, d])
  tree[c].append([p, d])

_max = -1
max_i = 1

def dfs(tar):
  global _max, max_i
  tar_dis = tree[tar]
  for i in tar_dis:  # [[2, 3], [3, 2]]
    if (visited[i[0]] == -1):
      visited[i[0]] = visited[tar] + i[1]
      if (_max < visited[i[0]]):
        _max = visited[i[0]]
        max_i = i[0]
      dfs(i[0])

visited[1] = 0
dfs(1)
_max = -1
visited = [-1 for _ in range(n + 1)]
visited[max_i] = 0
dfs(max_i)
print(_max)
