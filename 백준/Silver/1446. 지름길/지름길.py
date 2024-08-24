import sys
input = sys.stdin.readline

def solution(arr):
  dist_list = [i for i in range(D + 1)] # 전체 지점의 최단 거리 저장 (0 ~ 목적지)

  for i in range(len(dist_list)):
    if(i > 0):
      dist_list[i] = min(dist_list[i], dist_list[i - 1] + 1) # 현재까지의 최단 거리랑, 직전 지점까지의 거리 + 1 비교
    for start, end, distance in arr: # 시작점, 끝점, 거리(비용)
      # 시작점 차례(start == i)이고, 끝점이 목적지보다 멀리 있지 않고, (현재위치 + 지름길 거리)가 현재 끝점까지의 거리보다 짧으면
      if(start == i and end <= D and distance + dist_list[i] < dist_list[end]):
        dist_list[end] = dist_list[i] + distance # 끝점까지의 거리는 현재지점까지의 거리 + 지름길 거리

  return dist_list[D]


if __name__ == "__main__":
  N, D = map(int, input().split())
  arr = []
  for _ in range(N):
    arr.append(list(map(int,input().split())))
  print(solution(arr))
