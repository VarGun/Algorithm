import sys

input = sys.stdin.readline
n, m, r = map(int, input().split())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

rotate_cnt = min(m, n) // 2 # 회전할 배열들 수, 안쪽의 갯수

sx, ex, sy, ey = 0, m, 0, n

for j in range(rotate_cnt):

  rotate_limit = r % ((ex - sx - 1) * 2 +  (ey - sy - 1) * 2) # 나머지만큼만 돌리기

  while(rotate_limit):
    rotate_limit -= 1

    start = arr[sy][sx + 1]

    # 윗 줄
    for i in range(sx + 1, ex - 1):
      arr[sy][i] = arr[sy][i + 1]
    
    # 오른쪽 줄
    for i in range(sy, ey - 1):
      arr[i][ex - 1] = arr[i + 1][ex - 1]
    
    # 아랫 줄
    for i in range(ex - 1, sx, -1):
      arr[ey - 1][i] = arr[ey - 1][i - 1]
    
    # 왼쪽 줄
    for i in range(ey - 1, sy, -1):
      arr[i][sx] = arr[i - 1][sx]

    arr[sy][sx] = start

  # 경계 값 갱신
  sx += 1
  sy += 1
  ex -= 1
  ey -= 1

for i in range(len(arr)):
  print(*arr[i])