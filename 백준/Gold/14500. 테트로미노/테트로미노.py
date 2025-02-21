import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

max = 0

# case 1 : ㅡ
for i in range(n):
  sum = 0
  for j in range(m - 3):
    sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3]
    if(sum > max):
      max = sum

# case 1 - 2 : ㅣ
for i in range(n - 3):
  sum = 0
  for j in range(m):
    sum = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j]
    if(sum > max):
      max = sum

# case 2 : L
for i in range(n - 2):
  sum = 0
  for j in range(m - 1):
    sum = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j + 1]
    if(sum > max):
      max = sum

# case 2 - 2 : ㄴ 대치
for i in range(n - 1):
  sum = 0
  for j in range(m - 2):
    sum = arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2] + arr[i][j + 2]
    if(sum > max):
      max = sum

# case 2 - 3 : ㄱ
for i in range(n - 2):
  sum = 0
  for j in range(m - 1):
    sum = arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
    if(sum > max):
      max = sum

# case 2 - 4 : ¬ 대치
for i in range(n - 1):
  sum = 0
  for j in range(m - 2):
    sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j]
    if(sum > max):
      max = sum

# case 2 - 2 - 1 : L 대치
for i in range(n - 2):
  sum = 0
  for j in range(m - 1):
    sum = arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1] + arr[i + 2][j]
    if(sum > max):
      max = sum

# case 2 - 2 - 2 : ㄴ
for i in range(n - 1):
  sum = 0
  for j in range(m - 2):
    sum = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
    if(sum > max):
      max = sum

# case 2 - 2 - 3 : ㄱ 대치
for i in range(n - 2):
  sum = 0
  for j in range(m - 1):
    sum = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i][j + 1]
    if(sum > max):
      max = sum

# case 2 - 2 - 4 : ¬
for i in range(n - 1):
  sum = 0
  for j in range(m - 2):
    sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 2]
    if(sum > max):
      max = sum

# case 3
for i in range(n - 2):
  sum = 0
  for j in range(m - 1):
    sum = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
    if(sum > max):
      max = sum

# case 3 - 2
for i in range(n - 1):
  sum = 0
  for j in range(m - 2):
    sum = arr[i + 1][j] + arr[i + 1][j + 1] + arr[i][j + 1] + arr[i][j + 2]
    if(sum > max):
      max = sum

# case 3 - 3
for i in range(n - 2):
  sum = 0
  for j in range(m - 1):
    sum = arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j] + arr[i + 2][j]
    if(sum > max):
      max = sum

# case 3 - 4
for i in range(n - 1):
  sum = 0
  for j in range(m - 2):
    sum = arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
    if(sum > max):
      max = sum


# case 4 
for i in range(n - 1):
  sum = 0
  for j in range(m - 2):
    sum = arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i][j + 2]
    if(sum > max):
      max = sum

# case 4 - 2
for i in range(n - 2):
  sum = 0
  for j in range(m - 1):
    sum = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 1][j + 1]
    if(sum > max):
      max = sum

# case 4 - 3
for i in range(n - 1):
  sum = 0
  for j in range(m - 2):
    sum = arr[i + 1][j] + arr[i + 1][j + 1] + arr[i][j + 1] + arr[i + 1][j + 2]
    if(sum > max):
      max = sum

# case 4 - 4
for i in range(n - 2):
  sum = 0
  for j in range(m - 1):
    sum = arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
    if(sum > max):
      max = sum

# case 4 - 4
for i in range(n - 1):
  sum = 0
  for j in range(m - 1):
    sum = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i][j + 1]
    if(sum > max):
      max = sum

print(max)