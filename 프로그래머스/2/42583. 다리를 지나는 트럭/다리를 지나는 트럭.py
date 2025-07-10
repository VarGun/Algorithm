from collections import deque
def solution(bridge_length, weight, truck_weights):
    ans = 0
    gun = deque()
#     trucks = deque(truck_weights)
#     cur = 0 # 트럭 현재 순서
#     while(True):
#         if(cur <= len(truck_weights) - 1 and sum(gun) + truck_weights[cur] <= weight): # 못 넣음
   
    
    for i in range(bridge_length):
        gun.append(0)
    cur = 0 # 현재 트럭 순서
    _sum = 0
    while(True):
        ans += 1
        gugu = gun.popleft()
        flag = False
        if(gugu != 0): # 차가 나옴
            _sum -= gugu
        if(cur <= len(truck_weights) - 1 and _sum + truck_weights[cur] <= weight):
            gun.append(truck_weights[cur])
            _sum += truck_weights[cur]
            cur += 1
        else:
            gun.append(0)
        if(cur == len(truck_weights) and _sum == 0):
            break
    
    # print(gun)
    # print(sum(gun))
    return ans