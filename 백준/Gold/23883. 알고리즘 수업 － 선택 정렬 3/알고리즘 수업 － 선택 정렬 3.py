def selection(a, k, arr):
  order = {}
  s_arr = sorted(arr)
  for i in range(a):
    order[arr[i]] = i

  for i in range(a - 1, -1, -1):
    tmp = [0, 0]
    if(arr[i] != s_arr[i]):
      tmp = [arr[i], s_arr[i]]
      arr[i], arr[order[s_arr[i]]] = arr[order[s_arr[i]]], arr[i]
      order[tmp[0]], order[tmp[1]] = order[tmp[1]], order[tmp[0]]
      k -= 1
    if(k == 0):
      print(min(tmp[0], tmp[1]), max(tmp[0], tmp[1]))
      return
  print(-1)  
  
  return


if __name__ == "__main__":
  a, k = map(int, input().split())
  arr = list(map(int, input().split()))
  selection(a, k, arr)