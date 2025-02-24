import sys
import math
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = []

for _ in range(n):
  arr.append(list(map(int, input().split())))

ans = 0
ans_flag = False # 인구 이동이 가능한지

while True:
  ans_flag = False
  graph = [[[] for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if(i == n - 1): # 맨 아래 줄
        if(j != n - 1): # 맨 오른쪽 줄이 아니면
          if(l <= abs(arr[i][j] - arr[i][j + 1]) <= r):
            ans_flag = True
            graph[i][j].append([i, j + 1])
            graph[i][j + 1].append([i, j])
      else:
        if(l <= abs(arr[i][j] - arr[i + 1][j]) <= r):
          ans_flag = True
          graph[i][j].append([i + 1, j])
          graph[i + 1][j].append([i, j])
        if(j != n - 1):
          if(l <= abs(arr[i][j] - arr[i][j + 1]) <= r):
            ans_flag = True
            graph[i][j].append([i, j + 1])
            graph[i][j + 1].append([i, j])

  if(not ans_flag):
    break

  visited = [[False for _ in range(n)]for _ in range(n)]

  cnt_flag = False
  cnt = 0 # 그래프 수
  graph_list = [[] for _ in range(n * n)]

  def dfs(i, j):
    global cnt_flag, cnt, q
    if(visited[i][j] == True or len(graph[i][j]) == 0):
      return
    visited[i][j] = True
    
    if(cnt_flag == False):
      cnt_flag = True
    else:
      graph_list[cnt].append([i, j])


    for node in graph[i][j]:
      dfs(node[0], node[1])

    return

  for i in range(n):
    for j in range(n):
      if(visited[i][j] == False and len(graph[i][j]) != 0):
        cnt_flag = False
        cnt += 1
        graph_list[cnt].append([i, j])
      dfs(i, j)

  for i in range(1, cnt + 1):
    sum = 0
    for node in graph_list[i]:
      sum += arr[node[0]][node[1]]
    new_value = math.floor(sum / len(graph_list[i]))
    for node in graph_list[i]:
      arr[node[0]][node[1]] = new_value

  ans += 1

print(ans)