N, K = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]

m.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(N):
    if m[i][0] == K:
        t = i
        break

for i in range(N):
    if m[t][1:] == m[i][1:]:
        print(i + 1)
        break