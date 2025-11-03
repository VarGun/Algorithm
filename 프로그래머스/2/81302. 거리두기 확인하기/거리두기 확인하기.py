

# 주변에 있는 사람들 검사

def check_left_top(y, x, place):
    if(y == 0 or x == 0):
        return True
    
    if(place[y - 1][x - 1] == 'P'):
        if(place[y][x - 1] != 'X' or place[y - 1][x] != 'X'):
            return False
    return True
            
def check_left_bottom(y, x, place):
    if(y == 4 or x == 0):
        return True
    
    if(place[y + 1][x - 1] == 'P'):
        if(place[y][x - 1] != 'X' or place[y + 1][x] != 'X'):
            return False
    
    return True

def check_right_top(y, x, place):
    if(y == 0 or x == 4):
        return True
    

    if(place[y - 1][x + 1] == 'P'):
        if(place[y][x + 1] != 'X' or place[y - 1][x] != 'X'):
            return False
    
    return True

def check_right_bottom(y, x, place):
    if(y == 4 or x == 4):
        return True
    
    if(place[y + 1][x + 1] == 'P'):
        if(place[y][x + 1] != 'X' or place[y + 1][x] != 'X'):
            return False
    
    return True


def find_p(y, x, place):
    # 윗 방향
    for i in range(y - 1, y - 3, -1):
        if(i < 0):
            break
        if(place[i][x] == 'P'):
            return False
        elif(place[i][x] == 'X'):
            break
        
    # 아래
    for i in range(y + 1, y + 3):
        if(i >= 5):
            break
        if(place[i][x] == 'P'):
            return False
        elif(place[i][x] == 'X'):
            break
    
    # 왼쪽
    for i in range(x - 1, x - 3, -1):
        if(i < 0):
            break
        if(place[y][i] == 'P'):
            return False
        elif(place[y][i] == 'X'):
            break
            
    
    # 오른쪽
    for i in range(x + 1, x + 3):
        if(i >= 5):
            break
        if(place[y][i] == 'P'):
            return False
        elif(place[y][i] == 'X'):
            break
    
    # 대각선 4개
    lt = check_left_top(y, x, place)
    lb = check_left_bottom(y, x, place)
    rt = check_right_top(y, x, place)
    rb = check_right_bottom(y, x, place)
    
    if(lt and lb and rt and rb):
        return True
    
    return False
    
    
    # if(0 < y < 5 and 0 < x < 4):
    #     for lti in lt:
    #         p.add(lti)
    #     for lbi in lb:
    #         p.add(lbi)
    #     for rti in rt:
    #         p.add(rti)
    #     for rbi in rb:
    #         p.add(rbi)
    # elif(y == 0): # 아래만 검사
    #     for rbi in rb:
    #         p.add(rbi)
    #     for lbi in lb:
    #         p.add(lbi)
    # elif(y == 4): # 위만 검사
    #     for lti in lt:
    #         p.add(lti)
    #     for rti in rt:
    #         p.add(rti)
    # elif(x == 0): # 오른쪽만 검사
    #     for rti in rt:
    #         p.add(rti)
    #     for rbi in rb:
    #         p.add(rbi)
    # elif(x == 4): # 왼쪽만 검사
    #     for lti in lt:
    #         p.add(lti)
    #     for lbi in lb:
    #         p.add(lbi)
    # return p


def is_valid(place):
    for y in range(5):
        for x in range(5):
            if(place[y][x] == 'P'):
                p = find_p(y, x, place)
                
                # print('[y, x] : ', [y, x])
                # print('p : ', p)
                # print('---------------------')
                if(not p):
                    return 0
    
    return 1

def solution(places):
    answer = []
    is_valid(places[0])
    for place in places:
        answer.append(is_valid(place))
    return answer