from sys import stdin
from collections import Counter

def solution(N, dict, arr):
  NGF = [-1] * N
  stack = [0]
  
  for i in range(1, N):
    while stack and dict[arr[stack[-1]]] < dict[arr[i]]:
      NGF[stack.pop()] = arr[i]
    stack.append(i)
  print(*NGF)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, stdin.readline().split()))
    
    freq_dict = Counter(arr)
    
    solution(n, freq_dict, arr)