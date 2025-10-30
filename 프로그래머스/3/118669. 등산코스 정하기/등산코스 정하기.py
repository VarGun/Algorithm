import heapq
def solution(n, paths, gates, summits):
    summits = set(summits)
    inf = 100000000
    graph = [[] for _ in range(n + 1)]
    intens = [inf for _ in range(n + 1)]
    
    for p in paths:
        a, b, d = p[0], p[1], p[2]
        graph[a].append((d, b))
        graph[b].append((d, a))
    
    pq = []
    for g in gates:
        heapq.heappush(pq,(0, g))
        intens[g] = 0
    
    while pq:
        cur_cost, cur = heapq.heappop(pq)
        if(cur in summits):
            continue
        if(cur_cost > intens[cur]):
            continue
        for w, nxt in graph[cur]:
            new_intens = max(cur_cost, w)
            if(intens[nxt] > new_intens):
                intens[nxt] = new_intens
                heapq.heappush(pq, (new_intens, nxt))
    
    answer = []
    _min = inf
    
    
    for i in range(len(intens)):
        if(i in summits and intens[i] < _min):
            _min = intens[i]
            answer = [i, _min]
    
    return answer