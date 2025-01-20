def solve():
  n, k = map(int, input().split())
  arr = list(map(int, input().split()))
  
  pos = {num: idx for idx, num in enumerate(arr)}
  target = sorted(arr)
  swaps = k
  
  for i in range(n-1, -1, -1):
    if arr[i] != target[i] and swaps > 0:
      curr_val = arr[i]
      target_val = target[i]
      target_idx = pos[target_val]
      
      arr[i], arr[target_idx] = arr[target_idx], arr[i]
      
      pos[curr_val], pos[target_val] = pos[target_val], pos[curr_val]
      
      swaps -= 1
      
      if swaps == 0:
        return arr  

  return -1

result = solve()
if result == -1:
  print(-1)
else:
  print(*result)
