def dis(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def combi(arr, r, s = 0, comb = []):
  if len(comb) == r:
    comb_list.append(comb)
    return
  for i in range(s, len(arr)):
    combi(arr, r, i + 1, comb + [arr[i]])

if __name__ == "__main__":
  h = []
  c = []

  n, m = map(int, input().split())
  for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
      if(arr[j] == 1):
        h.append([i, j])
      elif(arr[j] == 2):
        c.append([i, j])
  
  comb_list = []

  combi(c, m)

  min_dis = 9999999

  for chs in comb_list:
    ch_dis = 0
    for home in h:
      min = 9999999
      for ch in chs:
        if(dis(home, ch) < min):
          min = dis(home, ch)
      ch_dis += min
    if(ch_dis < min_dis):
      min_dis = ch_dis
  
  print(min_dis)