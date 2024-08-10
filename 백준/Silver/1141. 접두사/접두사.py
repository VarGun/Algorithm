import sys
input = sys.stdin.readline

def solution(arr):
  cnt = 0
  for i in range(len(arr)):
    flag = False
    for j in range(i + 1, len(arr)):
      if(arr[i] == arr[j][:len(arr[i])]):
        flag = True
        break
    if not flag:
      cnt += 1
  print(cnt)
  return

if __name__ == "__main__":
  arr = []
  N = int(input())
  s = set()
  if(N == 1):
    print(1)
  else:
    for _ in range(N):
      s.add(input().strip())
    arr = list(s)
    arr.sort(key=len)
    solution(arr)