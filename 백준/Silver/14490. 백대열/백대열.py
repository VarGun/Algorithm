import math

n, m = map(int, input().split(":"))
g = math.gcd(n, m)
print(f"{n // g}:{m // g}")