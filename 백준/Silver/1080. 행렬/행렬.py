def solution(n, m, am, bm):
  if((n <= 2 or m <= 2) and am != bm): # 사이즈가 작을 경우
    print(-1)
    return
  cnt = 0
  for i in range(n - 2):
    for j in range(m - 2):
      if(am[i][j] != bm[i][j]):
        convert(i, j)
        cnt += 1
  if(am != bm):
    print(-1)
  else:
    print(cnt)
  return

def convert(i, j):
  for x in range(i, i + 3):
    for y in range(j, j + 3):
      if(am[x][y] == 0):
        am[x][y] = 1
      else:
        am[x][y] = 0

if __name__ == "__main__":
  n, m = map(int, input().split())
  am = []
  bm = []
  for _ in range(n):
    line = input()
    la = []
    for num in line:
      la.append(int(num))
    am.append(la)
  for _ in range(n):
    line = input()
    la = []
    for num in line:
      la.append(int(num))
    bm.append(la)
  solution(n, m, am , bm)