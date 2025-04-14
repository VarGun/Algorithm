arr = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
ans = 0
bingo_cnt = 0
bingo_flag = False
cnt = 0
l_cross_list = [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4]]

def bingo(y, x):
  global visited, bingo_cnt, bingo_flag, l_cross_list
  
  # x 축
  x_flag = False
  for i in range(5):
    if(visited[y][i] == 0):
      x_flag = True
      break
  
  if(not x_flag):
    bingo_cnt += 1
    if(bingo_cnt == 3):
      bingo_flag = True
      return
  
  # y 축
  y_flag = False
  for i in range(5):
    if(visited[i][x] == 0):
      y_flag = True
      break

  if(not y_flag):
    bingo_cnt += 1
    if(bingo_cnt == 3):
      bingo_flag = True
      return
  
  r_cr_flag = False # 오른쪽으로 떨어지는 대각선
  if(y == x):
    for k in range(5):
      if(visited[k][k] == 0):
        r_cr_flag = True
        break
  
    if(not r_cr_flag):
      bingo_cnt += 1
      if(bingo_cnt == 3):
        bingo_flag = True
        return

  l_cr_flag = False
  if([y, x] in l_cross_list): # 왼쪽으로 떨어지는 대각선
    for item in l_cross_list:
      if(visited[item[0]][item[1]] == 0):
        l_cr_flag = True
        break
  
    if(not l_cr_flag):
      bingo_cnt += 1
      if(bingo_cnt == 3):
        bingo_flag = True
        return
  
while(cnt < 5):
  line = list(map(int, input().split())) # 빙고 번호
  for i in range(5):
    for j in range(5):
      for k in range(5):
        if(arr[j][k] == line[i]):
          visited[j][k] = 1
          bingo(j, k)
          if(bingo_flag):
            print(cnt * 5 + i + 1)
            exit()
  
  cnt += 1
