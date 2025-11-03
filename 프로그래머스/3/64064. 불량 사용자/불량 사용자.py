def is_match(u, b):
    if(len(u) != len(b)): # 길이 다르면 안됨
        return False
    for i in range(len(b)):
        if(b[i] == '*'):
            continue
        if(u[i] != b[i]):
            return False
    return True

def back_t(idx, selected, banned_id, possible, res):
    if(idx == len(banned_id)):
        res.add(frozenset(selected))
        return
    for u in possible[idx]:
        if u not in selected:
            selected.add(u)
            back_t(idx + 1, selected, banned_id, possible, res)
            selected.remove(u)
    

def solution(user_id, banned_id):
    answer = 0
    res = set()
    
    possible = []  # 각 불량 아이디별로 매칭 가능한 user_id 목록
    for b in banned_id:
        cur = []
        for u in user_id:
            if is_match(u, b):
                cur.append(u)
        possible.append(cur)
    print('possible : ', possible)

    back_t(0, set(), banned_id, possible, res)
    
    return len(res)