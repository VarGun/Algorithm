from itertools import combinations

def make_str(lst):
    return ''.join(lst)

def compare_skill(skill, tree): # 선행 스킬, 대상 스킬 트리
    sk_idx = 0
    tr_idx = 0
    for i in range(len(tree)):
        if(tree[i] in skill): # 상관 있는 스킬일 경우
            if(skill[sk_idx] == tree[i]):
                sk_idx += 1
                tr_idx += 1
            else:
                return False
    return True

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        if(compare_skill(skill, tree)):
            answer += 1
    
    return answer