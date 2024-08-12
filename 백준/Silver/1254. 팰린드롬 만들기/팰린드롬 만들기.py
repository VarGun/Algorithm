s = input()
r_s = s[::-1]

for i in range(len(s)):
  str = s[i:]
  c_str = r_s[:len(s) - i]
  if(str == c_str):
    print(len(s) + i)
    break