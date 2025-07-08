def solution(arr):
    answer = []
    ans_1 = [1, 2, 3, 4, 5] * 2000
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5] * (10000 // 8)
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    cnt = [0, 0, 0]
    for i in range(len(arr)):
        if(arr[i] == ans_1[i]):
            cnt[0] += 1
        if(arr[i] == ans_2[i]):
            cnt[1] += 1
        if(arr[i] == ans_3[i]):
            cnt[2] += 1
    print(cnt)
    
    _max = max(cnt)
    print(_max)
    for i in range(3):
        if(cnt[i] == _max):
            answer.append(i + 1)
    
    return answer