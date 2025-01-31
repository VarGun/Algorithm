import sys
input = sys.stdin.readline

def solution(arr, re_arr, tar, n):
  cnt = 0
  re_cnt = 1

  for i in range(1, n):
    if(arr[i - 1] != tar[i - 1]):
      if(i != n - 1):
        cnt += 1
        arr[i - 1], arr[i], arr[i + 1] = abs(arr[i - 1] - 1), abs(arr[i] - 1), abs(arr[i + 1] - 1)
      else:
        cnt += 1
        arr[i - 1], arr[i]= abs(arr[i - 1] - 1), abs(arr[i] - 1)

    if(re_arr[i - 1] != tar[i - 1]):
      if(i != n - 1):
        re_cnt += 1
        re_arr[i - 1], re_arr[i], re_arr[i + 1] = abs(re_arr[i - 1] - 1), abs(re_arr[i] - 1), abs(re_arr[i + 1] - 1)
      else:
        re_cnt += 1
        re_arr[i - 1], re_arr[i] = abs(re_arr[i - 1] - 1), abs(re_arr[i] - 1)
      
  if(arr == tar and re_arr == tar):
    print(min(cnt, re_cnt))
    return
  elif(arr == tar):
    print(cnt)
    return
  elif(re_arr == tar):
    print(re_cnt)
    return
  else:
    print(-1)
    return

if __name__ == "__main__":
  n = int(input())
  arr = []
  re_arr = []
  tar = []
  a = input()
  b = input()
  if(a == b):
    print(0)
  
  else:
    for i in range(n):
      arr.append(int(a[i]))
      re_arr.append(int(a[i]))
    for i in range(n):
      tar.append(int(b[i]))
    re_arr[0], re_arr[1] = abs(re_arr[0] - 1), abs(re_arr[1] - 1)
    solution(arr, re_arr, tar, n)