import sys
input = sys.stdin.readline

N = int(input())

a = list(map(int, input().split()))

min_3 = min((a[0] + a[1] + a[2]), (a[0] + a[1] + a[3]), (a[0] + a[2] + a[4]), (a[0] + a[3] + a[4]), 
            (a[5] + a[1] + a[2]), (a[5] + a[1] + a[3]), (a[5] + a[2] + a[4]), (a[5] + a[3] + a[4]))

min_2 = min((a[0] + min(a[1], a[2], a[3], a[4])),
            (a[1] + min(a[2], a[3], a[5])),
            (a[2] + min(a[4], a[5])),
            (a[3] + min(a[4], a[5])),
            a[4] + a[5]
            )

min_1 = min(a)

ans = 0

cnt_2 = 4*(2*N - 3)

if(N == 1):
  ans += sum(a) - max(a)
else:
  ans += min_3 * 4 + min_2 * (cnt_2) + min_1 * ((N**2) * 5 - (cnt_2 * 2 + 12))

print(ans)