import sys
input = sys.stdin.readline

def solution(n, arr):
  d = [[arr[0][0], arr[0][1], arr[0][2]]]
  for i in range(1, n):
    d.append([arr[i][0] + min(d[i - 1][1], d[i - 1][2]), arr[i][1] + min(d[i - 1][0], d[i - 1][2]), arr[i][2] + min(d[i - 1][0], d[i - 1][1])])
  print(min(d[n-1]))


n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))
solution(n, arr)