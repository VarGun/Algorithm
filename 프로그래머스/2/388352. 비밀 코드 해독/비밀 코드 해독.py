from itertools import combinations


def solution(n, q, ans):
    answer = 0
    nums = [i for i in range(1, n + 1)]
    set_q = [set(q[i]) for i in range(len(q))]

    combs = combinations(nums, 5)
    for com in combs:
        tar = set(com)
        correct = True
        for i in range(len(q)):
            if(ans[i] != len(list(set_q[i] & tar))):
                correct = False
                break
        if(correct):
            answer += 1
    
    
    return answer