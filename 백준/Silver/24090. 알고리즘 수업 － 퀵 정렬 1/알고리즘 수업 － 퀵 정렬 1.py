import sys
sys.setrecursionlimit(int(1e4))
input = sys.stdin.readline

def quick(arr,p, r):
  global cnt, k
  if (p >= r):
    return
  q = partition(arr, p, r)
  quick(arr, p, q - 1)
  quick(arr, q + 1, r)
    
def partition(arr, p, r):
  global cnt
  x  = arr[r]
  i = p - 1
  for j in range(p, r):
    if(arr[j] <= x):
      i += 1
      if(i != j):
        arr[i], arr[j] = arr[j], arr[i]
      cnt += 1
      if(cnt == k):
        print(arr[i], arr[j])
  if(i + 1 != r):
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    cnt += 1
    if(cnt == k):
      print(arr[i + 1], arr[r])
  
  return i + 1

if __name__ == "__main__":
  a, k = map(int, input().split())
  arr = list(map(int, input().split()))
  cnt = 0
  quick(arr, 0, a - 1)
  if(k > cnt):
    print(-1)