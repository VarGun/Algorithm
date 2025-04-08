def o_r(arr): # r 연산
  ret_arr = [[] for _ in range(len(arr))]
  visited = [[i, 0] for i in range(101)]
  max_l = 0
  for i in range(len(arr)):
    visited = [[i, 0] for i in range(101)]
    line = arr[i] # 한 줄
    tmp = [] # 유효한 방문 횟수만 남기기
    for item in line:
      visited[item][1] += 1
    for j in range(101):
      if(visited[j][0] != 0 and visited[j][1] != 0):
        tmp.append(visited[j])
    sorted_tmp = sorted(tmp, key = lambda x: (x[1], x[0])) # 출현 횟수, 숫자 순으로 정렬
    cnt_l = 0
    for j in range(len(sorted_tmp)):
      for k in range(len(sorted_tmp[j])):
        ret_arr[i].append(sorted_tmp[j][k])
        cnt_l += 1
    if(cnt_l > max_l):
      max_l = cnt_l
  
  for i in range(len(ret_arr)):
    for j in range(max_l - len(ret_arr[i])):
      if(len(ret_arr[i]) > 100):
        ret_arr[i] = ret_arr[:99]
      else:
        ret_arr[i].append(0)

  return ret_arr

def reverse(arr): # 반전
  transposed = list(map(list, zip(*arr)))
  return transposed

def o_c(arr): # c 연산
  tmp = reverse(arr)
  tmp = reverse(o_r(tmp))
  return tmp


if __name__ == "__main__":
  r, c, k = map(int, input().split())
  r, c = r - 1, c - 1 # 인덱스 맞춰주기
  oper_list_1 = ['r']
  oper_list_2 = ['c']

  arr = [list(map(int, input().split())) for _ in range(3)]
  if(len(arr) > r and len(arr[0]) > c):
    if(arr[r][c] == k):
      print(0)
      exit()
  # case 1. R 연산 먼저
  case_1 = o_r(arr)

  cnt = 1
  
  ans = -1
  while(cnt < 101):
    if(len(case_1) > r and len(case_1[0]) > c):
      if(case_1[r][c] == k):
        ans = cnt
        break
    
    # case_1 부터
    if(len(case_1) >= len(case_1[0])): # 행의 개수 >= 열의 개수
      case_1 = o_r(case_1)
      oper_list_1.append('r')

    else:
      case_1 = o_c(case_1)
      oper_list_1.append('c')

    
    cnt += 1
    
  print(ans)