n, k = map(int, input().split())

d = sorted([int(x) for x in input().split()])

print(d[k - 1])
