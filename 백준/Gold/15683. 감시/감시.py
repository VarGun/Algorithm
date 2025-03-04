from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
z_cnt = 0 # 0 개수
tv = deque() # cctv 번호, 위치

for i in range(n):
  for j in range(m):
    if(arr[i][j] == 0):
      z_cnt += 1
    elif(arr[i][j] != 0 and arr[i][j] != 6):
      tv.append((arr[i][j], i, j))

d = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 남, 동, 북, 서

dir = {
  1 : [ [0], [1], [2], [3] ],
  2 : [ [0, 2], [1, 3] ],
  3 : [ [0, 1], [1, 2], [2, 3], [3, 0] ],
  4 : [ [0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3] ],
  5 : [ [0, 1, 2, 3] ]
}

def check(i, j):
  if(i < 0 or i >= n or j < 0 or j >= m):
    return False
  return True

def watch(i, j, direc, arr):
  for k in direc:
    dx, dy = j, i

    while True:
      dx += d[k][1]
      dy += d[k][0]
      if(not check(dy, dx) or arr[dy][dx] == 6):
        break
      if(arr[dy][dx] == 0):
        arr[dy][dx] = '#'

def count_zero(arr):
  global z_cnt
  cnt = 0
  for i in arr:
    for j in i:
      if(j == 0):
        cnt += 1
  z_cnt = min(cnt, z_cnt)

def dfs(depth, arr):
  tmp_arr = []

  if(depth == len(tv)):
    count_zero(arr)
    return

  for i in range(n):
    tmp_arr.append([])
    for j in range(m):
      tmp_arr[i].append(arr[i][j])

  num, y, x = tv[depth]

  for d in dir[num]:
    watch(y, x, d, tmp_arr)
    dfs(depth + 1, tmp_arr)
    tmp_arr = []
    for i in range(n):
      tmp_arr.append([])
      for j in range(m):
        tmp_arr[i].append(arr[i][j])

dfs(0, arr)
print(z_cnt)