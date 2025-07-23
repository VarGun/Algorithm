N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def rec(num, r, c):
  global arr
  if (num == 1):
    return arr[r][c]
  else:
    tmp = []
    tmp.append(rec(num // 2, r, c))
    tmp.append(rec(num // 2, r + num // 2, c))
    tmp.append(rec(num // 2, r, c + num // 2))
    tmp.append(rec(num // 2, r + num // 2, c + num // 2))
    return sorted(tmp)[2]


print(rec(N, 0, 0))
