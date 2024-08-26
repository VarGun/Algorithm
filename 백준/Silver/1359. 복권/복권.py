import math

N, M, K = map(int, input().split())

def comb(n, r):
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def prob(n, m, k):
    return comb(m, k) * comb(n - m, m - k) / comb(n, m)

res = 0
for i in range(K, M + 1):
    res += prob(N, M, i)

print(res)
