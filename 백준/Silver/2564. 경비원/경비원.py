r, c = map(int, input().split())
t = int(input())
stores = [list(map(int, input().split())) for _ in range(t)]
dong = list(map(int, input().split()))
sum = 0
for i in range(t):
  tar = stores[i]  # [1, 4], 각 좌표
  if (dong[0] == tar[0]):
    sum += abs(dong[1] - tar[1])
    continue
  if (dong[0] == 1):
    if (tar[0] == 2):
      sum += c + min(dong[1] + tar[1], r - dong[1] + r - tar[1])
    elif (tar[0] == 3):
      sum += dong[1] + tar[1]
    else:
      sum += (r - dong[1]) + tar[1]
  elif (dong[0] == 2):
    if (tar[0] == 1):
      sum += c + min(dong[1] + tar[1], r - dong[1] + r - tar[1])
    elif (tar[0] == 3):
      sum += dong[1] + (c - tar[1])
    else:
      sum += (r - dong[1]) + (c - tar[1])
  elif (dong[0] == 3):
    if (tar[0] == 1):
      sum += dong[1] + tar[1]
    elif (tar[0] == 2):
      sum += (c - dong[1]) + tar[1]
    else:
      sum += r + min(dong[1] + tar[1], c - dong[1] + c - tar[1])
  else:
    if (tar[0] == 1):
      sum += dong[1] + (r - tar[1])
    elif (tar[0] == 2):
      sum += (c - dong[1]) + (r - tar[1])
    else:
      sum += r + min(dong[1] + tar[1], c - dong[1] + c - tar[1])
print(sum)
