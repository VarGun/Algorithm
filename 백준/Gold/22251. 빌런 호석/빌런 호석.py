N, K, P, X = map(int, input().split())
# N : 최대수, K : 자릿수, P : 바꿀 수 있는 최대 수, X : 현재 층

lights = {'0': [1, 1, 1, 1, 1, 1, 0],
          '1': [0, 1, 1, 0, 0, 0, 0],
          '2': [1, 1, 0, 1, 1, 0, 1],
          '3': [1, 1, 1, 1, 0, 0, 1],
          '4': [0, 1, 1, 0, 0, 1, 1],
          '5': [1, 0, 1, 1, 0, 1, 1],
          '6': [1, 0, 1, 1, 1, 1, 1],
          '7': [1, 1, 1, 0, 0, 0, 0],
          '8': [1, 1, 1, 1, 1, 1, 1],
          '9': [1, 1, 1, 1, 0, 1, 1]}

ans = 0
X = list(str(X).zfill(K))
for cur in range(1, N + 1):  # 0부터 최대층까지
  cur = list(str(cur).zfill(K))  # 01
  if (cur == X):
    continue
  _sum = 0
  for i in range(len(X)):
    light_x = lights[X[i]]
    light_cur = lights[cur[i]]
    for j in range(7):
      if (light_x[j] != light_cur[j]):
        _sum += 1
    if (_sum > P):
      break
  if (1 <= _sum <= P):
    ans += 1
print(ans)
