import sys
input = sys.stdin.readline
from collections import deque

def solution(arr, q, visited):
  while q:
    c_num = q.popleft()
    for i in arr[c_num]:
      if(visited[i] == False):
        q.append(i)
        visited[i] = True
  
  print(sum(visited) - 1)


if __name__ == "__main__":
  N = int(input())
  M = int(input())
  arr = [[] for _ in range(N)]
  visited = [False for _ in range(N)]
  cnt = 0
  for _ in range(M):
    n, m = map(int,input().split())
    arr[n - 1].append(m - 1)
    arr[m - 1].append(n - 1)
  visited[0] = True
  q = deque([0])

  solution(arr, q, visited)