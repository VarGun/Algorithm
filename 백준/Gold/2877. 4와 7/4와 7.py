k = int(input())

pn, current = 2, 2
while current < k:
  current += 2 ** pn
  pn += 1

pn -= 1
prev_cnt = current - (2 ** pn)
idx = k - prev_cnt - 1

bits = f"{idx:0{pn}b}"
print(bits.replace('0', '4').replace('1', '7'))