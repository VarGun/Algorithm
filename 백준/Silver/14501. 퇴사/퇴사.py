import sys
input = sys.stdin.readline

if __name__ == "__main__":
  n = int(input())
  arr = []
  
  dp = [0 for _ in range(n + 1)]

  for i in range(n):
    arr.append(list(map(int, input().split())))
  
  for i in range(n):
    for j in range(i + arr[i][0], n + 1):
      if(dp[j] < dp[i] + arr[i][1]):
        dp[j] = dp[i] +  arr[i][1]
  
  print(dp[n])