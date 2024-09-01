N = int(input())
c = [[0] * 100 for _ in range(100)] 

for _ in range(N):
    y, x = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            c[i][j] = 1
area = sum(sum(row) for row in c)

print(area)