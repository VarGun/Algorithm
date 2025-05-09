d, k = map(int, input().split())
fibo = [0 for _ in range(d + 1)]
fibo[1] = 1
fibo[2] = 1
for i in range(3, d + 1):
  fibo[i] = fibo[i - 1] + fibo[i - 2]

start = fibo[d]  # 시작점
dis_row = fibo[d]  # 행 간 차이
dis_col = fibo[d - 1]  # 행 내에서 차이

row = 1
col = 1
rc = start
while True:
  if (rc == k):
    print(row)
    print(col)
    break

  elif (rc > k):
    rc = start + row * dis_row
    row += 1
    col = row
  else:
    rc += dis_col
    col += 1