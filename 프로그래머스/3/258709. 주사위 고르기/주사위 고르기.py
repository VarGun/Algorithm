import itertools

def left_most_bin(left, right, scores, tar):
    if(left > right):
        return left
    
    mid = (left + right) // 2
    if(scores[mid] >= tar):
        return left_most_bin(left, mid - 1, scores, tar)
    else:
        return left_most_bin(mid + 1, right, scores, tar)
    

def solution(dice):
    answer = []
    a_comb = list(itertools.combinations(range(len(dice)), len(dice) // 2)) # A 가 가진 주사위

    scores_idx = list(itertools.product(range(6), repeat = len(dice) // 2))
    
    max_boundary = 0
    for a_dice in a_comb: # a_dice : A 가 선택한 주사위 / (0, 1)
        
        b_dice = [] # B 가 선택할 주사위
        for i in range(len(dice)):
            if(i not in a_dice): # 남는 거 넣기
                b_dice.append(i)
        a_dice = list(a_dice)
        
        # 뽑을 수 있는 모든 idx / (0, 0), (0, 1) ... (6, 5), (6, 6)
        
        a_scores = [] # a 점수 저장
        b_scores = [] # b 점수 저장
        
        a_score = 0
        
        for i in range(len(scores_idx)): # (0, 0), (0, 1) ... (6, 5), (6, 6)
            b_score = 0
            a_score = 0
            idx = list(scores_idx[i]) # [0, 0]
                
            for j in range(len(idx)):
                b_score += dice[b_dice[j]][idx[j]]
                a_score += dice[a_dice[j]][idx[j]]
            b_scores.append(b_score)
            a_scores.append(a_score)
            
        b_scores.sort()
        boundary = 0
        for i in range(len(a_scores)):
            a_score = a_scores[i] # 경계 찾을 점수 -> 이 점수로 이길 확률
            boundary += left_most_bin(0, len(b_scores) - 1, b_scores, a_score) # 얘가 클 수록 이길 확률 높음
        if(max_boundary < boundary):
            # print('a_dice : ', a_dice)
            answer = a_dice
            # print('boundary : ', boundary)
            max_boundary = boundary
            
    
    for i in range(len(answer)):
        answer[i] += 1
    return answer