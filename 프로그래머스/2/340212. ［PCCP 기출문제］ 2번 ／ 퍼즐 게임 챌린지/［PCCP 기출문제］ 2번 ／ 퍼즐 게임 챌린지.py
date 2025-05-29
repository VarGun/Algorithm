def gun(diffs, times, lv, limit):
    sum_t = 0
    flag = False
    for i in range(len(diffs)):
        if(diffs[i] <= lv): # lv 가 크거나 같음 : 바로 통과
            sum_t += times[i]
        else: # 틀림
            if(i == 0):
                sum_t += times[i] * (diffs[i] - lv + 1)
            else:
                sum_t += times[i] * (diffs[i] - lv + 1) + times[i - 1] * (diffs[i] - lv)
        if(sum_t > limit):
            flag = True
            break
    if(flag): # 넘어감. lv 가 더 커야 해
        return False
    else: # 넘어가지 않음. lv 가 더 작아질 수 있어
        return True

def solution(diffs, times, limit):
    ans = max(diffs)
    left = min(diffs)
    right = max(diffs)
    
    while left <= right:
        mid = (left + right) // 2
        if(gun(diffs, times, mid, limit)):
            right = mid - 1
            ans = min(ans, mid)
        else:
            left = mid + 1
            
    
    return ans