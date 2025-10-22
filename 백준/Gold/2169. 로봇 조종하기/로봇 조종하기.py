N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 맨 윗줄 세팅
for i in range(1, M):
  board[0][i] = board[0][i - 1] + board[0][i]

for i in range(1, N):
  left_tmp = board[i][:]
  left_tmp[-1] += board[i - 1][-1]
  right_tmp = board[i][:]
  right_tmp[0] += board[i - 1][0]

  for j in range(1, M):
    left_tmp[M - j - 1] += max(left_tmp[M - j], board[i - 1][M - j - 1])
    right_tmp[j] += max(right_tmp[j - 1], board[i - 1][j])
  for j in range(M):
    board[i][j] = max(left_tmp[j], right_tmp[j])
print(board[N - 1][M - 1])
