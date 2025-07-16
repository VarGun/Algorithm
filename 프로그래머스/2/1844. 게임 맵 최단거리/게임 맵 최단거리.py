from collections import deque
def solution(arr): # 0 이 길, 1 이 벽
    answer = 0
    visited = [[-1 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        if(y == len(arr) - 1 and x == len(arr[0]) -1):
            return visited[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if(0 <= ny < len(arr) and 0 <= nx < len(arr[0]) and arr[ny][nx] == 1 and visited[ny][nx] == -1):
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
    
    return -1