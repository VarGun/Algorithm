N, M = map(int, input().split())

s = set()
s2 = set()
for _ in range(N):
  s.add(input())
for _ in range(M):
  s2.add(input())

gun = sorted(list(s & s2))
print(len(gun))
for i in range(len(gun)):
  print(gun[i])
