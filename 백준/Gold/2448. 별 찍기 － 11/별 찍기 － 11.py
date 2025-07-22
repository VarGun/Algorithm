base = ['  *  ', ' * * ', '*****']

N = int(input())

arr = [[' ' for _ in range(N * 2 - 1)] for _ in range(N)]


def rec(i, j, num):
  global arr
  if (num == 3):
    arr[i][j] = '*'
    arr[i + 1][j - 1] = arr[i + 1][j + 1] = '*'
    for k in range(-2, 3):
      arr[i + 2][j + k] = '*'
  else:
    num2 = num // 2
    rec(i, j, num2)
    rec(i + num2, j + num2, num2)
    rec(i + num2, j - num2, num2)


rec(0, N - 1, N)
for i in range(N):
  print(''.join(arr[i]))
