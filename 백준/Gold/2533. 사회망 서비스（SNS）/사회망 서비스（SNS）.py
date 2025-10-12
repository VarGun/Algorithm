import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())

tree = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]  # 각 노드에 대해서, (일단 얘네는 다 얼리어답터가 된다고 가정)
# 그 노드가 얼리어답터가 아닐 때 얼리어답터 노드 수 : 얘가 얼리어답터가 아니므로, 얘랑 인접한 애들이 다 얼리어답터여야 함. 여기서는 얘 자식들이 얼리어답터 인 경우(dp[자식노드][1])들 다 더함
# 그 노트가 얼리어답터길 때 얼리어답터 노드 수 : 얘가 얼리어답터이므로, 얘랑 인접한 애들이 얼리어답터인지 상관 없음. 얘랑 인접한 애들 대상으로 얼리어답터가 아닐 경우와, 얼리어답터일 경우의 얼리어답터 수 중 작은 값을 더함

for _ in range(N - 1):
  u, v = map(int, input().split())
  tree[u].append(v)
  tree[v].append(u)


def dfs(node):

  visited[node] = True

  dp[node][1] = 1

  for next in tree[node]:
    if (not visited[next]):
      dfs(next)
      dp[node][0] += dp[next][1]
      dp[node][1] += min(dp[next][0], dp[next][1])


dfs(1)
print(min(dp[1][0], dp[1][1]))
