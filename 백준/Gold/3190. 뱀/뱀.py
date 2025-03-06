import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

k = int(input())
for _ in range(k): # 사과
  x,y = map(int,input().split())
  arr[x][y] = 2

com = {} # 명령어 dir
l = int(input())

for _ in range(l): 
  sec, direct = input().split()
  com[int(sec)] = direct

t = 0
direction = [[1, 0],[0, 1], [-1, 0], [0, -1]]
x, y = 1, 1
arr[y][x] = 1
d = 0
q = deque([(1, 1)])

while True:
  t += 1

  dx, dy = x + direction[d][0], y + direction[d][1]

  if dx <= 0 or dy <= 0 or dx > n or dy > n or (dx, dy) in q:
    break

  if arr[dy][dx]!=2:
    a,b = q.popleft()
    arr[b][a]=0
  
  x, y = dx, dy
  arr[y][x] = 1
  q.append((dx, dy))

  if t in com.keys():
    if com[t] == "D":
      d = (d+1)%4
    else:
      d = (d - 1) % 4

print(t)