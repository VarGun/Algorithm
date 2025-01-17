import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(tar):
  global visited, arr, par
  if(visited[tar] == True):
    return
  visited[tar] = True
  

  for i in range(len(arr[tar])):
    # if(visited[arr[tar][i]] == False):
    # if(tar == 2):
    #   print('par[arr[tar][i]] : ', par[arr[tar][i]])
    #   print('arr[tar] : ', arr[tar])
      # print('par[arr[tar]] : ', par[])
    if(par[arr[tar][i]] == 0):
      par[arr[tar][i]] = tar
    if(visited[arr[tar][i]] == False):
      dfs(arr[tar][i])
  
  # print('tar : ', tar)
  # print('par[tar] : ', par[tar])

  return

if __name__ == "__main__":
  n = int(input())
  arr = [[] for _ in range(n + 1)]
  visited = [False for _ in range(n + 1)]
  par = [0 for _ in range(n + 1)]
  for _ in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
  
  dfs(1)
  
  for node in par[2:]:
    print(node)