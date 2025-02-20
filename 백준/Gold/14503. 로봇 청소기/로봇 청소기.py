import sys

input = sys.stdin.readline

n, m = map(int, input().split())
sx, sy, d = map(int, input().split())

arr = []
drt = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 북 동 남 서

for i in range(n):
  arr.append(list(map(int, input().split())))

end = False
cnt = 0

def clean(x, y):
  global end, d, cnt
  while True:
    if(arr[x][y] == 0): # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
      cnt += 1
      arr[x][y] = 2
    flag = True
    for _ in range(4):
      d = (d - 1) % 4
      nx = x + drt[d][0]
      ny = y + drt[d][1]
      if(arr[nx][ny] == 0):
        x, y = nx, ny
        flag = False
        break

          
    if(flag): # 2. 현재 칸의 주변 4 칸 중 청소되지 않은 빈 칸이 없는 경우
      back_d = [-1 * drt[d][0], -1 * drt[d][1]] # 반대 방향
      back_x = x + back_d[0]
      back_y = y + back_d[1]
      if(arr[back_x][back_y] == 1): # 2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        end = True
        break
      else:
        x = x + (-1) * (drt[d][0])
        y = y + (-1) * (drt[d][1])
    
    if(end):
      break

clean(sx, sy)

print(cnt)