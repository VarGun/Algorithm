par = input()
n = len(par)
stack = [] # 괄호 담을 스택
cur = 1
ans = 0

for i in range(n):
  if(par[i] == '(' ):
    cur *= 2
    stack.append(par[i])

  elif(par[i] == '['):
    cur *= 3
    stack.append(par[i])

  elif(par[i] == ')'):
    if(len(stack) == 0 or stack[-1] == '['): # 비었는데 들어왔거나, 짝이 잘못 맞았을 경우
      ans = 0
      break
    if(par[i - 1] == '('): # 직전 괄호가 맞을 경우에만 더 해줌. 이미 앞에서 곱을 처리했기 때문에 바로 더함
      ans += cur
    cur //= 2
    stack.pop()
  
  else:
    if(len(stack) == 0 or stack[-1] == '('): # 비었는데 들어왔거나, 짝이 잘못 맞았을 경우
      ans = 0
      break
    if(par[i - 1] == '['): # 직전 괄호가 맞을 경우에만 더 해줌. 이미 앞에서 곱을 처리했기 때문에 바로 더함
      ans += cur
    cur //= 3
    stack.pop()

if(len(stack) != 0):
  print(0)
else:
  print(ans)