N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def rec(n, r, c):
  if (n == 1):
    return arr[r][c]
  else:
    tmp = []
    tmp.append(rec(n // 2, r, c))
    tmp.append(rec(n // 2, r + n // 2, c))
    tmp.append(rec(n // 2, r, c + n // 2))
    tmp.append(rec(n // 2, r + n // 2, c + n // 2))
    return sorted(tmp)[1]


print(rec(N, 0, 0))
