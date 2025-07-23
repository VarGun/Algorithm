N = int(input())
arr = list(map(int, input().split()))
K = int(input())
ans = []


def rec(arr, depth):
  global N, K, ans

  if (len(arr) == 2):
    arr.sort()
    if (depth == K):
      for i in range(2):
        ans.append(arr[i])
    return arr
  else:
    tmp = []
    length = len(arr)
    tmp2 = rec(arr[:length // 2], depth * 2)
    tmp3 = rec(arr[length // 2:], depth * 2)
    for i in range(len(tmp2)):
      tmp.append(tmp2[i])
      tmp.append(tmp3[i])
    tmp.sort()

    if (depth == K):
      for i in range(len(tmp)):
        ans.append(tmp[i])
    return tmp

rec(arr, 1)
print(*ans)
