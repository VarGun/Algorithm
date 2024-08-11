import sys
input = sys.stdin.readline

n = int(input().strip())
friendship = [input().strip() for _ in range(n)]

friend = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if friendship[i][j] == 'Y':
            friend[i][j] = 1
        else:
            friend[i][j] = any(friendship[i][k] == 'Y' and friendship[k][j] == 'Y' for k in range(n) if k != i)

most_popular = max(sum(row) for row in friend)
print(most_popular)
