import sys
input = sys.stdin.readline

def dfs(idx, sum):
  global ans

  if idx >= n:
    return
  
  sum += arr[idx]

  if(sum == s):
    ans += 1
  
  dfs(idx + 1, sum)

  dfs(idx + 1, sum - arr[idx])

if __name__ == "__main__":
  n, s = map(int, input().split())
  arr = list(map(int, input().split()))
  ans = 0
  dfs(0, 0)
  print(ans)