import sys
input = sys.stdin.readline

def solution(s, e, arr, n):
  while s <= e:
    m = (s + e) // 2
    l = 0
    
    for i in arr:
      l += i // m
    if(l >= n):
      s = m + 1
    else:
      e = m - 1
  print(e)


if __name__ == "__main__":
  k, n = map(int, input().split())
  arr = []
  s = 1
  e = 0

  for i in range(k):
    l = int(input())
    arr.append(l)
    if(l > e):
      e = l
  solution(s, e, arr, n)