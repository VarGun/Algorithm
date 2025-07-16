visited = []

def dfs(node, net):
    global visited
    for i in range(len(net[node])):
        if(not visited[net[node][i]]):
            visited[net[node][i]] = True
            dfs(net[node][i], net)

def solution(n, computers):
    global visited
    answer = 0
    visited = [False for _ in range(n)]
    net = [[] for _ in range(n)]
    
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if(i != j and computers[i][j] == 1):
                net[i].append(j)
    cnt = 0
    for i in range(n):
        if(not visited[i]):
            cnt += 1
            dfs(i, net)
        
    return cnt