from collections import deque
N = int(input())
arr = [[] for _ in range(N + 1)]
score = [0 for _ in range(N + 1)]
while True:
  n, m = map(int, input().split())
  if (n == -1 and m == -1):
    break
  arr[n].append(m)
  arr[m].append(n)

_min = 2500
min_arr = []


def bfs(num):
  global min_arr, _min
  visited = [-1 for _ in range(N + 1)]
  _max = -1
  q = deque()
  q.append(num)
  visited[num] = 0
  while q:
    head = q.popleft()

    for i in arr[head]:
      if (visited[i] == -1):
        q.append(i)
        visited[i] = visited[head] + 1
        if (visited[i] > _max):
          _max = visited[i]
  if (_min == _max):
    min_arr.append(num)
  elif (_min > _max):
    _min = _max
    min_arr = [num]


for i in range(1, N + 1):
  bfs(i)
print(_min, len(min_arr))
print(*min_arr)
