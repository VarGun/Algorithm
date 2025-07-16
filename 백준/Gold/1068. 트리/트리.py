n = int(input())

gun = list(map(int, input().split()))
tree = [[] for _ in range(n)]
is_deleted = []
for i in range(n):
  if (gun[i] != -1):
    tree[gun[i]].append(i)
visited = [False for _ in range(n)]
target = int(input())


def delete_dfs(i):
  tar = tree[i]
  is_deleted.append(i)
  for j in range(len(tar)):
    delete_dfs(tar[j])
  tree[i] = ['deleted']


delete_dfs(target)
ans = 0
for i in range(len(tree)):
  if (len(tree[i]) == 0):
    ans += 1
  elif (tree[i][0] != 'deleted'):
    gugu = 0
    for j in range(len(tree[i])):
      if (len(tree[tree[i][j]]) != 0 and tree[tree[i][j]][0] == 'deleted'):
        gugu += 1
    if (gugu == len(tree[i])):
      ans += 1

print(ans)
