from collections import deque    

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    arr  = [[0 for _ in range(102)] for _ in range(102)]
    visited  = [[-1 for _ in range(102)] for _ in range(102)]
    
    for i in range(len(rectangle)):
        r = rectangle[i] # [1,1,7,4]
        x1, y1, x2, y2 = map(lambda x:x * 2, r)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if(y1 < y < y2 and x1 < x < x2):
                    arr[y][x] = 1
                elif(arr[y][x] != 1):
                    arr[y][x] = 2
    
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    
    q = deque()
    q.append((characterY * 2, characterX * 2))
    visited[characterY * 2][characterX * 2] = 1
    
    while q:
        y, x = q.popleft()
        if(x == itemX * 2 and y == itemY * 2):
            answer = visited[y][x] // 2
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if(visited[ny][nx] == -1):
                if arr[ny][nx] == 2:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
    
    return answer