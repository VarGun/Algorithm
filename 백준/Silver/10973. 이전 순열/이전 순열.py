import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


i = n - 1
while i > 0 and arr[i - 1] <= arr[i]:
    i -= 1

if i <= 0:
    print(-1)
else:
    j = n - 1
    while arr[j] >= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    arr[i:] = reversed(arr[i:])
    print(' '.join(map(str, arr)))
