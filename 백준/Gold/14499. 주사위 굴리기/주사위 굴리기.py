import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
bmap = [[] for _ in range(n)]
dice = [0, 0, 0, 0, 0, 0]
for i in range(n):
  bmap[i] = list(map(int, input().split()))

com = list(map(int, input().split()))
cnt = 0
for i in com:
  flag = False
  if(i == 1): # 동
    if(y + 1 < m): # 넘어가지 않을 경우만 취급
      flag = True
      y += 1
      dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]

  elif(i == 2): # 서
    if(y - 1 >= 0):
      flag = True
      y -= 1
      dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
  
  elif(i == 3): # 북
    if(x - 1 >= 0):
      flag = True
      x -= 1
      dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
  
  elif(i == 4): # 남
    if(x + 1 < n):
      flag = True
      x += 1
      dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
      
  cnt += 1
  if(flag): # 조건에 걸릴 때만 출력
    if(bmap[x][y] == 0): # 칸이 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다
        bmap[x][y] = dice[5]
    else:
      dice[5] = bmap[x][y]
      bmap[x][y] = 0
    print(dice[0])