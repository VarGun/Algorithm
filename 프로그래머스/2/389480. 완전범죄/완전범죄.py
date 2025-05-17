
def solution(info, n, m):
    ans = float('inf')
    flag = False
    length = len(info)
    visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(length)]
    
    def dfs(info, depth, n, m, length, maxN, maxM):
        nonlocal ans, flag
        
        if(depth == length):
            ans = min(ans, n)
            flag = True
            return

        if(n >= ans or visited[depth][n][m]):
            return
        visited[depth][n][m] = True
        
        nextN = n + info[depth][0]
        nextM = m + info[depth][1]
        if(nextN < maxN):
            dfs(info, depth + 1, nextN, m, length, maxN, maxM)
        if(nextM < maxM):
            dfs(info, depth + 1, n, nextM, length, maxN, maxM)
    
    dfs(info, 0, 0, 0, length, n, m)
    
    return ans if ans != float('inf') else -1
