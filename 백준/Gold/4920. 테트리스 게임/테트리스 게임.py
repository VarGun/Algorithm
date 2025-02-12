import sys

# # 파일에서 입력값 읽어오기
# with open("input.txt", "r", encoding="utf-8") as file:
#     data = file.readlines()

# # sys.stdin 대체
# sys.stdin = open("input.txt", "r", encoding="utf-8")

input = sys.stdin.readline

num = 1
while True:
  n = int(input())

  if (n == 0):
    break

  arr = []

  for _ in range(n):
    line = list(map(int, input().split()))
    arr.append(line)

  max = -9999999

  # case 1 : ㅡ
  for i in range(n):
    for j in range(n - 3):
      sum = 0
      sum += arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3]
      if(sum > max):
        max = sum

  # case 1-2 : ㅣ
  for i in range(n - 3):
    for j in range(n):
      sum = 0
      sum += arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j]
      if(sum > max):
        max = sum

  # case 2-1 : ㄱㄴ
  for i in range(n - 1):
    for j in range(n - 2):
      sum = 0
      sum += arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
      if(sum > max):
        max = sum

  # case 2-2 :  
  for i in range(n - 2):
    for j in range(n - 1):
      sum = 0
      sum += arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j]
      if(sum > max):
        max = sum

  # # case 2-3 - 뒤집은거라 포함 안될 수도
  # for i in range(n - 1):
  #   for j in range(n - 2):
  #     sum = 0
  #     sum += arr[i + 1][j] + arr[i + 1][j + 1] + arr[i][j + 1] + arr[i][j + 2]
  #     if(sum > max):
  #       max = sum

  # case 3 - 1
  for i in range(n - 1):
    for j in range(n - 2):
      sum = 0
      sum += arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 2]
      if(sum > max):
        max = sum

  # case 3 - 2
  for i in range(n - 2):
    for j in range(n - 1):
      sum = 0
      sum += arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1] + arr[i + 2][j]
      if(sum > max):
        max = sum

  # case 3 - 3
  for i in range(n - 2):
    for j in range(n - 1):
      sum = 0
      sum += arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i][j + 1]
      if(sum > max):
        max = sum

  # # case 3 - 4 - 뒤집은거라 빼야할 수도
  for i in range(n - 1):
    for j in range(n - 2):
      sum = 0
      sum += arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
      if(sum > max):
        max = sum

  # case 4 - 1
  for i in range(n - 1):
    for j in range(n - 2):
      sum = 0
      sum += arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1]
      if(sum > max):
        max = sum

  # case 4 - 2
  for i in range(n - 2):
    for j in range(n - 1):
      sum = 0
      sum += arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1] + arr[i + 1][j]
      if(sum > max):
        max = sum

  # case 4 - 3
  for i in range(n - 2):
    for j in range(n - 1):
      sum = 0
      sum += arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 1][j + 1]
      if(sum > max):
        max = sum

  # # case 4 - 4 - 뒤집은거라 빼야할 수도
  for i in range(n - 1):
    for j in range(n - 2):
      sum = 0
      sum += arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
      if(sum > max):
        max = sum

  # case 5
  for i in range(n - 1):
    for j in range(n - 1):
      sum = 0
      sum += arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]
      if(sum > max):
        max = sum

  print("%s. %s" % (num, max))
  num += 1
