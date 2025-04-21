from collections import deque
import itertools
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
comList = [list(map(int, input().split())) for _ in range(k)]
nPr = itertools.permutations(comList, k)

def arrValue(arr): # 배열 값 계산하는 함수
  retValue = 50 * 100 + 1 # 한 줄에서 나올 수 있는 최대 값 + 1
  for i in range(len(arr)):
    tmp = 0
    for j in range(len(arr[i])):
      tmp += arr[i][j]
    if(tmp < retValue):
      retValue = tmp
  
  return retValue

def rotate(arr, r, c, s):
  global n, m
  start = [r - s - 1, c - s - 1]
  end = [r + s - 1, c + s - 1]
  tmp_arr = []
  for i in range(n):
    tmp_arr.append(arr[i][:])

  while(start[0] < end[0] and start[1] < end[1]):
    # 회전 먼저
    # 윗 줄
    for i in range(start[1] + 1, end[1] + 1):
      tmp_arr[start[0]][i] = arr[start[0]][i - 1]
    
    # 왼쪽 줄
    for i in range(start[0] + 1, end[0] + 1):
      tmp_arr[i][end[1]] = arr[i - 1][end[1]]
    
    # 아랫 줄
    for i in range(end[1] - 1, start[1] - 1, -1):
      tmp_arr[end[0]][i] = arr[end[0]][i + 1]
    
    # 오른쪽 줄
    for i in range(end[0] - 1, start[0] - 1, -1):
      tmp_arr[i][start[1]] = arr[i + 1][start[1]]

    # 영역 줄이기
    start[0] += 1
    start[1] += 1
    end[0] -= 1
    end[1] -= 1

  return tmp_arr


if __name__ == '__main__':
  ans = retValue = 50 * 100 + 1
  allCom = list(nPr)

  while(allCom):
    tmp = []
    comItem = allCom.pop() # ([4, 2, 1], [3, 4, 2])
    for i in range(len(comItem)):
      com = comItem[i] # [4, 2, 1]
      if(i == 0):
        tmp = (rotate(arr, com[0], com[1], com[2]))
      else:
        tmp = rotate(tmp, com[0], com[1], com[2])
    ans = min(ans, arrValue(tmp))

  print(ans)