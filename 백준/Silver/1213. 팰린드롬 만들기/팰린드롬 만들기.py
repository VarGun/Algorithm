def solution(dict):
  ans = []
  odd_str = ""
  for i in range(65, 91):
    if(dict[chr(i)] == 0):
      continue
    if(dict[chr(i)] % 2 != 0):
      if(odd_str == ""):
        odd_str = chr(i)
        dict[chr(i)] -= 1
      else:
        return "I'm Sorry Hansoo"
    for j in range(0, dict[chr(i)] // 2):
      ans.append(chr(i))
  
  return ''.join(ans) + odd_str + ''.join(sorted(ans, reverse=True))
  
if __name__ == "__main__":
  n = input()

  dict = {}

  for i in range(65, 91):
    dict[chr(i)] = 0

  for i in range(len(n)):
    dict[n[i]] += 1
  
  s = solution(dict)
  print(s)

