import math
n, m = map(int, input().split())

a = m - n

gc = math.gcd(a, m)

print(a // gc, m // gc)
