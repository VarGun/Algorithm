def set_friends(friends):
    gift_dic = dict()
    for i in range(len(friends)):
        gift_dic[friends[i]] = [0, 0] # [보낸 횟수, 받은 횟수]
    return gift_dic


def solution(friends, gifts):
    answer = 0
    score_dict = set_friends(friends) # 선물 지수 기록용
    gift_dict = dict() # 선물 준 사람들 기록 / {'준 사람' {'받은 사람' : '준 횟수', '받은 사람' : '준 횟수'}}
    next_gift = dict() # 다음 달에 받을 선물 기록
    for i in range(len(friends)):
        gift_dict[friends[i]] = dict()
        next_gift[friends[i]] = 0
    
    for i in range(len(gifts)):
        sender, receiver = gifts[i].split()[0], gifts[i].split()[1]
        score_dict[sender][0] += 1 # 준 횟수 증가
        score_dict[receiver][1] += 1 # 받은 횟수 증가
        if(receiver not in gift_dict[sender]):
            gift_dict[sender][receiver] = 1
        else:
            gift_dict[sender][receiver] += 1
    
    for i in range(len(friends) - 1):
        for j in range(i + 1, len(friends)):
            a = friends[i]
            b = friends[j]
            score_a = score_dict[a][0] - score_dict[a][1]
            score_b = score_dict[b][0] - score_dict[b][1]
            
            if(b in gift_dict[a] or a in gift_dict[b]): # 준 기록 있을 경우
                if(b not in gift_dict[a]): # a 가 b 에게 주지 않았을 경우 -> b 만 줌
                    next_gift[b] += 1
                elif(a not in gift_dict[b]): # 반대, a 만 줌
                    next_gift[a] += 1
                else: # 둘 다 줌
                    if(gift_dict[a][b] != gift_dict[b][a]): # 둘이 준 횟수가 다름
                        if(gift_dict[a][b] > gift_dict[b][a]): # a 가 b 한테 더 많이 줌
                            next_gift[a] += 1 # a 가 받아야지
                        else: # b 가 a 한테 더 많이 줌
                            next_gift[b] += 1 # b 가 받아야지
                    else: # 둘이 준 횟수가 같음 -> 선물지수
                        if(score_a > score_b):
                            next_gift[a] += 1 # a 가 받아야지
                        elif(score_a < score_b):
                            next_gift[b] += 1 # b 가 받아야지
            else: # 준 기록 없을 경우 -> 선물 지수만 생각
                if(score_a > score_b):
                    next_gift[a] += 1 # a 가 받아야지
                elif(score_a < score_b):
                    next_gift[b] += 1 # b 가 받아야지
    

    # print('score_dict : ', score_dict)
    # print('gift_dict : ', gift_dict)
    # print('next_gift : ', next_gift)
    # for i in next_gift:
    #     print(i)
    # print('max(next_gift, key=next_gift.get) : ', max(next_gift, key=next_gift.get))
    
    
    
    return next_gift[max(next_gift, key=next_gift.get)]