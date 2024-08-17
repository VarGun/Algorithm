import sys
input = sys.stdin.readline

def solution(arr):
  cmd = []
  for i in range(len(arr)):
    flag = False
    for j in range(len(arr[i])):
      if(not arr[i][j][0].upper() in cmd):
        cmd.append(arr[i][j][0].upper())
        flag = True
        arr[i][j] = "[" + arr[i][j][0] +  "]" + arr[i][j][1:]
        print(' '.join(arr[i]))
        break
    if(flag):
      continue
    
    for j in range(len(arr[i])):
      for k in range(len(arr[i][j])):
        if(not arr[i][j][k].upper() in cmd):
          cmd.append(arr[i][j][k].upper())
          flag = True
          arr[i][j] = arr[i][j][0:k] + "[" + arr[i][j][k] + "]" + arr[i][j][k + 1:]
          print(' '.join(arr[i]))
          break
      if(flag):
        break
    if(not flag):
      print(' '.join(arr[i]))
      
if __name__ == "__main__":
  n = int(input())
  arr = []
  for _ in range(n):
    arr.append(input().rstrip().split())
  solution(arr)
