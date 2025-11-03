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

    if(not check_left_top(y, x, place)):
        return False
    if(not check_left_bottom(y, x, place)):
        return False
    if(not check_right_top(y, x, place)):
        return False
    if(not check_right_bottom(y, x, place)):
        return False
    
    return True
    
    
def is_valid(place):
    for y in range(5):
        for x in range(5):
            if(place[y][x] == 'P'):
                p = find_p(y, x, place)
                if(not p):
                    return 0
    return 1

def solution(places):
    answer = []
    is_valid(places[0])
    for place in places:
        answer.append(is_valid(place))
    return answer