def solution():
  n = int(input())
  arr = list(map(int, input().split()))
  d = [-1000] * n
  d[0] = arr[0]
  for i in range(1, n):
    d[i] = max(arr[i],arr[i] + d[i - 1])
  print(max(d))
  

if __name__ == "__main__":
  solution()