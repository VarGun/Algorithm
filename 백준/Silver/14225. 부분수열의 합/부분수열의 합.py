import sys
input = sys.stdin.readline

def dfs(idx, sum):
  global min

  if (idx >= n):
    return
  
  sum += arr[idx]
  visited[sum] = True
  
  dfs(idx + 1, sum)

  dfs(idx + 1, sum - arr[idx])


if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  visited = [False for _ in range(0, 2000001)]
  min = 100000
  dfs(0, 0)
  for i in range(1, len(visited)):
    if(visited[i] == False):
      print(i)
      break