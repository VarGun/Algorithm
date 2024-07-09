n, m = map(int, input().split())
arr = map(int, input().split())

sum = 0
for i in arr:
  sum += i
print(1 if sum % m == 0 else 0)