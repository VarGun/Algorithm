from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def bfs(y, x, height, width, land, visited, oil_line):
    global dy, dx
    cnt = 1
    
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    oils = set()
    oils.add(x)
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if(0 <= ny < height and 0 <= nx < width and not visited[ny][nx] and land[ny][nx] == 1):
                q.append((ny, nx))
                oils.add(nx)
                visited[ny][nx] = True
                cnt += 1
    # if(x == 6):
    #     print('gmlgml')
    
    
    oils_list = list(oils)
    # print('oils_list :', oils_list)
    for i in range(len(oils_list)):
        oil_line[oils_list[i]] += cnt
    
    return cnt

def solution(land):
    answer = 0
    
    height = len(land)
    width = len(land[0])
    _max = -1   
    visited = [[False for _ in range(width)] for _ in range(height)]
    oil_line = [0 for _ in range(width)]
    for i in range(width):
        # print('i : ', i)
        line_cnt = 0
        for j in range(height):
            if(land[j][i] == 1 and not visited[j][i]):
                # print('j : ', j)
                bfs(j, i, height, width, land, visited, oil_line)
                # print('cnt : ', cnt)
        # if(_max < line_cnt):
        #     _max = line_cnt    
    
    
    return max(oil_line)