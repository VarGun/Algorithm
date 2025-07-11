import sys

input = sys.stdin.readline
n, m = map(int, input().split())
l_list = [[] for _ in range(n + 1)]  # 본인보다 큰 리스트
s_list = [[] for _ in range(n + 1)]  # 본인보다 작은 리스트

for _ in range(m):
  s, l = map(int, input().split())
  l_list[s].append(l)
  s_list[l].append(s)

def dfs(num, visited, tar_list):  # num : 대상, visited : 검사, tar_list = s_list or l_list
  tar = tar_list[num]  # i 번 학생보다 큰 or 작은 리스트
  visited[num - 1] = True
  for i in range(len(tar)):
    if (not visited[tar[i] - 1]):
      dfs(tar[i], visited, tar_list)

ans = 0
for i in range(1, n + 1):
  tar_s = s_list[i]  # i 번 학생보다 작은 리스트
  tar_l = l_list[i]  # i 번 학생보다 큰 리스트
  visited = [False for _ in range(n)]
  visited[i - 1] = True
  for j in range(len(tar_s)):
    dfs(tar_s[j], visited, s_list)
  for j in range(len(tar_l)):
    dfs(tar_l[j], visited, l_list)
  if (False not in visited):
    ans += 1
print(ans)