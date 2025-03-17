from collections import deque

n = int(input())
arr = []
_max = 10 ** 4

com = ['D', 'S', 'L', 'R']

for i in range(n):
  a, b = input().split()
  arr.append([a, b])

def bfs(num, tar):
  q = deque()
  q.append([num, ''])
  visited = [False for _ in range(_max + 1)]
  visited[int(num)] = True
  while q:
    head = q.popleft()
    num, command = head[0], head[1]

    if(num == tar):
      print(command)
      return 
    
    next = [num * 2 % 10000, (num - 1) % 10000, num // 1000 + (num % 1000) * 10, num // 10 + (num % 10) * 1000]
    for i in range(4):
       if(visited[next[i]] == False):
          visited[next[i]] = True
          q.append([next[i], command + com[i]])

for i in range(n):
  a, b = arr[i][0], arr[i][1]
  bfs(int(a), int(b))