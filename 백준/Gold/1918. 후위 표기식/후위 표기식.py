def solution(arr):
  stack = []
  dict = {"(" : 0 ,"*" : 2, "/" : 2, "+" : 1, "-" : 1}
  ans = ""
  
  for i in arr:
    if(i.isupper()):
      ans += i
    elif(i == "("):
      stack.append(i)
    elif(i == ")"):
      while stack and stack[-1] != "(":
        ans += stack.pop()
      stack.pop()
    else:
      while stack and dict[i] <= dict[stack[-1]]:
        ans += stack.pop()
      stack.append(i)
  while stack:
    ans += stack.pop()
  return ans



if __name__ == "__main__" :
  arr = input()
  print(solution(arr))