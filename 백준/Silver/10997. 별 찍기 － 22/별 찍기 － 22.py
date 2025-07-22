N = int(input())

arr = [[' ' for _ in range(4 * N - 3)] for _ in range(4 * N - 1)]


def rec(c, num):
  global arr, N

  if (num == 1):
    for i in range(c, c + 3):
      arr[c][i] = '*'
      arr[i][c] = '*'
  else:
    for i in range(c, c + 4 * num - 1):
      arr[i][c] = '*'
    for i in range(c + 2, c + 4 * num - 1):
      arr[i][c + 4 * num - 4] = '*'
    for i in range(c, c + 4 * num - 3):
      arr[c][i] = '*'
      arr[c + 4 * num - 2][i] = '*'
    if (num != N):
      arr[c][c + 4 * num - 3] = '*'

    rec(c + 2, num - 1)


if (N == 1):
  print('*')
else:
  rec(0, N)
  for line in map("".join, arr):
    print(line.rstrip())
