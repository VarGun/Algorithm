def rotate_clock(key): # key 돌리기 (시계 방향)
    tmp_key = [[0 for _ in range(len(key[0]))] for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            tar = key[i][j]
            tmp_key[j][len(key) - 1 - i] = key[i][j]
    
    
    return tmp_key

def cal_holes(key): # 구멍 수 계산
    cnt = 0
    for i in range(len(key)):
        cnt += sum(key[i])
    return cnt


def check_match(key, lock):
    n = len(lock)
    m = len(key)
    size = n + 2 * (m - 1)
    board = [[1 for _ in range(size)] for _ in range(size)] # 확장
    
    for i in range(n):
        for j in range(n):
            board[i + m - 1][j + m - 1] = lock[i][j]
    
    for y in range(size - m + 1): # 0, 1, 2, 3, 4
        for x in range(size - m + 1): # 0, 1, 2, 3, 4 -> 여기까지가 범위 내 이동
            
            for i in range(m):
                for j in range(m):
                    board[y + i][x + j] += key[i][j]
            
            
            flag = True
            for i in range(n):
                for j in range(n):
                    if(board[i + m - 1][j + m - 1] != 1):
                        flag = False
                        break
                if(not flag):
                    break
            
            if(flag):
                return True
            
            for i in range(m):
                for j in range(m):
                    board[y + i][x + j] -= key[i][j]
            
    return False
    
    

def solution(key, lock):
    answer = True
    lock_h = len(lock) * len(lock[0]) - cal_holes(lock)
    key_h = cal_holes(key)
    
    if(lock_h > key_h):
        return False
    for _ in range(4):
        key = rotate_clock(key)
        if(check_match(key, lock)):
            return True
        
    return False