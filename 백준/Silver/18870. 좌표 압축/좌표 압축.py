N = int(input())
arr = list(map(int, input().split()))
# 중복 제거 -> list -> 정렬 -> 몇 번째에 있는지
s_list = sorted(list(set(arr)))

dic = {}
for i in range(len(s_list)):
  dic[s_list[i]] = i
for num in arr:
  print(dic[num], end=' ')
