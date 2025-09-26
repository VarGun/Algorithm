from collections import deque
def bfs(y, x, visited, tar, rows, cols, map_storage, cnt, is_car): # 지게차 bfs
    global sum_storage
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    # for i in range(len(map_storage)):
    #     print(map_storage[i])
    q = deque()
    q.append([y, x])
    visited[y][x] = True
    while q:
        head = q.popleft()
        y = head[0]
        x = head[1]
        # print('y : ', y)
        # print('x : ', x)
        # print('------------------')
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 갈 수는 있음
            if(0 <= ny < rows and 0 <= nx < cols and visited[ny][nx] == False):
                visited[ny][nx] = True
                if(is_car):
                    if(map_storage[ny][nx] == -1):
                        q.append([ny, nx])
                else:
                    q.append([ny, nx])
                if(map_storage[ny][nx] == tar):
                    map_storage[ny][nx] = -1
                    cnt += 1
                # if(is_car):
                #     if(map_storage[ny][nx] == -1):
                #         q.append([ny, nx])
                #     else:
                #         if(map_storage[ny][nx] == tar):
                #             map_storage[ny][nx] = -1
                #             cnt += 1
                # else:
                #     q.append([ny, nx])
                #     if(map_storage[ny][nx] == tar):
                #         map_storage[ny][nx] = -1
                #         cnt += 1
                    
                        # q.append([ny, nx])
    sum_storage -= cnt

def gun_bfs(y, x, visited, tar, rows, cols, map_storage, cnt): # 크레인 bfs
    global sum_storage
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    for i in range(len(map_storage)):
        print(map_storage[i])
    q = deque()
    q.append([y, x])
    visited[y][x] = True
    while q:
        head = q.popleft()
        y = head[0]
        x = head[1]
        # print('y : ', y)
        # print('x : ', x)
        # print('------------------')
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 갈 수는 있음
            if(0 <= ny < rows and 0 <= nx < cols and visited[ny][nx] == False):
                visited[ny][nx] = True
                q.append([ny, nx])
                if(map_storage[ny][nx] == tar):
                    map_storage[ny][nx] = -1
                    cnt += 1
                    
    sum_storage -= cnt
    
    


def solution(storage, requests):
    global sum_storage
    cnt = 0 # 빠진 컨테이너 수
    sum_storage = len(storage) * len(storage[0]) # 처음 전체 갯수
    map_storage = [[-1] * (len(storage[0]) + 2)]
    for i in range(len(storage)):
        line = [-1, *storage[i], -1]
        map_storage.append(line)
    map_storage.append([-1]* (len(storage[0]) + 2))
    
    rows = len(map_storage)
    cols = len(map_storage[0])
    
    for i in range(len(requests)): # requests 수 만큼 돌 거
        req = requests[i]
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        bfs(0, 0, visited, requests[i][0], rows, cols, map_storage, cnt, len(req) == 1)
            
        # bfs(0, 0, visited, tar)
    # visited = [[False for _ in range(cols)] for _ in range(rows)]
    # bfs(0, 0, visited, requests[0], rows, cols, map_storage, cnt, False)
    for i in range(len(map_storage)):
        print(map_storage[i])
    print(sum_storage)
    
    return sum_storage