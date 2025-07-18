n = int(input())
gun = ['***', '* *', '***']
ans = []


def rec(num, tar):
  global gun, n, ans
  if (num == n):
    ans = tar
    return

  arr = []
  for i in range(num):
    arr.append(tar[i] * 3)
  for i in range(num):
    arr.append(tar[i] + ' ' * num + tar[i])
  for i in range(num):
    arr.append(tar[i] * 3)

  rec(num * 3, arr)


if (n == 3):
  for i in range(3):
    print(gun[i])
else:
  rec(3, gun)
  for i in range(len(ans)):
    print(ans[i])
