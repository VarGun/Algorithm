from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
z_cnt = 0

for i in arr:
  if(i == 0):
    z_cnt += 1

def rotate(l):
  n_list = [0 for _ in range(len(l))]
  for i in range(len(l)):
    n_list[i] = l[i - 1]

  return n_list

def durability(head):
  global arr, z_cnt
  arr[head + 2] -= 1
  if(arr[head + 2] == 0):
    z_cnt += 1


r_q = deque() # 로봇 담을 큐

time = 0

while(True):
  time += 1
  # 1. 벨트 회전
  arr = rotate(arr)

  # 2. 로봇 이동
  n_q = deque() # 로봇 위치 갱신 큐
  while(r_q):
    head = r_q.popleft()
    # 이동 전에 우선 바로 뺄 수 있는지
    # n - 1 : 내리는 위치
    # 벨트가 이동 했으므로 한 칸 이동한 곳이 내리는 곳인지
    if(head + 1 == n - 1):
      continue
    # 이동 처리
    # 이동할 수 있음 = 앞에 로봇이 없음 + 이동할 칸의 내구도가 0 보다 큼
    if(arr[head + 2] > 0): # 이동할 수 있음
      if(head + 2 == n - 1): # 이동하면 끝 값임
        durability(head)
        continue
      if(len(n_q) == 0):
        n_q.append(head + 2) # 로봇 이동
        durability(head)
      else:
        if(n_q[- 1] != head + 2):
          n_q.append(head + 2) # 로봇 이동
          durability(head)
        else:
          n_q.append(head + 1)

    # 이동 못함 : 한 칸만 갱신
    else:
      n_q.append(head + 1)
  # 2 - 2. 로봇 위치 갱신
  r_q = n_q
  # 3. 올리는 위치의 내구도 검사
  if(arr[0] > 0): # 올릴 수 있다면
    r_q.append(0) # 올리고
    arr[0] -= 1 # 내구도 갱신
    if(arr[0] == 0):
      z_cnt += 1

  if(z_cnt >= k):
    break
  
print(time)