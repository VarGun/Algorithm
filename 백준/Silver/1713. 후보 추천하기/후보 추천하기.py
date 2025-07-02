n = int(input())

t = int(input())

rec = list(map(int, input().split()))


def find_min(tar, _min):  # 대상 배열, 최소값 (여기서는 첫 요소의 1번째 인덱스로 돌릴 예정)
  min_i = 0  # 그 학생의 인덱스
  for i in range(1, len(tar)):
    if (tar[i][1] < _min):
      _min = tar[i][1]
      min_i = i  # 학생
  return min_i  # -1 이면


pic = []

for i in range(t):
  flag = False  # 없니 ?
  for j in range(len(pic)):
    if (rec[i] == pic[j][0]):  # 있을 경우
      pic[j][1] += 1
      flag = True  # 있네
  if (not flag):  # 없을 경우
    if (len(pic) < n):  # 들어갈 수 있네
      pic.append([rec[i], 1])
    else:  # 못들어가네
      min_rec = find_min(pic, pic[0][1])  # 인덱스만
      del pic[min_rec]
      pic.append([rec[i], 1])

pic.sort(key=lambda x: x[0])

for i in range(len(pic)):
  print(pic[i][0], end=' ')