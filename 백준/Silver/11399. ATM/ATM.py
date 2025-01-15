n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for i in range(len(arr)):
  ans += arr[i] * (len(arr) - i)
print(ans)