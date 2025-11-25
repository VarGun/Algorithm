N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 1. 진행하다가 자기보다 1 작은 애 만나면 : 2칸 연속으로 가능인지 확인
# 1 - 2. 2 이상 작은 애 만나면 ? -> return false 해도 될듯
# 2. 큰 애 만나면 : 자기 위로 2칸 연속으로 가능인지 확인
# 2 - 2. 마찬가지로 2 이상 큰 애 만나면 -> return false 해도 될듯
# @@@@@ 겹치는 경우도 생각
ans = 0


def check_down(y, x, tar, line):  # 아래로 체크
  t = 0
  while (y + t < N and t < L):
    t += 1
    if (y + t >= N or board[y + t][x] != tar or line[y + t] == True):
      return False
    line[y + t] = True
  return True


def check_up(y, x, tar, line):
  t = 0
  while (y - t >= 0 and t < L):
    t += 1
    if (y - t < 0 or board[y - t][x] != tar or line[y - t] == True):
      return False
    line[y - t] = True
  return True


def check_right(y, x, tar, line):
  t = 0
  while (x + t < N and t < L):
    t += 1
    if (x + t >= N or board[y][x + t] != tar or line[x + t] == True):
      return False
    line[x + t] = True
  return True


def check_left(y, x, tar, line):
  t = 0
  while (x - t >= 0 and t < L):
    t += 1
    if (x - t < 0 or board[y][x - t] != tar or line[x - t] == True):
      return False
    line[x - t] = True
  return True


for y in range(N):
  is_valid_line = True
  line = [False for _ in range(N)]
  for x in range(N - 1):
    if (board[y][x] - 1 == board[y][x + 1]):  # 1 만큼 작은 애 만나면
      flag = check_right(y, x, board[y][x + 1], line)
      if (not flag):
        is_valid_line = False
        break
    elif (board[y][x] + 1 == board[y][x + 1]):  # 1 만큼 큰 애 만나면
      flag = check_left(y, x + 1, board[y][x], line)
      if (not flag):
        is_valid_line = False
        break
    elif (board[y][x] - 2 >= board[y][x + 1]):
      is_valid_line = False
      break
    elif (board[y][x] + 2 <= board[y][x + 1]):
      is_valid_line = False
      break
  if (is_valid_line):
    ans += 1

for x in range(N):
  is_valid_line = True
  line = [False for _ in range(N)]
  for y in range(N - 1):
    if (board[y][x] - 1 == board[y + 1][x]):  # 1 만큼 작은 애 만나면
      flag = check_down(y, x, board[y + 1][x], line)
      if (not flag):
        is_valid_line = False
        break
    elif (board[y][x] + 1 == board[y + 1][x]):  # 1 만큼 큰 애 만나면
      flag = check_up(y + 1, x, board[y][x], line)
      if (not flag):
        is_valid_line = False
        break
    elif (board[y][x] - 2 >= board[y + 1][x]):
      is_valid_line = False
      break
    elif (board[y][x] + 2 <= board[y + 1][x]):
      is_valid_line = False
      break
  if (is_valid_line):
    ans += 1

print(ans)
