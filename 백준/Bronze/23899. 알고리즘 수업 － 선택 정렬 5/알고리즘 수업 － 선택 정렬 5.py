import sys
input = sys.stdin.readline

def selection(n, arr, tar):
  order = {}
  s_arr = sorted(arr)
  for i in range(len(arr)):
    order[arr[i]] = i
  
  for i in range(n - 1, 0, -1):
    if(tar == arr):
      print(1)
      return
    tmp = [0, 0]
    if(arr[i] != s_arr[i]):
      tmp = [arr[i], s_arr[i]]
      arr[i], arr[order[s_arr[i]]] = arr[order[s_arr[i]]], arr[i]
      order[tmp[0]], order[tmp[1]] = order[tmp[1]], order[tmp[0]]
  if(tar == arr):
    print(1)
    return
  print(0)
  return


if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  tar = list(map(int, input().split()))
  selection(n, arr, tar)