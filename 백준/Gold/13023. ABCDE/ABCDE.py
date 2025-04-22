import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nodes = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  nodes[a].append(b)
  nodes[b].append(a)

ans = 0

def backT(nodeNum, depth):
  global ans, nodes
  
  if(ans == 1): # 이미 답이 나왔을 경우
    return
  
  if(depth == 5):
    ans = 1
    return

  visited[nodeNum] = 1
  for i in nodes[nodeNum]:
    if(visited[i] == 0 and len(nodes[i]) != 0):
      backT(i, depth + 1)
      visited[i] = 0

for i in range(n):
  visited = [False for _ in range(2001)] # 최대 n (사람 수) = 2000
  if(ans == 0):
    backT(i, 1)
  else:
    print(1)
    break

if(ans == 0):
  print(0)