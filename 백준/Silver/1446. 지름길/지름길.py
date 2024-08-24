import sys
input = sys.stdin.readline

def solution(arr):
  dist_list = [i for i in range(D + 1)]

  for i in range(len(dist_list)):
    if(i > 0):
      dist_list[i] = min(dist_list[i], dist_list[i - 1] + 1)
    for start, end, distance in arr:
      if(start == i and end <= D and distance + dist_list[i] < dist_list[end]):
        dist_list[end] = dist_list[i] + distance

  return dist_list[D]


if __name__ == "__main__":
  N, D = map(int, input().split())
  arr = []
  for _ in range(N):
    arr.append(list(map(int,input().split())))
  print(solution(arr))