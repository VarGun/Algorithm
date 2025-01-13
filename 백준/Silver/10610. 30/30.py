def solution(n):
  n.sort(reverse=True)
  if(n[len(n) - 1] != '0'):
    print(-1)
    return
  s = 0
  ans = ''
  for i in n:
    s += int(i)
    ans += i
  if(s % 3 != 0):
    print(-1)
    return
  else:
    print(ans)

if __name__ == "__main__":
  n = list(input())
  solution(n)