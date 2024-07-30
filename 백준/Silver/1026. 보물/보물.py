# 입력 받기
n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# a_list는 오름차순으로, b_list는 내림차순으로 정렬
a_list.sort()
b_list.sort(reverse=True)

# 두 리스트의 요소를 곱하여 합산
s = sum(a * b for a, b in zip(a_list, b_list))

# 결과 출력
print(s)
