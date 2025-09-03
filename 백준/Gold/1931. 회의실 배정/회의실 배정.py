import sys
input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
  s, e = map(int, input().split())
  meetings.append([s, e])

meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 1
gugu = meetings[0][1]

for i in range(1, N):
  if (gugu <= meetings[i][0]):
    cnt += 1
    gugu = meetings[i][1]
print(cnt)
