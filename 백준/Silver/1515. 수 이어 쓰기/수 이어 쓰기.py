import sys
input = sys.stdin.readline

n = input().strip()
i = 0
c_num = 1
while i < len(n):
  for j in str(c_num):
    if(i >= len(n)):
      break
    if(j == str(n[i])):
      i += 1
  c_num += 1

print(c_num - 1)