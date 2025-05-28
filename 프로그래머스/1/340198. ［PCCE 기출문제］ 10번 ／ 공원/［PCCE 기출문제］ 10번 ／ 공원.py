from collections import deque

def cal_dis(y, x, park):
    
    dis_y = 1
    dis_x = 1
    
    for i in range(y + 1, len(park)):
        if(park[i][x] == '-1'):
            dis_y += 1
        else:
            break
        
    for i in range(x + 1, len(park[0])):
        if(park[y][i] == '-1'):
            dis_x += 1
        else:
            break
    
    return [dis_y, dis_x]

def search(y, x, gugu, park, dy, dx):
    visited = [[False for _ in range(gugu)] for _ in range(gugu)]
    q = deque()
    q.append([y, x])
    visited[0][0] = True
    while q:
        head = q.popleft()
        yy = head[0]
        xx = head[1]
        for i in range(4):
            ny = yy + dy[i]
            nx = xx + dx[i]
            if(y <= ny < y + gugu and x <= nx < x + gugu and visited[ny - y][nx - x] == False):
                if(park[ny][nx] == '-1'):
                    q.append([ny, nx])
                    visited[ny - y][nx - x] = True
                else:
                    return False
    return True



def gun(y, x, park, dy, dx):
    cal = cal_dis(y, x, park)
    gugu = min(cal[0], cal[1]) # 둘 중 더 짧은 거리까지만 돌면 됨
    if(gugu == 1):
        return 1
    
    while gugu:
        res = search(y, x, gugu, park, dy, dx)
        if(res == True):
            return gugu
        gugu -= 1
        
    return gugu

def solution(mats, park):
    answer = -1
    mats.sort()
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    
    
    # for i in range(len(park)):
    #     print(park[i])
    # print(cal_dis(2, 1, park))
    
    _max = -1
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if(park[i][j] == '-1'):
                res = gun(i, j, park, dy, dx)
                if(_max < res):
                    _max = res
    
    print('_max : ', _max)
    for i in range(len(mats)):
        if(mats[i] <= _max):
            answer = mats[i]
        else:
            return answer
    
    return answer