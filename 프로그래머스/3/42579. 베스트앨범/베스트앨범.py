def solution(genres, plays):
    answer = []
    gun = []
    cnt_dic = {}
    dic = {}

    for i in range(len(genres)):
        if(genres[i] not in cnt_dic):
            cnt_dic[genres[i]] = plays[i]
        else:
            cnt_dic[genres[i]] += plays[i]
    
    for i in range(len(genres)):
        gun.append([cnt_dic[genres[i]], genres[i], plays[i], i])
    
    
    gun.sort(key = lambda x:(-x[0], -x[2], x[3]))
    print(gun)
    
    gugu = '-1' # 첫번째 장르
    cnt = 0
    for i in range(len(gun)): # gun[i] = [3100, 'pop', 2500, 4]
        if(gugu != gun[i][1]):
            cnt = 1
            gugu = gun[i][1]
            answer.append(gun[i][3])
        else:
            if(cnt >= 2):
                continue
            answer.append(gun[i][3])
            cnt += 1
        
    
    
#     for i in gun: # i = [3100, 'pop', 2500, 4]
#         if(i[1] not in dic):
#             dic[i[1]] = [[i[1], i[2]]]
#         else:
#             dic[i[0]].append([i[1], i[2]])
    
#     for key in dic:
#         tar = dic[key]
#         cnt = 0
#         for i in range(len(tar)):
#             if(cnt < 2):
#                 answer.append(tar[i][1])
#                 cnt += 1
#             else:
#                 break
    
    
    return answer