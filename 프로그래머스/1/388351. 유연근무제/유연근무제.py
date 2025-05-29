def convert_time(time):
    new_time = 0
    if(time % 100 + 10 >= 60):
        return (time // 100 + 1) * 100 + (time % 100 + 10) % 60
    else:
        return time + 10

def solution(schedules, timelogs, startday):
    answer = len(schedules)
    gun = [[0, 1, 2, 3, 4], 
           [0, 1, 2, 3, 6], 
           [0, 1, 2, 5, 6],
           [0, 1, 4, 5, 6],
           [0, 3, 4, 5, 6],
           [2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5]]
    tar = []
    for i in range(5):
        tar.append(gun[startday - 1][i])
    print('tar : ', tar) # 2, 3, 4, 5, 6
    
    
    
    for i in range(len(schedules)): # 0, 1, 2
        chul = schedules[i] # 700
        flag = False
        for j in range(5):
            if(timelogs[i][tar[j]] > convert_time(chul)):
                flag = True
                break
        if(flag):
            answer -= 1
        
    
    return answer