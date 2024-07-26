import sys
input = sys.stdin.readline

N, M = map(int, input().split())

s_n = min(N, M)

ans = 1

arr = [[] for _ in range(N)]

for i in range(N):
  str = input()
  for j in range(M):
    arr[i].append(str[j])

for i in range(N - 1):
  for j in range(M):
    max_n = 1
    for k in range(1, s_n):
      if(j + k > M - 1 or i + k > N - 1):
        break
      if(arr[i][j] == arr[i][j + k] and arr[i][j] == arr[i + k][j] and arr[i][j] == arr[i + k][j + k]):
        tmp = k
        max_n = k + 1
      
    if(max_n > ans):
      ans = max_n

print(ans ** 2)