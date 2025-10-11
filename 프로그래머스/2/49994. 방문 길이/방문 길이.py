def solution(dirs):
    answer = 0
    visited = [[{'L' : False, 'R' : False, 'U' : False, 'D' : False} for _ in range(11)] for _ in range(11)]
    sx, sy = 5, 5 # 초기 좌표 (시작)
    # L = (0, -1), R = (0, 1), U = (-1, 0), D = (1, 0)
    dy = {'L' : 0, 'R' : 0, 'U' : -1, 'D' : 1}
    dx = {'L' : -1, 'R' : 1, 'U' : 0, 'D' : 0}
    oppsite = {'L' : 'R', 'R' : 'L', 'U' : 'D', 'D' : 'U' }
    for d in dirs:
        ny = sy + dy[d]
        nx = sx + dx[d]
        if not (0 <= ny < 11 and 0 <= nx < 11):
            continue
        if(0 <= ny < 11 and 0 <= nx < 11):
            if(not visited[sy][sx][d]):
                answer += 1
                visited[sy][sx][d] = True
                visited[ny][nx][oppsite[d]] = True
            sy, sx = ny, nx
    return answer