# ., K, k, P, p, N, n, B, b, R, r, Q, q
 
# $0$, 
# $1$, 
# $3$, 
# $3$, 
# $5$, 
# $9$점

dict = {0: 0, 1: 0, 3: 0, 5: 0, 9: 0}
for _ in range(8):
  l = input()
  for i in l:
    if(i == 'K'):
      dict[0] += 1
    elif(i == 'k'):
      dict[0] -= 1
    elif(i == 'P'):
      dict[1] += 1
    elif(i == 'p'):
      dict[1] -= 1
    elif(i == 'N' or i == "B"):
      dict[3] += 1
    elif(i == 'n' or i == 'b'):
      dict[3] -= 1
    elif(i == 'R'):
      dict[5] += 1
    elif(i == 'r'):
      dict[5] -= 1
    elif(i == 'Q'):
      dict[9] += 1
    elif(i == 'q'):
      dict[9] -= 1
ans = 0
for i in dict:
  ans += (i * dict[i])
  # print(i,dict[i])
print(ans)