from collections import deque
n, k = map(int, input().split())
_max = 10 ** 6
cnt_all = 0
ans = 0
def bfs(num):
  global ans, cnt_all
  q = deque()
  q.append(n)
  visited = [0 for _ in range(_max + 1)]

  while q:
    num = q.popleft()
    ans_tmp = visited[num]
    if(num == k):
      ans = ans_tmp
      cnt_all += 1
      continue
    next = [num - 1, num + 1, num * 2]
    for i in next:
      if(0 <= i < _max + 1 and (visited[i] == 0 or visited[i] == visited[num] + 1)):
        q.append(i)
        visited[i] = visited[num] + 1
bfs(n)
print(ans)
print(cnt_all)