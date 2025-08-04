N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
gun = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
maxnum = 0
for i in range(6):
  bottom = arr[0][i]  # 바닥
  top = arr[0][gun[i]]
  _max = -1
  res_tmp = 0
  for j in range(6):
    if (arr[0][j] != bottom and arr[0][j] != top):
      if (_max < arr[0][j]):
        _max = arr[0][j]
  res_tmp += _max
  for j in range(1, N):
    tar_dice = arr[j]  # 타켓 주사위
    bottom = top  # 1 ~ 6
    # 그러니까 bottom 의 index 를 찾아서 top 에 넣어야지
    top = arr[j][gun[arr[j].index(bottom)]]  # 주사위에서 bottom 의 인덱스
    _max = -1
    for k in range(6):
      if (arr[j][k] != bottom and arr[j][k] != top):
        if (_max < arr[j][k]):
          _max = arr[j][k]
    res_tmp += _max
  if (maxnum < res_tmp):
    maxnum = res_tmp
print(maxnum)
