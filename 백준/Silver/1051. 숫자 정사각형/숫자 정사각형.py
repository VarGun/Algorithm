import sys
input = sys.stdin.readline

N, M = map(int, input().split())

s_n = min(N, M)

ans = 1

arr = [[] for _ in range(N)]

for i in range(N):
  str = input()
  for j in range(M):
    arr[i].append(str[j])

# print('s_n : ', s_n)

# if(N < M):
# 가로가 긴 경우
for i in range(N - 1):
  for j in range(M):
    max_n = 1
    for k in range(1, s_n):
      if(j + k > M - 1 or i + k > N - 1):
        # print("-------꺾일때-------")
        # print("i : ", i)
        # print("j : ", j)
        # print("k : ", k)
        # print("-------꺾일때-------")
        break
      # else:
      #   print("-------안 꺾 임-------")
      #   print("i : ", i)
      #   print("j : ", j)
      #   print("k : ", k)
      #   print("-------안 꺾 임-------")
      if(arr[i][j] == arr[i][j + k] and arr[i][j] == arr[i + k][j] and arr[i][j] == arr[i + k][j + k]):
        tmp = k
        max_n = k + 1
    # else:
      
    if(max_n > ans):
      # print('arr[i][j] : ', arr[i][j])
      # print('arr[i][j + tmp] : ', arr[i][j + tmp])
      # print('arr[i + tmp][j] : ', arr[i + tmp][j])
      # print('arr[i + tmp][j + tmp] : ', arr[i + tmp][j + tmp])
      ans = max_n

# else:
#   for i in range(N - 1):
#     for j in range(M):
#       max_n = 1
#       for k in range(1, s_n):
#         if(j + k > M - 1 or i + k > N - 1):
#           print("-------꺾일때-------")
#           print("i : ", i)
#           print("j : ", j)
#           print("k : ", k)
#           print("-------꺾일때-------")
#           break
#         else:
#           print("-------안 꺾 임-------")
#           print("i : ", i)
#           print("j : ", j)
#           print("k : ", k)
#           print("-------안 꺾 임-------")
#         if(arr[i][j] == arr[i][j + k] and arr[i][j] == arr[i + k][j] and arr[i][j] == arr[i + k][j + k]):
#           tmp = k
#           max_n = k + 1
#       # else:
        
#       if(max_n > ans):
#         # print('arr[i][j] : ', arr[i][j])
#         # print('arr[i][j + tmp] : ', arr[i][j + tmp])
#         # print('arr[i + tmp][j] : ', arr[i + tmp][j])
#         # print('arr[i + tmp][j + tmp] : ', arr[i + tmp][j + tmp])
#         ans = max_n
      
        

# print('ans : ', ans)
print(ans ** 2)