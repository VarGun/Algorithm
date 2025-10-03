from itertools import combinations

def left_most_bin(left, right, scores, tar):
    if(left > right):
        return left
    mid = (left + right) // 2
    if(scores[mid] >= tar):
        return left_most_bin(left, mid - 1, scores, tar)
    else:
        return left_most_bin(mid + 1, right, scores, tar)
    
    
def set_info(string):
    info_item = string.split()
    score = info_item[-1]
    return (info_item[:4], int(score))

def set_query(string):
    query_item = string.replace('and ','')
    query_item = query_item.split()
    score = query_item[-1]
    condition = ''
    for i in range(len(query_item) - 1):
        if(query_item[i] != '-'):
            condition += query_item[i] + ' '
    return (condition.strip(), int(score))
    
def solution(info, query):
    answer = []
    dic = {}
    for i in range(len(info)):
        condition, score = set_info(info[i])
        for j in range(5):
            for com in (combinations(condition, j)): # 0 ~ 4 개 조합
                key = ' '.join(com)
                if key not in dic:
                    dic[key] = []
                dic[key].append(score)
    
    for key in dic:
        dic[key].sort() # 점수 정렬 -> 이분 탐색
    
    for i in range(len(query)):
        condition, score = set_query(query[i])
        if(condition in dic):
            scores = dic[condition]
            position = left_most_bin(0, len(scores) - 1, scores, score)
            cnt = len(scores) - position
            answer.append(cnt)
        else:
            answer.append(0)
    
    return answer