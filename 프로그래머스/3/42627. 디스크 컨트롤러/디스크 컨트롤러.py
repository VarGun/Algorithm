from collections import deque
import heapq

def solution(jobs):
    jobs.sort()  # 요청 시각 기준 정렬
    heap = []
    time = 0      # 현재 시간
    i = 0         # jobs 인덱스
    total = 0     # 총 반환 시간
    count = len(jobs)

    while i < count or heap:
        # 현재 시간까지 들어온 작업을 힙에 넣음
        while i < count and jobs[i][0] <= time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))  # (소요시간, 요청시간)
            i += 1

        if heap:
            duration, start = heapq.heappop(heap)
            time += duration
            total += time - start
        else:
            # 작업 대기 큐가 비었으면 다음 요청 작업 시간으로 점프
            time = jobs[i][0]

    return total // count