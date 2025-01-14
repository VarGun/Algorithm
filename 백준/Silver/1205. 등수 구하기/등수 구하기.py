

def solution(n, score, p, arr):
  idx = 0
  rank = 1
  dup_n = 0
  for i in range(len(arr)):
    if(arr[i] < score):
      # arr.insert(i, score)
      if(i > 0 and score != arr[i-1]):
        rank += 1
        rank += dup_n
      idx = i
      break

    if(i > 0):
      if(arr[i] != arr[i-1]):
        rank += 1
        rank += dup_n
        dup_n = 0
      else:
        # print('arr[i] : ', arr[i], ', arr[i-1] : ', arr[i-1])
        dup_n += 1
  if(p - 1 < idx):
    print(-1)
  else:
    # print('rank : ', rank)
    print(rank)
  # print('idx : ', idx)
  return



if __name__ == "__main__":
  n, score, p = map(int, input().split())
  if(n == 0):
    print(1)
  else:
    arr = list(map(int, input().split()))
    arr.append(-1)
    solution(n, score, p, arr)
  # for i in range(n):
  #   if()
  
