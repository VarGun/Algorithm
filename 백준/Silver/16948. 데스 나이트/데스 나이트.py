from collections import deque

def bfs(s_x, s_y, t_x, t_y):
  m_cnt = 0
  d = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]
  q = deque([(s_x, s_y)])

  while (q):
    cur_x, cur_y = q.popleft()
    if(cur_x == t_x and cur_y == t_y):
      print(g[cur_x][cur_y])
      return
    for i in range(6):
      n_x = cur_x +  d[i][0]
      n_y = cur_y + d[i][1]
      if(0 <= n_x < n and 0 <= n_y < n):
        if(g[n_x][n_y] == 0):
          m_cnt += 1
          q.append([n_x, n_y])
          g[n_x][n_y] = g[cur_x][cur_y] + 1
  
  print(-1)
  return

if __name__ == "__main__":
  n = int(input())
  s_x, s_y, t_x, t_y = map(int, input().split())
  g = [[0 for _ in range(n)] for _ in range(n)]
  bfs(s_x, s_y, t_x, t_y)
