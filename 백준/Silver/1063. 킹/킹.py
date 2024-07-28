import sys
input = sys.stdin.readline

L1, L2, N = input().split()

N = int(N)

arr = [[0,0,0,0,0,0,0,0] for _ in range(8)]
# start row
s_r = 'A'
# start col
s_c = 8

# king 위치
king = [0,0]
# stone 위치
stone = [0,0]


for i in range(7, -1, -1):
  for j in range(8):
    arr[7 - i][j] = s_r + str(i + 1)
    if(arr[7 - i][j] == L1):
      king = [7 - i, j]
    if(arr[7 - i][j] == L2):
      stone = [7 - i, j]
    s_r = chr(ord(s_r) + 1)
  s_r = 'A'

def solution(cm):

  if(cm == 'R'):
    if(king[0] == stone[0] and king[1] + 1 == stone[1]):
      if(stone[1] + 1 > 7):
        return
      else:
        king[1] += 1
        stone[1] += 1
    else:
      if(king[1] + 1 > 7):
        return
      else:
        king[1] += 1

  elif(cm == "L"):
    if(king[0] == stone[0] and king[1] - 1 == stone[1]):
      if(stone[1] - 1 < 0):
        return
      else:
        king[1] -= 1
        stone[1] -= 1
    else:
      if(king[1] - 1 < 0):
        return
      else:
        king[1] -= 1
        
  elif(cm == "B"):
    if(king[0] + 1 == stone[0] and king[1] == stone[1]):
      if(stone[0] + 1 > 7):
        return
      else:
        king[0] += 1
        stone[0] += 1
    else:
      if(king[0] + 1 > 7):
        return
      else:
        king[0] += 1
        
  elif(cm == 'T'):
    if(king[0] - 1 == stone[0] and king[1] == stone[1]):
      if(stone[0] - 1 < 0):
        return
      else:
        king[0] -= 1
        stone[0] -= 1
    else:
      if(king[0] - 1 < 0):
        return
      else:
        king[0] -= 1
  
  elif(cm == "RT"):
    if(king[0] - 1 == stone[0] and king[1] + 1 == stone[1]):
      if(stone[0] - 1 < 0 or stone[1] + 1 > 7):
        return
      else:
        king[0] -= 1
        stone[0] -= 1
        king[1] += 1
        stone[1] += 1
    else:
      if(king[0] - 1 < 0 or king[1] + 1 > 7):
        return
      else:
        king[0] -= 1
        king[1] += 1
  
  elif(cm == "LT"):
    if(king[0] - 1 == stone[0] and king[1] - 1 == stone[1]):
      if(stone[0] - 1 < 0 or stone[1] - 1 < 0):
        return
      else:
        king[0] -= 1
        stone[0] -= 1
        king[1] -= 1
        stone[1] -= 1
    else:
      if(king[0] - 1 < 0 or king[1] - 1 < 0):
        return
      else:
        king[0] -= 1
        king[1] -= 1
  
  elif(cm == "RB"):
    if(king[0] + 1 == stone[0] and king[1] + 1 == stone[1]):
      if(stone[0] + 1 > 7 or stone[1] + 1 > 7):
        return
      else:
        king[0] += 1
        stone[0] += 1
        king[1] += 1
        stone[1] += 1
    else:
      if(king[0] + 1 > 7 or king[1] + 1 > 7):
        return
      else:
        king[0] += 1
        king[1] += 1
    
  elif(cm == "LB"):
    if(king[0] + 1 == stone[0] and king[1] - 1 == stone[1]):
      if(stone[0] + 1 > 7 or stone[1] - 1 < 0):
        return
      else:
        king[0] += 1
        stone[0] += 1
        king[1] -= 1
        stone[1] -= 1
    else:
      if(king[0] + 1 > 7 or king[1] - 1 < 0):
        return
      else:
        king[0] += 1
        king[1] -= 1
    
for _ in range(N):
  solution(input().strip())
  
print(arr[king[0]][king[1]])
print(arr[stone[0]][stone[1]])
