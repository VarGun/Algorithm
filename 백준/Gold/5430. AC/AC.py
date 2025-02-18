import sys
from collections import deque

input = sys.stdin.readline


T = int(input())

for _ in range(T):
  p = input() 
  n = int(input())
  arr = input()
  q = deque(arr.rstrip()[1:-1].split(',')) 
  flag = False
  r = 0

  if(n == 0):
    q = []

  for i in range(len(p)):
    if(p[i] == "R"):
      r += 1
    elif(p[i] == "D"):
      if(len(q) == 0):
        flag = True
        print('error')
        break
      else:
        if(r % 2 == 0):
          head = q.popleft()
        else:
          head = q.pop()
  if(not flag):
    if(r % 2 != 0):
      q.reverse()
    print('[' + (',').join(q) + ']')