n = int(input())

ans = 0
d = 1
s = 1

while s <= n:
  e = s * 10 - 1
  e = min(e, n)
  cnt = e - s + 1
  ans += cnt * d

  d += 1
  s *= 10

print(ans)