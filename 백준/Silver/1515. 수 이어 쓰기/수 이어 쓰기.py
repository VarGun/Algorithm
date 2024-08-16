import sys
input = sys.stdin.readline

n = input().strip()
i = 0
c_num = 0
while i < len(n):
  c_num += 1
  for j in str(c_num):
    if(i >= len(n)):
      break
    if(j == str(n[i])):
      i += 1

print(c_num)