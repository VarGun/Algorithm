import heapq

def dijkstra(node, n, nodes):
    inf = float('inf')
    dist = [inf for _ in range(n + 1)] # 각 노드까지의 거리
    dist[node] = 0
    pq = [(0, node)] # (비용(0), 시작점)
    
    while pq:
        cost, u = heapq.heappop(pq) # 큐에 저장되어 있는 (비용, 노드)
        if cost > dist[u]: # 기존 거리 값보다 새로운 값이 크면 무시
            continue
        for v, w in nodes[u]: # 지금 보려는 노드(u)와 인접한 노드들 대상
            # v : 인접한 노드들, w : 비용
            next_d = cost + w # u를 거쳐 v로 가는 새 비용
            if(dist[v] > next_d): # 새 비용이 기존 최단(dist[v])보다 싸면
                dist[v] = next_d # 갱싱
                heapq.heappush(pq, (next_d, v))
    return dist


def solution(n, s, a, b, fares):
    
    answer = 0
    nodes = [[] for _ in range(n + 1)]
    
    for i in range(len(fares)): # 거리 저장 / c -> d : f, d -> c : f
        c, d, f = fares[i][0], fares[i][1], fares[i][2]
        nodes[c].append((d, f))
        nodes[d].append((c, f))
    
    
    distS = dijkstra(s, n, nodes) # S 에서 각 노드까지의 최단거리를 구한 리스트
    distA = dijkstra(a, n, nodes) # A 에서 각 노드까지의 최단거리를 구한 리스트
    distB = dijkstra(b, n, nodes) # B 에서 각 노드까지의 최단거리를 구한 리스트
    
    answer = min(distS[k] + distA[k] + distB[k] for k in range(1, n + 1))
    return answer