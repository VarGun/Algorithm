
s = input()
arr = []
for i in range(1, len(s) - 1):
  for j in range(i + 1, len(s)):
    s1 = s[:i][::-1]
    s2 = s[i:j][::-1]
    s3 = s[j:][::-1]
    arr.append(''.join(s1 + s2 + s3))

print(sorted(arr)[0])
