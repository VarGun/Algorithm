N = int(input())

arr = [[' ' for _ in range(4 * N - 3)] for _ in range(4 * N - 3)]


def rec(c, num):
  global arr
  if (num == 1):
    arr[c][c] = '*'
  else:
    for i in range(c, c + 4 * num - 3):
      arr[c][i] = '*'
      arr[i][c] = '*'
      arr[c + 4 * num - 4][i] = '*'
      arr[i][c + 4 * num - 4] = '*'
    rec(c + 2, num - 1)


rec(0, N)


for i in range(len(arr)):
  print(''.join(arr[i]))
