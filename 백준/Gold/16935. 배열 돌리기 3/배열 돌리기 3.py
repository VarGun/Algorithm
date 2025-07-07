n, m, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
com = list(map(int, input().split()))


def rotate_1(arr):  # 상하 반전
  tmp_arr = []
  col_len = len(arr)
  for i in range(col_len - 1, -1, -1):
    tmp_arr.append(arr[i])
  return tmp_arr


def rotate_2(arr):  # 좌우 반전
  tmp_arr = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
  row_len = len(arr[0])
  col_len = len(arr)
  for i in range(row_len - 1, -1, -1):
    for j in range(col_len):
      tmp_arr[j][row_len - i - 1] = arr[j][i]
  return tmp_arr


def rotate_3(arr):  # 시계 방향
  _min = min(len(arr), len(arr[0]))  # 둘 중 작은 길이
  row_len = len(arr[0])  # m
  col_len = len(arr)  # n
  tmp_arr = [[0 for _ in range(col_len)] for _ in range(row_len)]
  for i in range(_min // 2):
    up = arr[i][i: row_len - i]
    down = arr[col_len - i - 1][i: row_len - i]
    left = [arr[j][i] for j in range(i, col_len - i)]
    right = [arr[j][row_len - i - 1] for j in range(i, col_len - i)]
    for j in range(i, row_len - i):
      # up -> left
      tmp_arr[j][col_len - i - 1] = up[j - i]
      # down -> right
      tmp_arr[j][i] = down[j - i]
    for j in range(i, col_len - i):
      # left -> up
      tmp_arr[i][j] = left[col_len - i - j - 1]
      # right -> down
      tmp_arr[row_len - i - 1][j] = right[col_len - i - j - 1]

  return tmp_arr


def rotate_4(arr):  # 반시계 방향
  _min = min(len(arr), len(arr[0]))  # 둘 중 작은 길이
  row_len = len(arr[0])  # m
  col_len = len(arr)  # n
  tmp_arr = [[0 for _ in range(col_len)] for _ in range(row_len)]
  for i in range(_min // 2):
    up = arr[i][i: row_len - i]
    down = arr[col_len - i - 1][i: row_len - i]
    left = [arr[j][i] for j in range(i, col_len - i)]
    right = [arr[j][row_len - i - 1] for j in range(i, col_len - i)]

    for j in range(i, row_len - i):
      # up -> right
      tmp_arr[j][i] = up[row_len - j - i - 1]
      # down -> left
      tmp_arr[j][col_len - i - 1] = down[row_len - j - i - 1]

    for j in range(i, col_len - i):
      # right -> up
      tmp_arr[i][j] = right[j - i]
      # left -> down
      tmp_arr[row_len - i - 1][j] = left[j - i]

  return tmp_arr


def rotate_5(arr):
  row_len = len(arr[0])  # m
  col_len = len(arr)  # n
  sec1 = [[arr[i][j] for j in range(row_len // 2)] for i in range(col_len // 2)]
  # 3 -> 1
  for i in range(col_len // 2):
    for j in range(row_len // 2):
      arr[i][j] = arr[i + col_len // 2][j]
  # 4 -> 3
  for i in range(col_len // 2, col_len):
    for j in range(row_len // 2):
      arr[i][j] = arr[i][j + row_len // 2]

  # 2 -> 4
  for i in range(col_len // 2, col_len):
    for j in range(row_len // 2, row_len):
      arr[i][j] = arr[i - col_len // 2][j]

  # sec1 -> 2
  for i in range(col_len // 2):
    for j in range(row_len // 2):
      arr[i][j + row_len // 2] = sec1[i][j]
  return arr


def rotate_6(arr):
  row_len = len(arr[0])  # m
  col_len = len(arr)  # n
  sec1 = [[arr[i][j] for j in range(row_len // 2)] for i in range(col_len // 2)]
  # 2 -> 1
  for i in range(col_len // 2):
    for j in range(row_len // 2):
      arr[i][j] = arr[i][j + row_len // 2]

  # 4 -> 2
  for i in range(col_len // 2):
    for j in range(row_len // 2, row_len):
      arr[i][j] = arr[i + col_len // 2][j]

  # 3 -> 4
  for i in range(col_len // 2, col_len):
    for j in range(row_len // 2, row_len):
      arr[i][j] = arr[i][j - row_len // 2]

  # sec1 -> 3
  for i in range(col_len // 2):
    for j in range(row_len // 2):
      arr[i + col_len // 2][j] = sec1[i][j]
  return arr


for i in range(len(com)):
  if (com[i] == 1):
    arr = rotate_1(arr)
  elif (com[i] == 2):
    arr = rotate_2(arr)
  elif (com[i] == 3):
    arr = rotate_3(arr)
  elif (com[i] == 4):
    arr = rotate_4(arr)
  elif (com[i] == 5):
    arr = rotate_5(arr)
  else:
    arr = rotate_6(arr)

for i in range(len(arr)):
  for j in range(len(arr[i])):
    print(arr[i][j], end=' ')
  print()
