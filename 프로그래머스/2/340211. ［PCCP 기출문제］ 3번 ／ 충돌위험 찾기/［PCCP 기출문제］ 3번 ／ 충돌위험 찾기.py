import copy

def decide_direction(tar, current):
    if(tar[0] > current[0]): # 목적지 y 가 크면
        return [1, 0] # y 1 증가
    elif(tar[0] < current[0]):
        return [-1, 0]
    elif(tar[1] > current[1]):
        return [0, 1]
    return [0, -1]

def solution(points, routes):
    answer = 0
    current = [] # 로봇 현재 위치
    tar = [] # 목적지
    tar_i = [1 for _ in range(len(routes))]
    for i in range(len(routes)):
        cur_copy = copy.deepcopy(points[routes[i][0] - 1])
        tar_copy = copy.deepcopy(points[routes[i][1] - 1])
        current.append(cur_copy) # 처음 위치
        tar.append(tar_copy) # 다음 위치
    ended = [False for _ in range(len(routes))] # 로봇들 끝났는지 체크
    
    # 처음 충돌 검사
    v_map = [[0 for _ in range(101)] for _ in range(101)] # 그 칸에 있는 로봇 수 -> 이미 있는 칸인지 검사용
    v_TF = [[False for _ in range(101)] for _ in range(101)] # 겹쳤는지 검사용
    for i in range(len(routes)):
        if(v_map[current[i][0]][current[i][1]] >= 1): # 이미 그 자리에 로봇이 있었으면
            v_TF[current[i][0]][current[i][1]] = True # 겹침 체크

        v_map[current[i][0]][current[i][1]] += 1 # 로봇 이동
         # 충돌 검사
    for i in range(len(v_TF)):
        for j in range(len(v_TF[i])):
            if(v_TF[i][j] == True):
                print('충돌 i : ', i, ', j : ', j)

        answer += sum(v_TF[i])
    
    
    cnt = 0
    
    while(sum(ended) < len(routes) ):
        cnt += 1
        
        v_map = [[0 for _ in range(101)] for _ in range(101)] # 그 칸에 있는 로봇 수 -> 이미 있는 칸인지 검사용
        v_TF = [[False for _ in range(101)] for _ in range(101)] # 겹쳤는지 검사용
        # print('current : ', current)
        # print('tar : ', tar)
        # print('--------------')
        # 로봇 하나씩
        for i in range(len(routes)):
            # 끝난 애면 냅두기
            if(ended[i]):
                continue
            # 이동 방향
            # tar[i] : i 번째 로봇 목적지, current[i] : i 번째 로봇 현재
            direction = decide_direction(tar[i], current[i]) # 로봇 목적지, 로봇 현재
            # 이동
            current[i][0] += direction[0]
            current[i][1] += direction[1]
            if(v_map[current[i][0]][current[i][1]] >= 1): # 이미 그 자리에 로봇이 있었으면
                v_TF[current[i][0]][current[i][1]] = True # 겹침 체크
            
            v_map[current[i][0]][current[i][1]] += 1 # 로봇 이동
            
            # 목적지 도달했는지 검사
            if(tar[i][0] == current[i][0] and tar[i][1] == current[i][1]):
                tar_i[i] += 1
                if(tar_i[i] >= len(routes[i])): # 최종 목적지까지 다 끝났으면
                    ended[i] = True
                else: # 최종 목적지 아니라면
                    # 목적지 갱신
                    # if(i == 0):
                        # print('routes[tar_i[i]] : ', routes[tar_i[i]])
                        # print('tar_i[i] : ', tar_i[i])
                    # tar[i] = points[tar_i[i] - 1]
                    tar[i] = points[routes[i][tar_i[i]] - 1]
        # 충돌 검사
        for i in range(len(v_TF)):
            # for j in range(len(v_TF[i])):
            #     if(v_TF[i][j] == True):
            #         print('충돌 i : ', i, ', j : ', j)
            # if(sum(v_TF[i]) != 0):
            #     print('gml')
            
            answer += sum(v_TF[i])
        
        # 3개 다 끝났으면 break
        if(sum(ended) == len(routes)):
            break
            
    
    return answer