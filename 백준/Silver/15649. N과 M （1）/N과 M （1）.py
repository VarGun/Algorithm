def solution(arr):
	if len(arr) == M:
		print(" ".join(map(str, arr)))
		return
    
	for i in range(1, N + 1):
		if i not in arr:
			solution(arr + [i])

if __name__ == "__main__":
	N, M = map(int, input().split())
	solution([])
