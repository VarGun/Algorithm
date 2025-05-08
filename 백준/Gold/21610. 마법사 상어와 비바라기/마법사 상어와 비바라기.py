from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

com = [list(map(int, input().split())) for _ in range(m)]

# 좌 좌상 상 우상 우 우하 하 좌하
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud_q = deque([[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]])

for t in range(m):
  command = com[t]
  cloud_pos = [[0 for _ in range(n)] for _ in range(n)]
  new_cloud = []
  # 이동
  while cloud_q:
    head = cloud_q.popleft()
    ny = (head[0] + (dy[command[0] - 1] * command[1])) % n
    nx = (head[1] + (dx[command[0] - 1] * command[1])) % n
    cloud_pos[ny][nx] = 1  # 이동한 구름 위치 갱신 - 새로 구름 만들 때 필요
    new_cloud.append([ny, nx])  # 구름 위치 저장

  # 증가 (1)
  for i in range(len(new_cloud)):
    board[new_cloud[i][0]][new_cloud[i][1]] += 1

  # 증가 (대각선)
  for i in range(len(new_cloud)):
    tar = new_cloud[i]  # 타겟 구름
    for j in range(1, 8, 2):  # 대각선만 검사하도록
      ny = new_cloud[i][0] + dy[j]
      nx = new_cloud[i][1] + dx[j]
      if (0 <= ny < n and 0 <= nx < n and board[ny][nx] != 0):
        board[new_cloud[i][0]][new_cloud[i][1]] += 1

  # 구름 생성
  for i in range(n):
    for j in range(n):
      # 물의 양이 2 보다 많고 기존 구름 위치가 아닌 경우
      if (board[i][j] >= 2 and cloud_pos[i][j] != 1):
        cloud_q.append([i, j])
        board[i][j] -= 2

# 확인
ans = 0
for i in range(n):
  ans += sum(board[i])
print(ans)
