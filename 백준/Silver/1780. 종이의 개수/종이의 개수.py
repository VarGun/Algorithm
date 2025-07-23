import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0, 0]


def rec(board, size, r, c):
  global ans
  if (size == 1):
    ans[board[r][c]] += 1
    return
  _sum = 0
  tar = board[0][0]  # 기준
  tar_flag = False

  for i in range(len(board)):
    _sum += sum(board[i])
    for j in range(len(board[i])):
      if (tar != board[i][j]):
        tar_flag = True
        break
    if (tar_flag):
      break
  if (not tar_flag):  # 전부 같을 경우
    if (_sum == 0):
      ans[0] += 1
    elif (_sum == -1 * (size ** 2)):
      ans[-1] += 1
    elif (_sum == size ** 2):
      ans[1] += 1
    return
  else:
    # 9등분 ..
    board1 = []
    board2 = []
    board3 = []
    board4 = []
    board5 = []
    board6 = []
    board7 = []
    board8 = []
    board9 = []
    slength = size // 3
    for i in range(r, r + slength):
      board1.append(board[i][c:c + slength])
      board2.append(board[i][c + slength: c + (slength * 2)])
      board3.append(board[i][c + (slength * 2): c + size])
    for i in range(r + slength, r + (slength * 2)):
      board4.append(board[i][c:c + slength])
      board5.append(board[i][c + slength: c + (slength * 2)])
      board6.append(board[i][c + (slength * 2): c + size])
    for i in range(r + (slength * 2), r + size):
      board7.append(board[i][c:c + slength])
      board8.append(board[i][c + slength: c + (slength * 2)])
      board9.append(board[i][c + (slength * 2): c + size])

    # rec(board, size, r, c)
    rec(board1, slength, 0, 0)
    rec(board2, slength, 0, 0)
    rec(board3, slength, 0, 0)
    rec(board4, slength, 0, 0)
    rec(board5, slength, 0, 0)
    rec(board6, slength, 0, 0)
    rec(board7, slength, 0, 0)
    rec(board8, slength, 0, 0)
    rec(board9, slength, 0, 0)


rec(arr, N, 0, 0)
print(ans[-1])
print(ans[0])
print(ans[1])
