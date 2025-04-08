from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
dic = {}
q = deque()
for i in range(n ** 2):
  line = list(map(int, input().split()))
  q.append([line[0], line[1:]]) # [4, [2, 5, 1, 7]]
  dic[line[0]] = line[1:]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0
while(q):
  head = q.popleft()
  tar = head[0] # 4
  frd = head[1] # [2, 5, 1, 7]
  seat = []
  for i in range(n):
    for j in range(n):
      tmp = [0, 0, i, j]
      for k in range(4):
        ny = i + dy[k]
        nx = j + dx[k]
        if(0 <= ny < n and 0 <= nx < n): # 일단 벗어나는지 검사
          # 1. 좋아하는 학생
          if(arr[ny][nx] in frd):
            tmp[0] += 1
          # 2. 빈 칸
          if(arr[ny][nx] == 0):
            tmp[1] += 1
      seat.append(tmp)
  
  # 좋아하는 학생, 빈 칸 수, 행, 열 순으로 정렬
  sorted_seat = sorted(seat, key = lambda x: (-x[0], -x[1], x[2], x[3]))

  for i in range(len(sorted_seat)):
    if(arr[sorted_seat[i][2]][sorted_seat[i][3]] == 0): # 빈 자리면 자리 선택
      arr[sorted_seat[i][2]][sorted_seat[i][3]] = tar
      break
  
# 만족도 조사
sum = 0
for i in range(n):
  for j in range(n):
    tar = arr[i][j]
    tmp = 0
    for k in range(4):
      ny = i + dy[k]
      nx = j + dx[k]
      if(0 <= ny < n and 0 <= nx < n): # 벗어나는지 검사
        if(arr[ny][nx] in dic[tar]):
          tmp += 1
    if(tmp == 1):
      sum += 1
    elif(tmp == 2):
      sum += 10
    elif(tmp == 3):
      sum += 100
    elif(tmp == 4):
      sum += 1000

print(sum)
