import sys
input = sys.stdin.readline

N = int(input())


def on_light(idx, cur):  # 전구 켜는 함수
  if idx == 0:
    cur[0] = 1 - cur[0]
    cur[1] = 1 - cur[1]
  elif idx == N - 1:
    cur[N - 1] = 1 - cur[N - 1]
    cur[N - 2] = 1 - cur[N - 2]
  else:
    for i in range(idx - 1, idx + 2):
      cur[i] = 1 - cur[i]


cur_off = list(map(int, input().strip()))  # 현재 상태
tar = list(map(int, input().strip()))  # 목표 상태

cur_on = cur_off[:]
on_light(0, cur_on)  # 현재 상태(켰음)


def on_or_off(cur):  # cur[i - 1] 이 tar[i - 1] 과 다르면 전구 켜기
  global tar, N
  cnt = 0
  for i in range(1, N):
    if tar[i - 1] != cur[i - 1]:
      cnt += 1
      on_light(i, cur)
  return cnt if cur == tar else -1


off_cnt = on_or_off(cur_off[:])
res = on_or_off(cur_on)

on_cnt = res + 1 if res != -1 else -1  # 이미 한 번 켰으니까

if on_cnt == -1 and off_cnt == -1:
  print(-1)
elif on_cnt == -1:
  print(off_cnt)
elif off_cnt == -1:
  print(on_cnt)
else:
  print(min(on_cnt, off_cnt))
