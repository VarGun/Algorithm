N = int(input())
M = int(input())
S = input()
ioi = 'IO' * N + 'I'  # IOI 문자열
length = 2 * N + 1  # IOI 문자열의 길이

i = 0
ans = 0
while (i <= M - 1):
  if (S[i] == 'I'):
    if (S[i:i + length] == ioi):
      ans += 1
      i += 2
    else:
      i += 1
  else:
    i += 1

print(ans)
