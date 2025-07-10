from itertools import combinations
n = int(input())

arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))


num_list = list(range(1, n + 1))
result = []  # [[(1, 2), (3, 4)], [(1, 3), (2, 4)], [(1, 4), (2, 3)]]

all_combs = list(combinations(num_list, n // 2))

for i in range(len(all_combs) // 2):
  pair1 = list(all_combs[i])
  pair2 = sorted([x for x in num_list if x not in pair1])
  result.append([pair1, pair2])

_min = 10000
for i in range(len(result)):  # result : [[[1, 2], [3, 4]], [[1, 3], [2, 4]], [[1, 4], [2, 3]]] 형식
  team = result[i]
  team1 = result[i][0]  # [1, 2] or [1, 2, 3]
  com_team1 = list(combinations(team1, 2))  # [1, 2],[1, 3], [2, 3]
  team2 = result[i][1]  # [3, 4] or [4, 5, 6]
  com_team2 = list(combinations(team2, 2))
  sum1 = 0
  sum2 = 0

  for j in range(len(com_team1)):
    tar = com_team1[j]
    tar2 = com_team2[j]
    a, b = tar
    c, d = tar2
    sum1 += arr[a - 1][b - 1] + arr[b - 1][a - 1]
    sum2 += arr[c - 1][d - 1] + arr[d - 1][c - 1]
  if (_min > abs(sum1 - sum2)):
    _min = abs(sum1 - sum2)
print(_min)