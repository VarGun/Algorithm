def is_valid(S):
    for x, y, a in S:
        if a == 0: # 기둥
            # 땅이거나, 아래에 기둥이 있거나, 한쪽 끝에 기둥이 있거나
            if(y == 0 or (x, y - 1, 0) in S or (x - 1, y, 1) in S or (x, y, 1) in S):
                continue
            return False
        else: # 보
            # 
            if((x, y - 1, 0) in S or (x + 1, y - 1, 0) in S or ((x + 1, y, 1) in S and (x - 1, y, a) in S)):
                continue
            return False
            
    return True


def solution(n, build_frame):
    S = set()
    for x, y, a, b in build_frame:
        if b == 1: # 설치
            S.add((x, y, a))
            if(not is_valid(S)):
                S.remove((x, y, a))
        else: # 삭제
            if((x, y, a) in S):
                S.remove((x, y, a))
                if(not is_valid(S)):
                    S.add((x, y, a))
    
    S = list(map(list, S))
    S.sort(key = lambda x : (x[0], x[1], x[2]))
            
    return S