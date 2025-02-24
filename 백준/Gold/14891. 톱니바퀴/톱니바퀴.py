import sys

input = sys.stdin.readline

def clock(line): # 시계 방향
  return [line[-1]] + line[:-1]

def r_clock(line): # 반시계 방향
  return line[1:] + [line[0]]

arr = [[] for _ in range(4)] # 톱니 바퀴 상태
for i in range(4):
  line = input().rstrip()
  for j in line:
    arr[i].append(int(j))

k = int(input())

for _ in range(k):
  n, d = map(int, input().split()) # 1 : 시계, -1 : 반시계

  same = [[True, True], [True, True], [True, True], [True, True]]

  # 극이 같은지 검사
  if(arr[0][2] != arr[1][6]):
    same[0][1] = False
    same[1][0] = False
  if(arr[1][2] != arr[2][6]):
    same[1][1] = False
    same[2][0] = False
  if(arr[2][2] != arr[3][6]):
    same[2][1] = False
    same[3][0] = False
  
  isClock = True
  tmpIsClock = True
  if(d == -1):
    isClock = False
    tmpIsClock = isClock

  for i in range(n - 1, 4): # 오른쪽으로
    if(same[i][1] == True):
      break
    else: # 돌릴거
      if(tmpIsClock):
        arr[i + 1] = r_clock(arr[i + 1])
      else:
        arr[i + 1] = clock(arr[i + 1])

      tmpIsClock = not tmpIsClock
      
  tmpIsClock = isClock

  for i in range(n - 1, 0, -1):
    if(same[i][0] == True):
      break
    else: # 돌릴거
      if(tmpIsClock):
        arr[i - 1] = r_clock(arr[i - 1])
      else:
        arr[i - 1] = clock(arr[i - 1])
      tmpIsClock = not tmpIsClock
  if(isClock):
    arr[n - 1] = clock(arr[n - 1])
  else:
    arr[n - 1] = r_clock(arr[n - 1])

sum = 0
mul = 1
for i in range(4):
  sum += arr[i][0] * mul
  mul *= 2

print(sum)