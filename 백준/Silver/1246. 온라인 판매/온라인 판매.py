import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cnt_fr = min(N, M) # 둘 중 작은 수, 실질적으로 팔 수 있는 최대의 수

arr = []

for _ in range(M):
  arr.append(int(input()))

arr = sorted(arr)


cnt = cnt_fr

idx = 0

max = arr[0]

# print('cnt : ', cnt)
max_i = 0

for i in range(1, arr[len(arr) - 1] + 1):
  if(i > arr[idx]):
    # print('걸리긴 함.')
    idx += 1
    if(cnt == len(arr) - idx + 1):
      # print("걸림 i : ", i)
      cnt -= 1 # 팔 수 있는 수 하나 줄이기
      # print('cnt : ', cnt)
      # print('idx : ', idx)
      # print("-----------------------")
  if(max < i * cnt):
    # print('i : ', i)
    # print('cnt : ', cnt)
    max = i * cnt
    max_i = i
  # print('i : ', i)
  # print("cnt : ", cnt)

print(max_i, max)


