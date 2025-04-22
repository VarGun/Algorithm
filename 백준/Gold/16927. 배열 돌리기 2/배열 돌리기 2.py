import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

start = [0, 0]
end = [n - 1, m - 1]

def rotate(start, end):
    top = arr[start[0]][start[1]]
    left = arr[end[0]][start[1]]
    bot = arr[end[0]][end[1]]
    right = arr[start[0]][end[1]]

    # 왼쪽 줄
    for i in range(end[0], start[0], - 1):
      arr[i][start[1]] = arr[i - 1][start[1]]
    
    # 아랫 줄
    for i in range(end[1], start[1] + 1, - 1):
      arr[end[0]][i] = arr[end[0]][i - 1]
    
    # 오른쪽 줄
    for i in range(start[0], end[0] - 1):
      arr[i][end[1]] = arr[i + 1][end[1]]
    
    # 윗 줄
    for i in range(start[1], end[1] - 1):
      arr[start[0]][i] = arr[start[0]][i + 1]
    
    arr[start[0]+1][start[1]] = top
    arr[end[0]][start[1] + 1] = left
    arr[end[0] - 1][end[1]] = bot
    arr[start[0]][end[1] - 1] = right


while(start[0] < end[0] and start[1] < end[1]):
  size = ((end[0] + end[1]) - (start[0] + start[1])) * 2

  rotate_cnt = r % size
  for _ in range(rotate_cnt):
    rotate(start, end)
  
  start[0] += 1
  start[1] += 1
  end[0] -= 1
  end[1] -= 1

for i in range(len(arr)):
  print(*arr[i])