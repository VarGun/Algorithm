from collections import deque
n, m, k = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(n)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
fire_q = deque()  # 화염 저장 큐
task_q = deque()  # 처리 필요한 위치 저장 큐
visited = [[0 for _ in range(n)] for _ in range(n)]  # 처리할 위치 중복 방지
for _ in range(m):
  r, c, m, s, d = map(int, input().split())
  board[r - 1][c - 1] += 1
  if (board[r - 1][c - 1] >= 2 and visited[r - 1][c - 1] == 0):  # 2 개 이상이고, 아직 큐에 안들어감
    task_q.append([r - 1, c - 1])  # 처리 필요한 칸
    visited[r - 1][c - 1] = 1  # 처리 필요한 칸 중복 방지
  fire_q.append([r - 1, c - 1, m, s, d])  # 질량, 속도, 방향

while k:
  k -= 1
  # 이동
  sum_m = 0  # 질량 합
  new_board = [[[] for _ in range(n)] for _ in range(n)]  # 실제 저장
  len_fire = len(fire_q)
  visited = [[0 for _ in range(n)] for _ in range(n)]  # 처리할 위치 중복 방지
  while fire_q:
    head = fire_q.popleft()  # [r, c, 질량, 속도, 방향]
    r, c, m, s, d = head[0], head[1], head[2], head[3], head[4]
    r = (r + (dy[d] * (s % n))) % n
    c = (c + (dx[d] * (s % n))) % n
    new_fire = [r, c, m, s, d]
    new_board[r][c].append(new_fire)
    if (len(new_board[r][c]) >= 2 and visited[r][c] == 0):
      task_q.append([r, c])  # 처리해야할 위치 추가
      visited[r][c] = 1  # 처리해야할 위치 중복 방지

  # 합쳐지는 작업 필요할 경우
  if (len(task_q) >= 0):
    while task_q:
      head = task_q.popleft()  # r, c
      target_len = len(new_board[head[0]][head[1]])
      target_len_2 = len(new_board[head[0]][head[1]])  # 칸의 총 갯수 저장
      # new_board[head[0]][head[1]] : 가, 세, 질, 속, 방
      new_m = 0  # 새 질량
      new_s = 0  # 새 속도
      new_d_l = [0, 0]  # 짝 홀
      while target_len:
        target_len -= 1
        new_head = new_board[head[0]][head[1]].pop()  # 가, 세, 질, 속, 방
        new_m += new_head[2]  # 질량
        new_s += new_head[3]  # 속도
        new_d_l[new_head[4] % 2] += 1  # 짝수일 경우 0 에, 아닐 경우 1 에
      new_m = new_m // 5
      if (new_m == 0):
        continue
      new_s = new_s // target_len_2
      new_d = [0, 2, 4, 6] if new_d_l[0] == 0 or new_d_l[1] == 0 else [1, 3, 5, 7]
      for i in range(4):
        new_board[head[0]][head[1]].append([head[0], head[1], new_m, new_s, new_d[i]])

  sum_f = 0
  for i in range(n):
    for j in range(n):
      for f in new_board[i][j]:
        fire_q.append(f)
        sum_f += f[2]
  if (k == 0):
    print(sum_f)
