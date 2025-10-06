from itertools import combinations

def solution(orders, course):
    answer = []
    order_dict = {} 
    cnt_dict = {} # course 길이 별 최대 주문 횟수 저장
    course_dict = {} # course 길이 별 후보 저장
    
    for i in range(len(orders)): # 정렬하고 진행 (WX 랑 XW 랑 다르게 잡힘)
        order = list(orders[i])
        order.sort()
        orders[i] = ''.join(order)
    
    for c in course:
        cnt_dict[c] = 0
        course_dict[c] = []
    
    # 각 주문 메뉴들로 조합 만들고, 그 조합이 없으면 추가. 있으면 갯수 증가
    for order in orders: # order : ABCFG 형태
        for i in range(2, len(order) + 1):
            order_comb = list(combinations(order, i))
            for comb in order_comb:
                order_join = ''.join(comb)
                if(order_join not in order_dict):
                    order_dict[order_join] = 0
                order_dict[order_join] += 1

    for key in order_dict:
        course_length = len(key) # 	key :  AC , order_dict[key] :  3 (코스후보, 주문횟수)
        if(course_length in course and order_dict[key] >= 2): # course 길이에 맞고, 2 번 이상인 경우
            # if(cnt_dict[course_length] < order_dict[key]): # 기존의 최대 주문 횟수보다 클 경우
            #     course_dict[course_length] = [key] # 리스트 새로 갱신
            #     cnt_dict[course_length] = order_dict[key] # 길이도 갱신
            # elif(cnt_dict[course_length] == order_dict[key]): # 기존의 최대 주문 횟수와 같을 경우
            #     course_dict[course_length].append(key) # 추가만
            # print('course_dict[course_length] : ', course_dict[course_length])
            if(course_dict[course_length] == []): # 처음일 경우
                course_dict[course_length].append(key)
            else: # 메뉴가 이미 있을 경우
                if(order_dict[course_dict[course_length][0]] < order_dict[key]): # 길이 갱신
                    course_dict[course_length] = [key]
                elif(order_dict[course_dict[course_length][0]] == order_dict[key]):
                    course_dict[course_length].append(key)
            
                
    
    for key in course_dict:
        for item in course_dict[key]:
            answer.append(item)
            
    answer.sort()
    return answer