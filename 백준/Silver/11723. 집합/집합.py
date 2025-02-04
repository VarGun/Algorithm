import sys
input = sys.stdin.readline

d = {}
for i in range(1, 21):
  d[i] = 0
n = int(input())

for _ in range(n):
  line = input().split()
  if(len(line) == 1):
    if(line[0] == 'empty'):
      for i in range(1, 21):
        d[i] = 0
    else:
      for i in range(1, 21):
        d[i] = 1
  else:
    o, n = line[0], line[1]
    if(o == "add"):
      d[int(n)] = 1
    elif(o == "remove"):
      d[int(n)] = 0
    elif(o == "check"):
      if(d[int(n)] == 1):
        print(1)
      else:
        print(0)
    elif(o == "toggle"):
      if(d[int(n)] == 1):
        d[int(n)] = 0
      else:
        d[int(n)] = 1