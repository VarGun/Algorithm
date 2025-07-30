n = int(input())


def gun(num, s, e):
  if (num == 1):
    print(s, e)
    return
  nn = 6 - s - e
  gun(num - 1, s, nn)
  print(s, e)
  gun(num - 1, nn, e)


print(2 ** n - 1)
gun(n, 1, 3)
