arr = input()
tar = input()
ans = 0
while (len(arr) >= len(tar)):
  if(tar == arr[:len(tar)]):
    ans += 1
    arr = arr[len(tar):]
  else:
    arr = arr[1:]
print(ans)