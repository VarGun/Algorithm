from collections import deque
r, c = map(int, input().split())

arr = [list(input()) for _ in range(r)]

stone = []
for i in range(r):
  for j in range(c):
    if(arr[i][j] == 'D'):
      stone = [i, j]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0
end_flag = False

while True:
  cnt += 1
  tmp_arr = []
  s_flag = False
  for i in range(r):
    tmp_arr.append([])
    for j in range(c):
      tmp_arr[i].append(arr[i][j])
  
  for i in range(r):
    for j in range(c):
      if(arr[i][j] == 'S'):
        for k in range(4):
          ny = i + dy[k]
          nx = j + dx[k]
          if(0 <= ny < r and 0 <= nx < c):
            if(ny == stone[0] and nx == stone[1]):
              end_flag = True
              break
            if(arr[ny][nx] == '.'):
              tmp_arr[ny][nx] = 'S'
              s_flag = True
  
  for i in range(r):
    for j in range(c):
      arr[i][j] = tmp_arr[i][j]  
  
  if(end_flag):
    print(cnt)
    break

  if(not s_flag):
    print('KAKTUS')
    break

  for i in range(r):
    for j in range(c):
      if(arr[i][j] == '*'):
        for k in range(4):
          ny = i + dy[k]
          nx = j + dx[k]
          if(0 <= ny < r and 0 <= nx < c):
            if(arr[ny][nx] == '.' or arr[ny][nx] == 'S'):
              tmp_arr[ny][nx] = '*'
  
  for i in range(r):
    for j in range(c):
      arr[i][j] = tmp_arr[i][j]