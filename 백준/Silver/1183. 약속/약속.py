n = int(input())
diffs = sorted([int(a) - int(b) for a, b in (map(int, input().split()) for _ in range(n))])

result = 1 if n % 2 == 1 else abs(diffs[n//2] - diffs[n//2 - 1]) + 1
print(result)