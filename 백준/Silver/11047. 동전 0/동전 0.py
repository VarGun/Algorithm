import sys
input = sys.stdin.readline


def solution(arr, K, cnt):
  for i in range(len(arr)):
    # print("i : ", i)
    if(K >= arr[i]):
      cnt += K // arr[i]
      K %= arr[i]
      # print('arr[i] : ', arr[i])
      # print("K : ", K)
  print(cnt)
  return


if __name__ == "__main__":
  N, K = map(int, input().split())
  arr = []
  cnt = 0
  for _ in range(N):
    arr.append(int(input()))
  arr.sort(reverse=True)
  # print(arr)
  solution(arr, K, cnt)
  
